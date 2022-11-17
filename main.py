import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
#####
# import random
# import math
####

GAME_RESX = 600
GAME_RESY = 600

screen = t.Screen()
###########
screen.cv._rootwindow.resizable(False,False)
###########
screen.setup(width=GAME_RESX, height=GAME_RESY)
screen.bgcolor('#004c99')
screen.tracer(0)

snake = Snake()
food = Food(GAME_RESX, GAME_RESY)
scoreboard = Scoreboard(GAME_RESY)

###
##try :
##    with open('highscore.dat','rb') as f :
##        high_score = pickle.load(f)
##except:
##    with open('highscore.dat','wb') as f :
##        pickle.dump(high_score,f)
####



screen.listen()

def game():
    GAME_SPEED = 0.1
    game_on = True
    score = 0

    while game_on:
        screen.update()
        time.sleep(GAME_SPEED)
        ## Movement
        snake.fwd()
        screen.onkeypress(snake.t_left, "a")
        screen.onkeypress(snake.t_right, "d")
        screen.onkeypress(snake.t_up, "w")
        screen.onkeypress(snake.t_down, "s")
    #########################################
        screen.onkeypress(snake.t_left, "A")
        screen.onkeypress(snake.t_right, "D")
        screen.onkeypress(snake.t_up, "W")
        screen.onkeypress(snake.t_down, "S")
    #########################################
        
        current_x = snake.head.xcor()
        current_y = snake.head.ycor()
        ## food detection
        # if math.dist((current_x,current_y),food.position())<10:
        if snake.head.distance(food) < 10 :

            food.move()
            game_on = True
            GAME_SPEED -= 0.0025
            ####
            # if score > high_score :
            #     high_score = score
            ####
            scoreboard.update()
            snake.add()

            print(f"Your score is: {scoreboard.score}")
            ###
            # print(high_score)
            ###
        ## collision with wall
        if current_x > (GAME_RESX/2 - 10) or current_x<-(GAME_RESX/2 - 20) or current_y>(GAME_RESY/2 - 10) or current_y<-(GAME_RESX/2 - 20):
            game_on = False
            time.sleep(0.4)
            scoreboard.over()
        ## collision with tail
        for seg in range(len(snake.segment)-1,1,-1):
            # if math.dist((current_x,current_y),snake.segment[seg].position())<10:
            if snake.head.distance(snake.segment[seg].position()) < 10 :
                time.sleep(0.4)
                game_on = False
                # with open('highscore.dat','wb') as f:
                #     pickle.dump(high_score,f)
                scoreboard.over()
    
    if game_on == False :
        screen.onkey(game, "space")
        snake.delete()
        scoreboard.restart(GAME_RESY)


    
    # screen.exitonclick()
    screen.mainloop()
game()
