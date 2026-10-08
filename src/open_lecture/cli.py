import argparse
import json

import uvicorn

from .config import Settings


def main():
    parser = argparse.ArgumentParser(description="Open Lecture local study backend")
    commands = parser.add_subparsers(dest="command", required=True)
    serve = commands.add_parser("serve", help="Start the HTTP API")
    serve.add_argument("--host", default="127.0.0.1")
    serve.add_argument("--port", type=int, default=8000)
    commands.add_parser("info", help="Show workspace location and capabilities")
    args = parser.parse_args()
    settings = Settings()
    if args.command == "info":
        print(
            json.dumps(
                {
                    "data_dir": str(settings.data_dir.resolve()),
                    "database": str(settings.database.resolve()),
                    "agent_runtime": "local_cli_bridge_and_mcp",
                    "circuits": "resistive_dc",
                },
                indent=2,
            )
        )
    else:
        if args.host not in {"127.0.0.1", "localhost", "::1"} and not settings.api_token:
            parser.error("Set OPENLECTURE_API_TOKEN before binding beyond loopback")
        from .api import create_app

        uvicorn.run(create_app(settings), host=args.host, port=args.port)


if __name__ == "__main__":
    main()
