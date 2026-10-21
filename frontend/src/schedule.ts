import type { Course } from "./api";

export const SCHEDULE_ID = "study-schedule";
export const SCHEDULE_COURSE: Course = {
  id: SCHEDULE_ID,
  code: "Study Schedule",
  title: "Calendar & study plans",
  created_at: "",
};

export const PERIODS = ["Morning", "Afternoon", "Evening"] as const;
export type Period = typeof PERIODS[number];
export type ScheduleSlot = { day: string; period: Period; text: string };
export type Exam = { id: string; day: string; title: string };
export type Schedule = { slots: ScheduleSlot[]; exams: Exam[] };

// Match complete course codes first, then unambiguous three-digit course numbers.
// Shared courses (e.g. ELEC 226/326) expose both numbers as aliases.
export function courseMentions(text: string, courses: Course[]) {
  const aliases = new Map<string, Course | null>();
  const add = (alias: string, course: Course) => {
    const key = alias.toLowerCase().replace(/\s+/g, "");
    if (!aliases.has(key)) aliases.set(key, course);
    else if (aliases.get(key)?.id !== course.id) aliases.set(key, null);
  };
  for (const course of courses) {
    add(course.code, course);
    const prefix = course.code.match(/^[a-z]+/i)?.[0];
    for (const number of course.code.match(/\d{3}\b/g) ?? []) {
      add(number, course);
      if (prefix) add(`${prefix} ${number}`, course);
    }
  }
  const escape = (value: string) => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  const patterns = [...aliases.keys()].filter((key) => aliases.get(key))
    .sort((a, b) => b.length - a.length)
    .map((key) => escape(key).replace(/^([a-z]+)(?=\d)/i, "$1\\s*"));
  if (!patterns.length) return [{ text, course: null }];
  const regex = new RegExp(`(?<![\\w/])(?:${patterns.join("|")})(?![\\w/])`, "gi");
  const result: { text: string; course: Course | null }[] = [];
  let offset = 0;
  for (const match of text.matchAll(regex)) {
    result.push({ text: text.slice(offset, match.index), course: null });
    result.push({ text: match[0], course: aliases.get(match[0].toLowerCase().replace(/\s+/g, "")) ?? null });
    offset = match.index! + match[0].length;
  }
  result.push({ text: text.slice(offset), course: null });
  return result;
}
