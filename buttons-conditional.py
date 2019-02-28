# Admittedly this is pretty heavily modified from the example
# provided in the tutorial. I didn't like the way it handled
# simultaneous button presses. There was also the issue of the
# program ending if the timing wasn't perfect.

from microbit import *

while True:
    sleep(100)
    (a, b) = (button_a.was_pressed(), button_b.was_pressed())
    if a and b:
        display.show(Image.SURPRISED)
        sleep(1000)
    elif a:
        display.show(Image.HAPPY)
        sleep(1000)
    elif b:
        display.show(Image.ARROW_W)
        sleep(1000)
    elif pin0.is_touched():
        break
    else:
        display.show(Image.SAD)

display.clear()

