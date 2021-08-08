import json
import os
import subprocess

default_brightness = 0.5
default_increment = 0.02

laptop_device = "DP-4"
print("detected laptop device: {}".format(laptop_device))


def set_brightness(value):
    "make sure this is going to be called once"
    subprocess.call(f"xrandr --output {laptop_device} --brightness {value}", shell=True, executable="/bin/bash")


def set_cur_value(value):
    with open("cur_value", "w") as f:
        json.dump({"cur_value": value}, f)


def get_cur_value():
    with open("cur_value", "r") as f:
        value = json.load(f)["cur_value"]
    return float(value)


if not os.path.exists("cur_value"):
    set_cur_value(default_brightness)
