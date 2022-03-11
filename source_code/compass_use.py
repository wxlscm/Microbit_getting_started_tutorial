from microbit import *
compass.calibrate()
while True:
    bearing = compass.heading()
    if bearing < 30 or bearing > 330:
        display.show('N')
    else:
        display.show(' ')
