import json
import os
import subprocess

default_brightness = 0.5
default_increment = 0.02


class Brightness:

    def __init__(self) -> None:
        self.cur_brightness = default_brightness
        self.increment = default_increment

    def up(self, increment=default_increment):
        self.cur_brightness = min(self.cur_brightness + increment, 1.0)

    def down(self, increment=default_increment):
        self.cur_brightness = max(self.cur_brightness - increment, 0.2)


brightness = Brightness()

# cur_devices = subprocess.check_output('xrandr | grep " connected" | cut -f1 -d " "', shell=True).strip().split(b"\n")
# cur_devices = [x.decode("utf-8") for x in cur_devices]
# laptop_device = [x for x in cur_devices if "DP" in x][0]
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
