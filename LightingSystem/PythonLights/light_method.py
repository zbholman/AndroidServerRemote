#Jigar, Haoyang
from sense_hat import SenseHat
import time
s = SenseHat()
nothing = (0,0,0) # add color codes (0,0,0) to show light-off
red = (255, 0, 0) 
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
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

def airbag_symbol():
    R = red
    W = white
    Y = yellow
    O = nothing
    logo = [
    O, R, R, O, O, Y, Y, O,
    R, R, R, R, O, Y, Y, W,
    R, R, R, R, O, R, W, O,
    O, R, R, O, O, R, R, O,
    O, O, O, O, W, R, R, O,
    O, O, R, R, R, W, O, O,
    O, R, R, R, O, O, W, O,
    R, R, O, O, O, O, O, W,    
    ]
    return logo

images = [hazrdLight, r_signal, l_signal, running_light, airbag_symbol] #organized all lights
count = 0
while True: #display the images by sequence of the images when true
    s.set_pixels(images[count % len(images)]())
    time.sleep(.8)
    s.clear()
    time.sleep(.8)
    count += 1
