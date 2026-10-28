"""The workspace's single built-in study planner, independent of ordinary courses."""

from datetime import date, datetime, timezone
from typing import Literal
from uuid import uuid4

from pydantic import Field

from .schemas import Model


class ScheduleSlot(Model):
    text: str = Field(max_length=10000)


class ScheduleExam(Model):
    day: date
    title: str = Field(min_length=1, max_length=200)


Period = Literal["Morning", "Afternoon", "Evening"]


def read_schedule(db):
    with db.connect() as connection:
        return {
            "slots": [dict(row) for row in connection.execute("SELECT * FROM study_schedule_slots ORDER BY day,period")],
            "exams": [dict(row) for row in connection.execute("SELECT * FROM study_schedule_exams ORDER BY day,title")],
        }


def save_slot(db, day: date, period: Period, text: str):
    with db.transaction() as connection:
        if text:
            connection.execute(
                "INSERT INTO study_schedule_slots VALUES (?,?,?) "
                "ON CONFLICT(day,period) DO UPDATE SET text=excluded.text",
                (day.isoformat(), period, text),
            )
        else:
            connection.execute("DELETE FROM study_schedule_slots WHERE day=? AND period=?", (day.isoformat(), period))
    return {"day": day.isoformat(), "period": period, "text": text}


class StudyPlan(Model):
    text: str = Field(max_length=100000)


def read_plan(db):
    """The one study-plan note (Markdown), shown in every course; empty until written."""
    with db.connect() as connection:
        row = connection.execute("SELECT text, updated_at FROM study_plan WHERE id=1").fetchone()
    return dict(row) if row else {"text": "", "updated_at": None}


def save_plan(db, text: str):
    result = {"text": text, "updated_at": datetime.now(timezone.utc).isoformat()}
    with db.transaction() as connection:
        connection.execute(
            "INSERT INTO study_plan VALUES (1,:text,:updated_at) "
            "ON CONFLICT(id) DO UPDATE SET text=excluded.text, updated_at=excluded.updated_at",
            result,
        )
    return result


def add_exam(db, exam: ScheduleExam):
    result = {"id": str(uuid4()), "day": exam.day.isoformat(), "title": exam.title}
    with db.transaction() as connection:
        connection.execute("INSERT INTO study_schedule_exams VALUES (:id,:day,:title)", result)
    return result
