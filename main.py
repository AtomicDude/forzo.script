import time, subprocess, sys

import easygui
from pynput.keyboard import Key, Controller
from easygui import *

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
    pressKey(Key.enter, 0.75)
    # Go to the car
    while x > 0:
        pressKey(Key.left, 0.2)
        x -= 1
    # Select the car and w8 to load
    pressKey(Key.enter, 0.75)
    pressKey(Key.enter, 7)
    # Go to 'Tune Car'
    pressKey(Key.esc, 1)
    pressKey(Key.left, 0.1)
    pressKey(Key.enter, 0.75)
    # Go to 'Car mastery'
    pressKey(Key.right, 0.1)
    pressKey(Key.right, 0.1)
    pressKey(Key.down, 0.5)
    pressKey(Key.enter, 0.6)
    # Choose perks
    pressKey(Key.enter, 0.5)
    pressKey(Key.right, 0.5)
    pressKey(Key.enter, 0.6)
    pressKey(Key.up, 0.5)
    pressKey(Key.enter, 0.6)
    # Go to starting point
    pressKey(Key.esc, 0.75)
    pressKey(Key.esc, 1)
    pressKey(Key.right, 0.75)

def STOP_EVERYTHING():
    stop = indexbox(msg="Do you want to stop the script?",choices=["YES"])
    if stop == 0:
        sys.exit("Ceva s o dus pe pula!")

def buy_cars():
    nr_cars = integerbox("How many cars do you want to buy?")
    print("number of cars:" + str(nr_cars))

    print("waits 5")
    time.sleep(5)

    pressKey(Key.right, 0.5)
    pressKey(Key.enter, 1)

    for i in range(0, nr_cars):
        keyboard.press("y")
        keyboard.release("y")
        time.sleep(0.5)
        pressKey(Key.enter,0.5)

    pressKey(Key.esc, 1)
    pressKey(Key.left, 1)

    easygui.textbox("Finished buying " + str(nr_cars) + " cars")

def sell_cars():
    nr_cars = integerbox("How many cars do you want to buy?")
    print("number of cars:" + str(nr_cars))
    sell(nr_cars)

def sell(nr_cars):
    print("waits 5")
    time.sleep(5)

    pressKey(Key.enter, 0.6)
    pressKey(Key.left, 0.1)
    pressKey(Key.down, 0.1)

    for j in range(0,nr_cars):
        pressKey(Key.enter, 0.2)
        for i in range(0, 4):
            pressKey(Key.down, 0.1)
        pressKey(Key.enter, 0.5)
        pressKey(Key.enter, 0.5)

    pressKey(Key.esc, 1)

    easygui.textbox("Finished selling " + str(nr_cars) + " cars")

def test_stop():
    STOP_EVERYTHING()
    while 1:
        print("pula")

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
        #start_willy()
        print(x)
    elif x == 4:
        sys.exit("Exit")

interface()
