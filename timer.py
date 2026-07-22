import json
import os
import time
from datetime import datetime

FILE = "sessions.json"
TEMP = ".current_session.json"


def load():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def start_timer(project):
    session = {
        "project": project,
        "start": time.time()
    }

    with open(TEMP, "w") as f:
        json.dump(session, f)

    print("⏳ Timer Started!")


def stop_timer():
    if not os.path.exists(TEMP):
        print("No running timer.")
        return

    with open(TEMP, "r") as f:
        session = json.load(f)

    duration = round((time.time() - session["start"]) / 60, 2)

    data = load()

    data.append({
        "project": session["project"],
        "duration": duration,
        "date": datetime.now().strftime("%Y-%m-%d")
    })

    save(data)

    os.remove(TEMP)

    print(f"✅ Saved {duration} minutes.")


def view_sessions():
    data = load()

    if not data:
        print("No sessions found.")
        return

    for item in data:
        print(f"{item['date']} | {item['project']} | {item['duration']} mins")
