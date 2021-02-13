import json

with open("VERSION.json", "r", encoding="utf-8") as f:
    DATA = json.loads(f.read())

DATA["revision"] += 1
if DATA["revision"] > 9:
    DATA["minor"] += 1
    DATA["revision"] = 0
if DATA["minor"] > 0:
    DATA["major"] += 1
    DATA["minor"] = 0
    DATA["revision"] = 0

with open("VERSION.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(DATA))

with open("VERSION.py", "w", encoding="utf-8") as f:
    f.write(f"VERSION = 'v{DATA['major']}.{DATA['minor']}.{DATA['revision']}'\n")
