"""Verify the relocated backend inside a mounted Mac disk image."""

import json
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.request import Request, urlopen


def main():
    server_script, data_dir = map(Path, sys.argv[1:])
    server_script = server_script.resolve()
    data_dir.mkdir()
    env = {**os.environ, "OPENLECTURE_DATA_DIR": str(data_dir), "OPENLECTURE_AGENT_RUNNER": "false"}
    with tempfile.TemporaryFile() as stdout:
        process = subprocess.Popen(
            [sys.executable, "-I", "-B", str(server_script)], cwd=data_dir, env=env, stdout=stdout
        )
        try:
            for _ in range(300):
                stdout.seek(0)
                address = stdout.readline().decode().strip()
                if address:
                    break
                if process.poll() is not None:
                    raise RuntimeError(f"Packaged server exited with status {process.returncode}")
                time.sleep(0.1)
            else:
                raise RuntimeError("Packaged server did not start")

            def fetch(path, data=None):
                request = Request(address + path)
                if data is not None:
                    request.data = json.dumps(data).encode()
                    request.add_header("Content-Type", "application/json")
                with urlopen(request, timeout=10) as response:
                    return response.read()

            assert json.loads(fetch("/api/v1/health"))["status"] == "ok"
            assert b'<div id="root">' in fetch("/")
            assert json.loads(fetch("/api/v1/courses")) == []
            course = json.loads(fetch("/api/v1/courses", {"code": "SMOKE", "title": "Packaged workspace"}))
            assert course["code"] == "SMOKE"
            assert (data_dir / "workspace.sqlite3").is_file()
        finally:
            process.terminate()
            try:
                process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait()


if __name__ == "__main__":
    main()
