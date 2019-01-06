from microbit import *
import speech

while True:
    if button_a.is_pressed():
        speech.say("Cats rule. Dogs drool", speed=82, pitch=72, throat=110, mouth=105)
        speech.say("Me how", speed = 150)
    if button_b.is_pressed():
        solfa = [
                "#115DOWWWWWW",   # Doh
                "#103REYYYYYY",   # Re
                "#94MIYYYYYY",    # Mi
                "#88FAOAOAOAOR",  # Fa
                "#78SOHWWWWW",    # Soh
                "#70LAOAOAOAOR",  # La
                "#62TIYYYYYY",    # Ti
                "#58DOWWWWWW",    # Doh
                ]
        song = ''.join(solfa)
        speech.sing(song, speed=100)