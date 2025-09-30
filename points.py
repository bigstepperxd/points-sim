#!/usr/bin/env python3
from datetime import datetime
import json
from pathlib import Path

DATA = Path("actions.json")

DEFAULT = {
  "weights": {"trade": 1.0, "deposit": 0.5, "stake": 2.0},
  "actions": [
    {"type": "trade", "amount": 100, "note": "XPL/USDT"},
    {"type": "deposit", "amount": 3000, "note": "USDAI farm"},
    {"type": "stake", "amount": 500, "note": "YT-Token demo"}
  ]
}

def load():
    if not DATA.exists():
        DATA.write_text(json.dumps(DEFAULT, indent=2))
    return json.loads(DATA.read_text())

def calc(data):
    total = 0.0
    for a in data["actions"]:
        w = data["weights"].get(a["type"], 0.0)
        total += w * float(a["amount"])
    return total

if __name__ == "__main__":
    data = load()
    pts = calc(data)
    now = datetime.utcnow().isoformat() + "Z"
    print(f"points-sim report — {now}")
    print(f"points_today: {pts}")
