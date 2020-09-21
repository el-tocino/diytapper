#!/usr/bin/python3

import sys
import time
from gpiozero import Button
from gpiozero import LED

runid = time.time()
gamelen = 30

### GPIO id's aren't the board pin ID
### wire buttons to 3.3v pins (board pin 1/17)
### wire LED's to 5v pins (board pins 2/4)
button1 = Button(5)
LED1 = LED(18)
button2 = Button(6)
LED2 = LED(23)
button3 = Button13)
LED3 = LED(24)
button4 = Button(19)
LED4 = LED(25)
button5 = Button(26)
LED5 = LED(12)



def countdown():
    """ Flash the lights in count down.
        3: 12345
        2:  234
        1:   3
        wait a random amount of time (0.2-2 seconds)
    """
    staticdelay = 0.2
    randomdelay = random.random() + random.random()
    delay = staticdelay + randomdelay
    time.sleep(delay)


def logging(buttonid,tsid):
    """ save to log. """
    print(buttonid, tsid, file=logfile)


def randombutton():
    """ get a random button between 0 and 4"""
    buttonid = randint(1,5)
    return(buttonid)


def buttonon(bid):
    """ turn on button's LED """
    

def buttonoff(bid):
    """ turn off button's LED """
    

def getbuttonpress(bid):
    """ Check if button has been pressed yet. If so turn off LED """


def playgame(starttime):
    """ run the game. """
    endtime = starttime + 30.05
    logging("starting",starttime)
    while time.time() < endtime:
        button = randombutton
        buttonon(button)
        getbuttonpress(button)
        logging(button, time.time())
    logging("ending",time.time())
      

def main():
    countdown
    starttime = time.time()
    logname = str(int(starttime)) + ".log"
    logfile = open(logname, "w")
    playgame(starttime)
    close(logfile)

