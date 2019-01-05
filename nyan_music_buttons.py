from microbit import *
import music

cat = Image("90009:"
            "98589:"
            "59595:"
            "05950:"
            "00000")

plus_one = Image("00000:"
                 "09009:"
                 "99909:"
                 "09009:"
                 "00000")
while True:
    if button_a.is_pressed():
        display.scroll('GO!')
        display.show(cat)
        music.play(music.NYAN)
    if button_b.is_pressed():
        display.show(plus_one)
        music.play(music.POWER_UP)