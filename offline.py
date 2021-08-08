import sys
from pathlib import Path

cur_path = Path(__file__).parent.absolute()
sys.path.insert(0, f"{str(cur_path)}")
from constant import get_cur_value, default_increment, set_cur_value, set_brightness, default_brightness


def up():
    cur_value = get_cur_value()
    cur_value += default_increment
    cur_value = min(1, cur_value)
    set_cur_value(cur_value)
    set_brightness(cur_value)
    print(cur_value)


def default():
    cur_value = default_brightness
    set_cur_value(cur_value)
    set_brightness(cur_value)
    print(cur_value)


def down():
    cur_value = get_cur_value()
    cur_value -= default_increment
    cur_value = max(0.2, cur_value)
    set_cur_value(cur_value)
    set_brightness(cur_value)
    print(cur_value)
