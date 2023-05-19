#Lucas Ross 27 Nov. 2022

from pynput.keyboard import Controller
import keyboard
import random as r
from time import sleep

inputs = [
    "a",
    "w",
    "d",
    "s"
]

active = "a"
hold = 2 #seconds to hold each input
controller = Controller()
toggle = -1
can_toggle = True
toggle_key = "space"
off_key = "e"


def get_rand_input(): #get another random input
    return inputs[r.randint(0, len(inputs) - 1)]

def press_input(): #press the active input for 1 second
    controller.press(active)
    sleep(hold)
    controller.release(active)

print("---- START PROGRAM ----")

while True:
    if keyboard.is_pressed(toggle_key):
        if can_toggle:
            toggle *= -1
            
            if toggle == 1:
                print("TOGGLE TRUE")
            else:
                print("TOGGLE FALSE")

        can_toggle = False
    else:
        can_toggle = True

    if keyboard.is_pressed(off_key):
        break

    if toggle == 1:
        press_input()
        active = get_rand_input()

print("---- END PROGRAM ----")