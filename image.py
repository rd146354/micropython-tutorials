from microbit import *

display.show(Image.CLOCK12)
sleep(5000)

boat = Image("05050:"
             "05050:"
             "05050:"
             "99999:"
             "0999")

display.show(boat)
sleep(1000)

shopping = ["Eggs", "Bacon", "Tomatoes"]
primes = [2, 3, 5, 7, 11, 13, 17, 19]
mixed_up_list = ["hello!", 1.234, Image.HAPPY]

display.show(Image.ALL_CLOCKS, loop=True, delay=100)

