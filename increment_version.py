import json
import os

with open("VERSION.json", "r", encoding="utf-8") as f:
    DATA = json.loads(f.read())

DATA["revision"] += 1
if DATA["revision"] > 9:
    DATA["minor"] += 1
    DATA["revision"] = 0
if DATA["minor"] > 9:
    DATA["major"] += 1
    DATA["minor"] = 0
    DATA["revision"] = 0

with open("VERSION.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(DATA))

VERSION = f"v{DATA['major']}.{DATA['minor']}.{DATA['revision']}"
with open("VERSION.py", "w", encoding="utf-8") as f:
    f.write(f"VERSION = '{VERSION}'\n")

os.environ["PYPENTAGONALCUBE_VERSION"] = VERSION
print(VERSION)
