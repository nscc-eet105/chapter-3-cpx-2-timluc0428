from adafruit_circuitplayground import cp 
import time

#use 2 for loops to control the neopixel LEDs to go back and forth between
#the first and last pixels
BLACK = (0, 0, 0)
delay_on = .3
delay_off = .1
forward_color = (0, 100, 0)
reverse_color = (100, 0, 0)


while True:
    for i in range(0, 10):
        cp.pixels[i] = (forward_color)
        time.sleep(delay_on)
        cp.pixels[i] = (BLACK)
        time.sleep(delay_off)
    
    for i in range(9, -1, -1):
        cp.pixels[i] = (reverse_color)
        time.sleep(delay_on)
        cp.pixels[i] = (0, 0, 0)
        time.sleep(delay_off)