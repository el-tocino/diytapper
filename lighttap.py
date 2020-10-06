""" DIY  whack-a-mole with led buttons aka fitlights.   """
#!/usr/bin/python3

import time
import random
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
    buttonled = LED(ledpins[bid])
    buttonled.off()


def alloff():
    """ Turn off all the LED's """
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
    alloff()
    time.sleep(.5)
    buttonon(1)
    buttonon(2)
    buttonon(3)
    time.sleep(.5)
    alloff()
    time.sleep(.5)
    buttonon(2)
    time.sleep(.5)
    alloff()
    staticdelay = 0.5
    randomdelay = random.random() + random.random()
    delay = staticdelay + randomdelay
    time.sleep(delay)


def logging(buttonid, tsid, logname):
    """ save to log. """
    print(buttonid, tsid, file=open(logname, "a"))


def randombutton():
    """ get a random button between 0 and 4"""
    buttonid = random.randint(0, 4)
    return buttonid


def getbuttonpress(bid):
    """ Check if button has been pressed yet. If so turn off LED """
    button = Button(buttonpins[bid])
    button.wait_for_press(10)
    buttonoff(bid)
    bidtime = time.time()
    return bidtime

def playgame(starttime, logname):
    """ run the game. """
    endtime = starttime + gamelen
    logging("starting", starttime, logname)
    lightcount = 0
    while time.time() < endtime:
        button = randombutton
        buttonon(button)
        tapped = getbuttonpress(button)
        if tapped <= endtime:
            lightcount += 1
        logging(button, time.time(), logname)
    logging("ending", time.time(), logname)
    logging("lightcount", lightcount, logname)

def main():
    """ Do the stuff and things! """
    countdown()
    starttime = time.time()
    logname = str(int(starttime)) + ".log"
    playgame(starttime, logname)
