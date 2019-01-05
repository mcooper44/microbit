from microbit import *
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/io.html
while True:
    pin0.write_digital(1)
    sleep(20)
    pin0.write_digital(0)
    sleep(480)