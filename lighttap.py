#!/usr/bin/python3

import sys
import time
from gpiozero import Button
from gpiozero import LED

runid = time.time()
gamelen = 30

### The GPIO pins aren't the board pins
buttonpins = [5, 6, 13, 19, 26]
ledpins = [18, 23, 24, 25, 12]

def buttonon(bid):
    """ turn on button's LED """
    buttonled = LED(ledpins[bid])
    buttonled.on()


def buttonoff(bid):
    """ turn off button's LED """
    buttonled = LED(ledpin[bid])
    buttonled.off()


def alloff():
    for lid in ledpins:
        buttonoff(lid)


def countdown():
    """ Flash the lights in count down.
        3: 01234
        2:  123
        1:   2
        wait a random amount of time (0.5-2.5seconds)
    """
    buttonon(4)
    buttonon(3)
    buttonon(2)
    buttonon(1)
    buttonon(0)
    time.sleep(.5)
    alloff
    time.sleep(.5)
    buttonon(1)
    buttonon(2)
    buttonon(3)
    time.sleep(.5)
    alloff
    time.sleep(.5)
    buttonon(2)
    alloff
    staticdelay = 0.5
    randomdelay = random.random() + random.random()
    delay = staticdelay + randomdelay
    time.sleep(delay)


def logging(buttonid,tsid):
    """ save to log. """
    print(buttonid, tsid, file=logfile)


def randombutton():
    """ get a random button between 0 and 4"""
    buttonid = randint(0,4)
    return(buttonid)


def getbuttonpress(bid):
    """ Check if button has been pressed yet. If so turn off LED """
    button = Button(buttonpins[bid])
    button.wait_for_press(10)


def playgame(starttime):
    """ run the game. """
    endtime = starttime + gamelen
    logging("starting",starttime)
    lightcount = 0
    while time.time() < endtime:
        button = randombutton
        buttonon(button)
        getbuttonpress(button)
        lightcount += 1
        logging(button, time.time())
    logging("ending",time.time())
    logging("lightcount",lightcount)
      

def main():
    countdown
    starttime = time.time()
    logname = str(int(starttime)) + ".log"
    logfile = open(logname, "w")
    playgame(starttime)
    close(logfile)

