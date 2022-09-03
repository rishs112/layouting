import json

with open("layout.json") as f:
    layout = json.load(f)

print(layout)