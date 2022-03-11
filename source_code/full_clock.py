from microbit import *
hour = 0
minute = 0
second = 0
clock_start = 0
clock_current = 0
clock_now_second = 0
def caculate_HMS(now_second_p):
    global second, minute, hour
    second += now_second_p
    while second > 59:
        second -= 60
        minute += 1
    while minute > 59:
        minute -= 60
        hour += 1
    while hour > 23:
        hour -= 24

def print_HMS(hms):
    display.clear()
    tens = hms // 10
    ones = hms % 10
    if tens <= 5:
        for i in range(tens):
            display.set_pixel(i, 0, 6)
    else:
        for i in range(5):
            display.set_pixel(i, 0, 6)
        for i in range(tens - 5):
            display.set_pixel(i, 1, 6)
    if ones <= 5:
        for i in range(ones):
            display.set_pixel(i, 2, 6)
    else:
        for i in range(5):
            display.set_pixel(i, 2, 6)
        for i in range(ones - 5):
            display.set_pixel(i, 3, 6)

display.scroll("Set Hour")
display.clear()
while True:
    if button_a.was_pressed():
        hour += 1
        if hour > 23:
            hour = 0
        print_HMS(hour)
    elif button_b.was_pressed():
        display.scroll("Set Hour={}!".format(hour))
        break

display.scroll("Set Min")
display.clear()
while True:
    if button_a.was_pressed():
        minute += 1
        if minute > 59:
            minute = 0
        print_HMS(minute)
    elif button_b.was_pressed():
        display.scroll("Set Min={}!".format(minute))
        break

display.scroll("Set Sec")
display.clear()
while True:
    if button_a.was_pressed():
        second += 1
        if second > 59:
            second = 0
        print_HMS(second)
    elif button_b.was_pressed():
        display.scroll("Set Sec={}!".format(second))
        break

clock_start = running_time()
while True:
    if button_b.was_pressed():
        clock_current = running_time()
        clock_now_second = (clock_current - clock_start) // 1000
        caculate_HMS(clock_now_second)
        clock_start = clock_current
        display.scroll("{}:{}:{}".format(hour, minute, second))
