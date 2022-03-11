from microbit import *
while True:
    if button_a.was_pressed():
        display.scroll(temperature())
