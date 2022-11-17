from turtle import Turtle
# import pickle

class Scoreboard(Turtle):
    def __init__(self,Y):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.pu()
        self.setpos(0-70,Y/2.2)
        self.ht()
        self.write("Score: 0",align="center",font=("arial",18,"bold"))
        #########
        
    # def high_score(self,Y):
    #    try:
    #        with open('highscore.dat','rb') as f :
    #            self.high_score = pickle.load(f)

    #    except :
    #        with open('highscore.dat','wb') as f :
    #            pickle.dump(self.high_score,f)

    #    self.high_score = 0
    #    self.color("white")
    #    self.pu
    #    self.setpos(0+100,Y/2.2)
    #    self.ht()
    #    self.write("High Score: 0",align="center",font=("arial",18,"bold"))

    def update(self):
        self.clear()
        self.score += 10
        ###
##        if self.score > self.high_score :
##            self.high_score = self.score
        ###
        score_text= f"Score: {self.score}"
        self.write(score_text,align="center",font=("arial",18,"bold"))

    
    def over(self):
        self.home()
        self.write("GAME OVER!",align="center",font=("arial",30,"bold"))
        ####
        self.setpos(0,0-25)
        self.ht()
        self.write("Press Space to Restart",align="center",font=("courier",15))
            

    def restart(self,Y):
        # self.clear()
        self.score = 0
        self.setpos(0-70,Y/2.2)
        self.ht()
        score_text= f"Score: {self.score}"
        self.write(score_text,align="center",font=("arial",18,"bold"))
