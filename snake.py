import turtle as t

from requests import head

SEGMENT_NUMBER = 1

class Snake:
    def __init__(self):
        self.segment = []
        self.head = t.Turtle("square")
        self.head.color("light green")
        self.head.pu()
        
        
        for i in range(SEGMENT_NUMBER):
            self.segment.append(self.head)
            self.head.setpos(x=-20*i,y=0)



    def fwd(self):
        for seg in range(len(self.segment)-1,0,-1):
            self.segment[seg].setpos(self.segment[seg-1].xcor(),self.segment[seg-1].ycor())
        self.segment[0].forward(20)
    
    def t_up(self):
        # head.direction = 'up'
        angle=self.segment[0].heading()
        if angle!=270 and angle!=90:
            for seg in range(len(self.segment)-1,0,-1):
                self.segment[seg].setpos(self.segment[seg-1].xcor(),self.segment[seg-1].ycor())
            self.segment[0].setheading(90)
    
    def t_down(self):
        angle=self.segment[0].heading()
        if angle!=270 and angle!=90:
            for seg in range(len(self.segment)-1,0,-1):
                self.segment[seg].setpos(self.segment[seg-1].xcor(),self.segment[seg-1].ycor())
            self.segment[0].setheading(-90)
    
    def t_left(self):
        angle=self.segment[0].heading()
        if angle!=0 and angle!=180:
            for seg in range(len(self.segment)-1,0,-1):
                self.segment[seg].setpos(self.segment[seg-1].xcor(),self.segment[seg-1].ycor())
            self.segment[0].setheading(180)
    
    def t_right(self):
        angle=self.segment[0].heading()
        if angle!=0 and angle!=180:
            for seg in range(len(self.segment)-1,0,-1):
                self.segment[seg].setpos(self.segment[seg-1].xcor(),self.segment[seg-1].ycor())
            self.segment[0].setheading(0)

    def add(self):
        self.new_seg = t.Turtle("square")
        self.new_seg.color("white")
        self.new_seg.pu()
        self.new_seg.setpos(x = self.segment[-1].xcor(), y = self.segment[-1].ycor())
        self.segment.append(self.new_seg)
        
    def delete(self):
        self.head.goto(0,0)
        for seg in self.segment[1:]:
            seg.goto(1000,1000)
            self.segment.pop()
