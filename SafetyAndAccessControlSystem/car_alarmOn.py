# Contributors: Phuong Lu, Joey Lee, and Matt Handwerk
# Date: 10/4/2016
# Course: IST 440W - Team 6, Professor Oakes
# Purpose: Display car alarm logo on Sense HAT when alarm is turned on

from sense_hat import SenseHat
import time
import pygame

pygame.mixer.init()
pygame.mixer.music.load("setalarm.mp3")
pygame.mixer.music.play()

s = SenseHat()
s.clear()
s.low_light = True

green = (0, 0, 0)
red = (0, 0, 0)
blue = (0, 0, 255)
nothing = (0, 0, 0)

def car_alarm():
  B = blue
  O = nothing
  logo = [
    O, O, O, O, O, O, O, O,
    O, B, B, B, B, B, B, O,
    O, B, B, B, O, O, B, O,
    O, B, B, B, O, O, B, O,
    O, B, B, B, O, O, B, O,
    O, B, B, B, O, O, B, O,
    O, O, B, B, O, B, O, O,
    O, O, O, B, B, O, O, O,
    ]
  return logo
    
images = [car_alarm]
count = 0


s.set_pixels(images[count % len(images)]())
time.sleep(.75)
count += 1
