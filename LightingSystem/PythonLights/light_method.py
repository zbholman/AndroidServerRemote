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

def running_light():
    G = green
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, G, G, O, O,
    G, G, G, O, G, O, G, O,
    O, O, O, O, G, O, O, G,
    G, G, G, O, G, O, O, G,
    O, O, O, O, G, O, O, G,
    G, G, G, O, G, O, G, O,
    O, O, O, O, G, G, O, O,
    ]
    return logo

images = [hazrdLight, r_signal, l_signal, running_light]
count = 0
while True:
    s.set_pixels(images[count % len(images)]())
    time.sleep(.8)
    s.clear()
    time.sleep(.8)
    count += 1
