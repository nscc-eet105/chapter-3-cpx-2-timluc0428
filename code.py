from adafruit_circuitplayground import cp 
import time

#test the slider switch
if cp.switch:
    cp.red = True
else:
    cp.red = False

#test A and B buttons
if cp.button_a:
    cp.play_file("bass_hit_c.wav")

if cp.button_b:
    cp.play_file("elec_hi_snare.wav")

#test capacitive Touch Pads A1 - A6
if cp.touch_A1:
    cp.pixels[0] = (100, 100, 100)
else:
    cp.pixels[0] = (0, 0, 0)

if cp.touch_A2:
    cp.pixels[1] = (100, 100, 100)
else:
    cp.pixels[1] = (0, 0, 0)

if cp.touch_A3:
    cp.pixels[2] = (100, 100, 100)
else:
    cp.pixels[2] = (0, 0, 0)

if cp.touch_A4:
    cp.pixels[3] = (100, 100, 100)
else:
    cp.pixels[3] = (0, 0, 0)

if cp.touch_A5:
    cp.pixels[4] = (100, 100, 100)
else:
    cp.pixels[4] = (0, 0, 0)    

if cp.touch_A6:
    cp.pixels[5] = (100, 100, 100)
else:
    cp.pixels[5] = (0, 0, 0)