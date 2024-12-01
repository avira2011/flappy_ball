import pgzrun 
import random 

TITLE = 'Flappy ball By: Avira'
WIDTH = 800 
HEIGHT = 600
gravity = 2000
#pixels per second

class Ball():
    def __init__(self,intial_x, intial_y):
        self.x = intial_x
        self.y = intial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40
    
    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos,self.radius,'white')

ball1 = Ball(400,300)
def draw():
    screen.clear()
    ball1.draw()

def update(dt):

    uy = ball1.vy
    ball1.vy += gravity*dt
    ball1.y += (uy+ball1.vy)*0.5*dt
    
    if ball1.y > HEIGHT - ball1.radius:
        ball1.y = HEIGHT - ball1.radius
        ball1.vy = - ball1.vy * 0.9
    
    ball1.x += ball1.vx * dt
    if ball1.x > WIDTH - ball1.radius or ball1.x < ball1.radius:
        ball1.vx = - ball1.vx

def on_key_down(key):
    
    if key == keys.SPACE:
        ball1.vy = - 300


pgzrun.go()