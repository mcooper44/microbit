from microbit import *

cat = Image("90009:"
            "99099:"
            "00000:"
            "09090:"
            "00900")

moon = Image("00000:"
             "09990:"
             "09990:"
             "09990:"
             "00000")

while True:
    if button_a.is_pressed():
        display.show(cat)
    elif button_b.is_pressed():
        display.show(moon)
    else:
        display.show(Image.HAPPY)

display.clear()