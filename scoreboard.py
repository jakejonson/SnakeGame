from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,Y):
        super().__init__()
        self.score = 0
        self.hs = 0
        self.color("white")
        self.pu()
        self.setpos(0,Y/2.2)
        self.ht()
        self.write(f"Score: 0   High Score: {self.hs}",align="center",font=("arial",18,"bold"))
        try:
           with open('highscore.txt','rt') as f :
               self.hs = int(f.read())
        except :
           with open('highscore.txt','wt') as f :
               f.write(str(self.hs))

        
    def high_score(self):
        self.clear()
        with open('highscore.txt','wt') as f :
               f.write(str(self.hs))

    def update(self):
        self.clear()
        self.score += 10        
        score_text= f"Score: {self.score}   High Score: {self.hs}"
        self.write(score_text,align="center",font=("arial",18,"bold"))

    
    def over(self):
        self.home()
        self.write(f"GAME OVER!\nYour score was: {self.score}",align="center",font=("arial",30,"bold"))
        self.setpos(0,0-25)
        self.ht()
        self.write("\nPress Space to Restart",align="center",font=("courier",15))
            

    def restart(self,Y):
        self.clear()
        self.score = 0
        self.setpos(0-70,Y/2.2)
        self.ht()
        score_text= f"Score: {self.score}   High Score: {self.hs}"
        self.write(score_text,align="center",font=("arial",18,"bold"))
