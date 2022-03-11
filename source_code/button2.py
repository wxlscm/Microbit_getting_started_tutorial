from microbit import *
number=0
display.show(str(number))
while True:
    if button_a.was_pressed():
        number+=1
        display.show(str(number))

