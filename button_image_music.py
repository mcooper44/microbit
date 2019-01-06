from microbit import *
import music # clip to 0 and GND

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

arrow = Image("00000:"
              "00090:"
              "99999:"
              "00090:"
              "00000") 

double_a = Image("00000:"
                 "09090:"
                 "99999:"
                 "09090:"
                 "00000") 
while True:
    switch = True
    
    if button_a.is_pressed():
        display.show(Image.HAPPY)
        music.play(music.POWER_UP)
        while switch:
            if button_a.is_pressed():
                display.show(cat)
                music.play(music.NYAN)
                display.show(arrow)
                switch = False
            if button_b.is_pressed():
                display.show(moon)
                music.play(music.BLUES)
                display.show(arrow)
                switch = False
    if button_b.is_pressed():
        display.clear()
        switch = True