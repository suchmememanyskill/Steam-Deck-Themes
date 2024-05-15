#!/bin/python3
### CONFIG

# Enabled random images
RANDOMISE = ["Home"]
# Available options: "Home", "Library", "Search", "Friends"

###

if len(RANDOMISE) <= 0:
    exit(0)

import os, json, random, subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
dir_name = os.path.basename(dir_path)

with open("config_USER.json", "r") as f:
    config = json.load(f)

for x in RANDOMISE:
    current_image = os.path.basename(config[x]["components"][f"{x} Background"])
    images = [f for f in os.listdir(x) if os.path.isfile(os.path.join(x, f)) if not f == current_image]
    if len(images) > 0:
        config[x]["components"][f"{x} Background"] = dir_name + "/" + x + "/" + random.choice(images)

with open("config_USER.json", "w") as f:
    json.dump(config, f)

subprocess.run(["curl", "-X", "POST", "--data", "{\"method\": \"reset\",\"args\": {}}", "-H", "Content-Type: application/json", "http://127.0.0.1:35821/req"])