from microbit import *
import speech # clip to 0 + GND

while True:
    if button_a.is_pressed():
        micro_temp = temperature()
        display.scroll(micro_temp)
        speech.say("It is {} degrees".format(micro_temp), 
                                            speed=82, 
                                            pitch=72, 
                                            throat=110, 
                                            mouth=105)
    if button_b.is_pressed():
        display.scroll(running_time())