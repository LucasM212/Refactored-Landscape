def setup():
    size(640, 480)
    
def draw():
  background(139, 90, 0)
  draw_sun(320, -100)
  cloud1(-100, height)
  cloud2(640, 240)

def draw_sun(x, height2):
  if height2 >= 640:
     height2 = -100
  height2 += 1
  noStroke()
  fill(255,255,0)
  ellipse(x, height2, 100, 100)

def cloud1(x2, height):
  if x2 >= 800:
        x2 = -100
  x2 += 1
  fill(255, 255, 255)
  ellipse(x2, height/2, 50, 50)
  ellipse(x2+30, height/2, 50, 50)
  ellipse(x2+10, height/2-20, 50, 50)

def cloud2(x3, height3):
  if x3 <= -100:
      x3 = 640
  x3 -= 1
  fill(255, 255, 255)
  ellipse(x3, height3, 50, 50)
  ellipse(x3+30, height3, 50, 50)
  ellipse(x3+10, height3-20, 50, 50)
