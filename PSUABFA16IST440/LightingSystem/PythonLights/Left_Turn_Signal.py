import pygame

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

running = True

x = 0
y = 0
sense.set_pixel(x, y, 255, 255, 255)

while running:
    sense.set_pixel(x, y, 0, 0, 0)  # Black 0,0,0 means OFF
    
    if event.key == K_RIGHT and x < 7:
        sense.set_pixel(7, 4, 255, 255, 255)
        sense.set_pixel(7, 3, 255, 255, 255)
    elif event.key == K_LEFT and x > 0:
        # left turn signal

        sense.set_pixel(x, y, 255, 255, 255)
        if event.type == QUIT:
            running = False
            print("BYE")
