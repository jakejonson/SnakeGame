import turtle as t
import random

class Food(t.Turtle):
    def __init__(self, GAME_RESX, GAME_RESY):
        super().__init__()
        self.max_x=GAME_RESX
        self.max_y=GAME_RESY
        self.shape("circle")
        self.shapesize(0.8)
        self.pu()
        self.speed("fastest")
        self.color("coral")
        self.xpos=random.randint(int((-GAME_RESX/2+20)/20),int((GAME_RESX/2-20)/20))*20
        self.ypos=random.randint(int((-GAME_RESY/2+20)/20),int((GAME_RESY/2-20)/20))*20
        self.setpos(self.xpos,self.ypos)

    def move(self):
        self.xpos=random.randint(int((-self.max_x/2+20)/20),int((self.max_x/2-20)/20))*20
        self.ypos=random.randint(int((-self.max_y/2+20)/20),int((self.max_y/2-20)/20))*20
        self.goto(self.xpos,self.ypos)

