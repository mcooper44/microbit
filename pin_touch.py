from microbit import *

while True:
    if pin0.is_touched():
        display.show(Image.HAPPY)
    if pin1.is_touched():
        display.show(Image.HEART)
    if pin2.is_touched():
        display.show(Image.MEH)
    else:
        display.show(Image.SAD)