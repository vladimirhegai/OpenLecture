from fastapi.testclient import TestClient

from open_lecture.api import create_app


def test_schedule_seeds_exams_once_and_persists_slots(client, settings):
    initial = client.get("/api/v1/study-schedule").json()
    assert initial["slots"] == []
    assert [(exam["day"], exam["title"]) for exam in initial["exams"]] == [
        ("2026-10-27", "ELEC 221 midterm"),
        ("2026-10-29", "ELEC 271 midterm"),
        ("2026-10-30", "ELEC 226 midterm"),
        ("2026-10-30", "ELEC 231 midterm"),
    ]
    for period in ("Morning", "Afternoon", "Evening"):
        response = client.put(f"/api/v1/study-schedule/days/2026-10-25/{period}", json={"text": f"231 {period}"})
        assert response.status_code == 200
    with TestClient(create_app(settings)) as reopened:
        persisted = reopened.get("/api/v1/study-schedule").json()
        assert len(persisted["slots"]) == 3
        assert len(persisted["exams"]) == 4
    client.put("/api/v1/study-schedule/days/2026-10-25/Morning", json={"text": "Updated"})
    client.put("/api/v1/study-schedule/days/2026-10-25/Afternoon", json={"text": ""})
    slots = client.get("/api/v1/study-schedule").json()["slots"]
    assert len(slots) == 2
    assert next(slot for slot in slots if slot["period"] == "Morning")["text"] == "Updated"


def test_schedule_validates_inputs_and_manages_exams(client):
    assert client.put("/api/v1/study-schedule/days/2026-02-30/Morning", json={"text": "x"}).status_code == 422
    assert client.put("/api/v1/study-schedule/days/2026-10-25/Night", json={"text": "x"}).status_code == 422
    assert client.put("/api/v1/study-schedule/days/2026-10-25/Morning", json={"text": "x" * 10001}).status_code == 422
    assert client.post("/api/v1/study-schedule/exams", json={"day": "2026-11-02", "title": " "}).status_code == 422
    exam = client.post("/api/v1/study-schedule/exams", json={"day": "2026-11-02", "title": "231 test"}).json()
    assert exam in client.get("/api/v1/study-schedule").json()["exams"]
    client.delete(f"/api/v1/study-schedule/exams/{exam['id']}")
    assert exam not in client.get("/api/v1/study-schedule").json()["exams"]
    # The planner exists without creating an ordinary course.
    assert client.get("/api/v1/courses").json() == []
