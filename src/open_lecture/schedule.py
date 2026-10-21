"""The workspace's single built-in study planner, independent of ordinary courses."""

from datetime import date
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


def add_exam(db, exam: ScheduleExam):
    result = {"id": str(uuid4()), "day": exam.day.isoformat(), "title": exam.title}
    with db.transaction() as connection:
        connection.execute("INSERT INTO study_schedule_exams VALUES (:id,:day,:title)", result)
    return result
