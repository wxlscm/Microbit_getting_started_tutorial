from microbit import *
hour = 0
minute = 0
second = 0
clock_start = 0
clock_current = 0
clock_now_second = 0

clock_start = running_time()
while True:
    if button_b.was_pressed():
        clock_current = running_time()
        clock_now_second = (clock_current - clock_start) // 1000
        display.scroll("{}".format(clock_now_second))

