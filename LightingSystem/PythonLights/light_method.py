from sense_hat import SenseHat
import time
s = SenseHat()
s.low_light = True
nothing = (0,0,0)
red = (255, 0, 0)
def hazrdLight():
    R = red
    O = nothing
    logo = [
    O, O, O, R, R, O, O, O,
    O, O, R, R, R, R, O, O,
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def r_signal():
    W = red
    O = nothing

    logo = [
    O, O, O, W, W, O, O, O,
    O, O, O, O, W, W, O, O,
    O, O, O, O, O, W, W, O,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    O, O, O, O, O, W, W, O,
    O, O, O, O, W, W, O, O,
    O, O, O, W, W, O, O, O,
    ]
    return logo

def l_signal():
    W = red
    O = nothing
    logo = [
    O, O, O, W, W, O, O, O,
    O, O, W, W, O, O, O, O,
    O, W, W, O, O, O, O, O,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    O, W, W, O, O, O, O, O,
    O, O, W, W, O, O, O, O,
    O, O, O, W, W, O, O, O,
    ]
    return logo

images = [hazrdLight,r_signal,l_signal]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.9)
    s.clear()
    time.sleep(.9)
    count += 1
