'''
keyestudio analog joystick breakout board
    v -> v
    g -> g
    x -> p0
    y -> p1
    b/sw -> p2
'''

from microbit import *

SEGMENT_SIZE = 1024 / 5  # ADC range / screen range

while True:
    x = pin0.read_analog()
    row = int(x / SEGMENT_SIZE)

    y = pin1.read_analog()
    col = int(y / SEGMENT_SIZE)

    display.set_pixel(col, row, 9)
    sleep(1)  # prevents pixel flicker
    display.set_pixel(col, row, 0)