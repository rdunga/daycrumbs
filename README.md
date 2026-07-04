# DayCrumbs

DayCrumbs is a small, opinionated, local-first command-line tool for leaving activity breadcrumbs while you work.

It is intentionally simple.

```bash
daycrumbs add Checked service logs, nothing unusual. Looking at IIS logs next
```

The idea is not to track every minute of your day or record every activity.

Just leave enough crumbs along the way to help reconstruct what happened later.

---

## Why I built this

A workday rarely happens in neat blocks.

You might spend five hours investigating an issue. Looking back, that can easily become:

> Worked on issue for 5 hours.

But those five hours were probably a sequence of smaller activities. Maybe you reproduced the issue, checked service logs and found nothing, looked through IIS logs, followed a theory that went nowhere, moved to the database, got interrupted by a colleague, and then returned to the investigation.

By the end of the day, you know you were busy. But if someone asks what you actually did, why it took that long, or where the time went, you have to reconstruct it from memory.

Memory tends to compress the whole thing into one vague block.

DayCrumbs came from wanting a low-friction way to leave small markers during the work itself:

```bash
daycrumbs add Checked service logs, no related errors found
daycrumbs add Reviewed IIS logs, requests look normal. Checking DB next
daycrumbs add Helped colleague trace incorrect commission config
daycrumbs add Found inconsistent status in DB for affected policies
```

None of these entries tells the whole story. Together, they leave enough of a trail to help you remember it.

---

## It does not need to be complete

DayCrumbs does not expect you to record everything.

You will forget entries. You might miss an hour. You might record several crumbs during one investigation and none during another. That is fine.

The goal is not a perfect timeline or an account of every minute. A few useful crumbs are enough to trigger memory later — when you are trying to remember what you did yesterday, prepare a timesheet, explain why an investigation took several hours, write a status update, or simply answer:

> Where did my day go?

---

## Why a command-line tool?

Because friction is where capture dies.

Opening another app, finding the right page, choosing a project, filling out a form — any of that is enough to postpone the entry until later. And later is when details start disappearing.

DayCrumbs keeps the capture step as small as possible:

```bash
daycrumbs add Checked DB records, status differs only for few financial records
```

Record it and continue working. No app to open. No account required. No organizing required.

---

## What it does

DayCrumbs currently focuses on one workflow: **leave small activity crumbs while you work and retrieve them later by date.**

You can:

- Add activities directly from the command line
- Write notes naturally without surrounding quotes
- Optionally group activities using buckets
- Optionally record duration in minutes
- View today's activities
- View activities from a specific date
- Keep everything stored locally in human-readable JSONL files

---

## Installation

```bash
pip install daycrumbs
```

---

## Usage

### Add an activity

```bash
daycrumbs add Investigated batch processing issue
```

You do not need quotes around the note. Everything after `add` is treated as the activity note.

### Add a bucket

```bash
daycrumbs add Investigated batch processing issue --bucket work
```

Buckets are optional labels to loosely categorize activities.

### Add duration

```bash
daycrumbs add Investigated batch processing issue --duration 45
```

Duration is in minutes. You can combine bucket and duration:

```bash
daycrumbs add Investigated renewal processing issue --bucket work --duration 45
```

### View today's activities

```bash
daycrumbs view
```

### View activities for a specific date

```bash
daycrumbs view 2026-07-04
```

Dates use the `YYYY-MM-DD` format.

---

## Local-first by design

DayCrumbs stores everything locally on your machine, organized by year and month as JSONL files. The storage location follows your operating system's conventions.

No account to create. No login. No remote service. No proprietary format. The data stays simple, readable, and yours.

---

## Status & roadmap

Version `0.1.0` focuses on one thing: make it easy to leave small breadcrumbs during the day and retrieve them when memory needs a little help.

Over time, those crumbs could support other workflows — preparing status updates, reconstructing timesheets, writing performance reviews, or generating AI-assisted summaries/insights. Those are possible directions, not current features. Future additions will be driven by actual usage, not by the desire to build a large system.

---

## License

MIT