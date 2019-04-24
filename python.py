from sense_hat import SenseHat
import time

sense = SenseHat()

green = (0,255,0)
blue  = (0,0,255)
red = (255,0,0)
nothing = (0,0,0)

sense.clear()
x = 1
y = 0

while (y<8):
  sense.set_pixel(x,y,blue)
  time.sleep(1)
  sense.set_pixel(x,y,blue)
  time.sleep(1)
  sense.set_pixel(x,y,red)
  if y >= 3:
    sense.set_pixel(x,y-3,nothing)
  y = y+1
  
  
