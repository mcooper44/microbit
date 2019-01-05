from microbit import *

while True:
    if button_a.is_pressed():
        display.scroll('A PRESSED')
    if button_b.is_pressed():
        display.scroll('B PRESSED')