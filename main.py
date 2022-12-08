#modules
import time
import random
from machine import Pin
#assign led
red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)
button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)
button2 = Pin(8, Pin.IN, Pin.PULL_DOWN)
button3 = Pin(3, Pin.IN, Pin.PULL_DOWN)

#sub-routines
def wave():
    for x in range(1,10):
        red.value(1)
        time.sleep(0.5)
        red.value(0)
        amber.value(1)
        time.sleep(0.5)
        amber.value(0)
        green.value(1)
        time.sleep(0.5)
        green.value(0)
        
def ran_blink(ran_num):
    for x in range(1,10):
        random_num = random.randint(1,3)
        if random_num == 1:
            red.value(1)
            time.sleep(0.5)
            red.value(0)
        elif random_num == 2:
            amber.value(1)
            time.sleep(0.5)
            amber.value(0)
        else:
            green.value(1)
            time.sleep(0.5)
            green.value(0)
        
def button1_prg(button1_end):
    while True:
        time.sleep(0.2)
        if button1.value() == 1:
            print("Wave selected")
            wave()
        elif button2.value() == 1:
            print("Random blink selected")
            ran_blink(ran_num)
        elif button3.value() == 1:
            print("Back")
            red.value(0)
            green.value(0)
            amber.value(0)
            button1_end = True
            return button1_end
        else:
            continue

def button2_prg(button2_end):
    while True:
        time.sleep(0.2)
        if button1.value() == 1:
            print("Red selected")
            red.toggle()
        elif button2.value() == 1:
            print("Green selected")
            green.toggle()
        elif button3.value() == 1:
            print("Back")
            red.value(0)
            green.value(0)
            button2_end = True
            return button2_end
        else:
            continue

#constants
ran_num = random.randint(1,3)
button1_end = False
button2_end = False
red.value(0)
amber.value(0)
green.value(0)

#main
while True:
    time.sleep(0.2)
    if button1.value() == 1 and button1_end != True:
        red.value(1)
        print("RGB mode")
        time.sleep(0.3)
        red.value(0)
        button1_prg(button1_end)
        button1_end = False
    elif button2.value() == 1 and button2_end != True:
        print("Static mode")
        red.value(1)
        time.sleep(0.3)
        red.value(0)
        button2_prg(button2_end)
        button2_end = False
    elif button3.value() == 1:
        red.value(1)
        time.sleep(0.3)
        red.value(0)
        print("End of program.")
        end = True
    else:
        continue
