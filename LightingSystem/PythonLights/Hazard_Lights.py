from sense_hat import SenseHat

sense = SenseHat()
yellow = (255, 191, 0)
red = (255, 0, 0)
hazards = True
number_of_blinks = 5

sense.clear()

x = 3
y = 0

sense.set_pixel(x, y, yellow)
sense.set_pixel(4, y, yellow)
y += 1
sense.set_pixel(2, y, yellow)
sense.set_pixel(5, y, yellow)
y += 1
sense.set_pixel(1, y, yellow)
sense.set_pixel(6, y, yellow)
y += 1
sense.set_pixel(0, y, yellow)
sense.set_pixel(7, y, yellow)

x = 0
for x in range(0, 8):
    sense.set_pixel(x, 7, yellow)
    
for y in range (1, 4):
    sense.set_pixel( 3, y, red)
    sense.set_pixel( 4, y, red)
    
sense.set_pixel( 3, 5, red)
sense.set_pixel( 4, 5, red)
