from loguru import logger
from pynput import keyboard

from constant import set_brightness, default_brightness, brightness

UPPER = [
    {keyboard.Key.ctrl, keyboard.Key.up},
]
DOWN = [
    {keyboard.Key.ctrl, keyboard.Key.down},
]

COMBINATIONS = [*UPPER, *DOWN]

current = set()


def execute_up():
    brightness.up()
    set_brightness(brightness.cur_brightness)
    print("up", brightness.cur_brightness)


def execute_down():
    brightness.down()
    set_brightness(brightness.cur_brightness)
    print("down", brightness.cur_brightness)


def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in UPPER):
            execute_up()
            return
        if any(all(k in current for k in COMBO) for COMBO in DOWN):
            execute_down()
            return


def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)


if __name__ == '__main__':
    logger.add("log.log")
    with logger.catch(reraise=True):
        set_brightness(default_brightness)
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
