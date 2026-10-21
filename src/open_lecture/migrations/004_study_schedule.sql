CREATE TABLE study_schedule_slots (
    day TEXT NOT NULL,
    period TEXT NOT NULL CHECK (period IN ('Morning', 'Afternoon', 'Evening')),
    text TEXT NOT NULL,
    PRIMARY KEY (day, period)
);
CREATE TABLE study_schedule_exams (
    id TEXT PRIMARY KEY,
    day TEXT NOT NULL,
    title TEXT NOT NULL
);
INSERT INTO study_schedule_exams VALUES ('midterm-2026-221', '2026-10-27', 'ELEC 221 midterm');
INSERT INTO study_schedule_exams VALUES ('midterm-2026-271', '2026-10-29', 'ELEC 271 midterm');
INSERT INTO study_schedule_exams VALUES ('midterm-2026-226', '2026-10-30', 'ELEC 226 midterm');
INSERT INTO study_schedule_exams VALUES ('midterm-2026-231', '2026-10-30', 'ELEC 231 midterm');
