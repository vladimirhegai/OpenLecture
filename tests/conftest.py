import time

import pytest
from fastapi.testclient import TestClient

from open_lecture.api import create_app
from open_lecture.config import Settings


@pytest.fixture
def settings(tmp_path):
    return Settings(data_dir=tmp_path / "workspace", api_token=None, agent_runner=False, _env_file=None)


@pytest.fixture
def client(settings):
    with TestClient(create_app(settings)) as client:
        yield client


@pytest.fixture
def course(client):
    return client.post("/api/v1/courses", json={"code": "ELEC 221", "title": "Circuits"}).json()["id"]


@pytest.fixture
def anyio_backend():
    return "asyncio"


def wait_job(client, course, job_id):
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline:
        job = client.get(f"/api/v1/courses/{course}/jobs/{job_id}").json()
        if job["status"] in {"completed", "failed"}:
            return job
        time.sleep(0.05)
    raise AssertionError("Ingestion did not finish within 15 seconds")
