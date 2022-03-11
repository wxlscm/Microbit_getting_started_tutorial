from microbit import *
hour = 0
minute = 0
second = 0
display.scroll("Set Hour")
while True:
    if button_a.was_pressed():
        hour += 1
        if hour > 23:
            hour = 0
    elif button_b.was_pressed():
        display.scroll("Set Hour={}!".format(hour))
        break

display.scroll("Set Min")
while True:
    if button_a.was_pressed():
        minute += 1
        if minute > 59:
            minute = 0
    elif button_b.was_pressed():
        display.scroll("Set Min={}!".format(minute))
        break

display.scroll("Set Sec")
while True:
    if button_a.was_pressed():
        second += 1
        if second > 59:
            second = 0
    elif button_b.was_pressed():
        display.scroll("Set Sec={}!".format(second))
        break
