import time, subprocess, sys

import easygui
from pynput.keyboard import Key, Controller
from easygui import *

MOVE_DElAY = 0.5
MOVE_FAST_DELAY = 0.1
ENTER_GARAGE_DELAY = 1
ENTER_BUY_DELAY = 0.5
ENTER_MENU_DELAY = 0.2
ESC_DELAY = 1

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

keyboard = Controller()
keys = {
    Key.enter: "enter",
    Key.esc: "esc",
    Key.left: "left",
    Key.right: "right",
    Key.up: "up",
    Key.down: "down",
    Key.cmd_l: "cmd_l"
        }
def pressKey(key, delay):
    forza()
    keyboard.press(key)
    print(keys[key])
    keyboard.release(key)
    time.sleep(delay)

def forza():
    if process_exists('ForzaHorizon5.exe'):
        return 1
    else:
        sys.exit("eroare")

def start_forza():
    pressKey(Key.cmd_l, 1)
    keyboard.press('f')
    keyboard.release('f')
    time.sleep(1)
    pressKey(Key.enter,20)
    time.sleep(20)

    # windowed mode
    print("exit fullscreen")
    keyboard.press(Key.alt_l)
    time.sleep(0.1)
    keyboard.press(Key.enter)
    time.sleep(0.3)
    keyboard.release(Key.enter)
    time.sleep(0.1)
    keyboard.release(Key.alt_l)
    #

    print("wait 30")
    time.sleep(30)

    # making sure it hits continue
    pressKey(Key.enter, 1)
    pressKey(Key.enter, 1)
    pressKey(Key.enter, 1)

    print("wait 20")
    time.sleep(20)

    pressKey(Key.esc, 1)

def start_willy():
    nr_cars = input("How many cars do you have?")

    print("waits 5")
    time.sleep(5)

    willy(int(nr_cars))

def willy(car_nr):
    x = int(car_nr / 2) + 1
    print(f"Willy nr: {car_nr + 1}")
    # Enter car menu
    pressKey(Key.enter, ENTER_GARAGE_DELAY)
    # Go to the car
    while x > 0:
        pressKey(Key.left, MOVE_FAST_DELAY)
        x -= 1
    # Select the car and w8 to load
    pressKey(Key.enter, ENTER_BUY_DELAY)
    pressKey(Key.enter, 7)
    # Go to 'Tune Car'
    pressKey(Key.esc, ESC_DELAY)
    pressKey(Key.left, MOVE_FAST_DELAY)
    pressKey(Key.enter, ENTER_BUY_DELAY)
    # Go to 'Car mastery'
    pressKey(Key.right, MOVE_FAST_DELAY)
    pressKey(Key.right, MOVE_FAST_DELAY)
    pressKey(Key.down, MOVE_DElAY)
    pressKey(Key.enter, ENTER_BUY_DELAY)
    # Choose perks
    pressKey(Key.enter, ENTER_BUY_DELAY)
    pressKey(Key.right, MOVE_DElAY)
    pressKey(Key.enter, ENTER_BUY_DELAY)
    pressKey(Key.up, MOVE_DElAY)
    pressKey(Key.enter, ENTER_BUY_DELAY)
    # Go to starting point
    pressKey(Key.esc, ESC_DELAY)
    pressKey(Key.esc, ESC_DELAY)
    pressKey(Key.right, MOVE_FAST_DELAY)

def STOP_EVERYTHING():
    stop = indexbox(msg="Do you want to stop the script?",choices=["YES"])
    if stop == 0:
        sys.exit("Ceva s o dus pe pula!")

def buy_cars():
    nr_cars = integerbox("How many cars do you want to buy?")
    print("number of cars:" + str(nr_cars))

    print("waits 5")
    time.sleep(5)

    pressKey(Key.right, MOVE_DElAY)
    pressKey(Key.enter, ENTER_GARAGE_DELAY)

    for i in range(0, nr_cars):
        keyboard.press("y")
        keyboard.release("y")
        time.sleep(0.5)
        pressKey(Key.enter,ENTER_BUY_DELAY)

    pressKey(Key.esc, ESC_DELAY)
    pressKey(Key.left, MOVE_DElAY)

    easygui.textbox("Finished buying " + str(nr_cars) + " cars")

def sell_cars():
    nr_cars = integerbox("How many cars do you want to buy?")
    print("number of cars:" + str(nr_cars))
    sell(nr_cars)

def sell(nr_cars):
    print("waits 5")
    time.sleep(5)

    pressKey(Key.enter, ENTER_GARAGE_DELAY)
    pressKey(Key.left, MOVE_FAST_DELAY)
    pressKey(Key.down, MOVE_FAST_DELAY)

    for j in range(0,nr_cars):
        pressKey(Key.enter, ENTER_MENU_DELAY)
        for i in range(0, 4):
            pressKey(Key.down, MOVE_FAST_DELAY)
        pressKey(Key.enter, ENTER_BUY_DELAY)
        pressKey(Key.enter, ENTER_BUY_DELAY)

    pressKey(Key.esc, ESC_DELAY)

    easygui.textbox("Finished selling " + str(nr_cars) + " cars")

def interface():
    x = easygui.indexbox(msg="What do you want to do?",choices=["Launch Forza","Buy cars","Sell cars","Get SWS","Exit"],default_choice="Exit")
    if x == 0:
        start_forza()
        interface()
    elif x == 1:
        buy_cars()
    elif x == 2:
        sell_cars()
    elif x == 3:
        start_willy()
    elif x == 4:
        sys.exit("Exit")

interface()
