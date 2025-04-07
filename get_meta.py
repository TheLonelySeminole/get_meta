#!/usr/bin/python3
import subprocess
import json


def playerctl(command):
    return subprocess.check_output(
        ["playerctl", "metadata", command], text=True
    ).strip()


try:
    output = playerctl("title") + " by " + playerctl("artist")
except Exception as e:
    output = "Not Connected"

dump = {"text": output, "class": "custom/media"}

print(json.dumps(dump))
