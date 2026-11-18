"""Start the bundled loopback server and report its URL to the Mac launcher."""

import socket

import uvicorn

from open_lecture.api import create_app


class DesktopServer(uvicorn.Server):
    async def startup(self, sockets=None):
        await super().startup(sockets=sockets)
        if self.started:
            port = self.servers[0].sockets[0].getsockname()[1]
            print(f"http://127.0.0.1:{port}", flush=True)


def main():
    with socket.socket() as listener:
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            listener.bind(("127.0.0.1", 8000))
        except OSError:
            listener.bind(("127.0.0.1", 0))
        server = DesktopServer(uvicorn.Config(create_app(), timeout_graceful_shutdown=5))
        server.run(sockets=[listener])
        if not server.started:
            raise SystemExit(1)


if __name__ == "__main__":
    main()
