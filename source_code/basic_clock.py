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

clock_start = running_time()
while True:
    if button_b.was_pressed():
        clock_current = running_time()
        clock_now_second = (clock_current - clock_start) // 1000
        caculate_HMS(clock_now_second)
        clock_start = clock_current
        display.scroll("{}:{}:{}".format(hour, minute, second))
