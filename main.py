import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

## Initialization
GAME_RESX = 600
GAME_RESY = 600

screen = t.Screen()
screen.cv._rootwindow.resizable(False,False)
screen.setup(width=GAME_RESX, height=GAME_RESY)
screen.bgcolor('#004c99')
screen.tracer(0)

## Configuration
snake = Snake()
food = Food(GAME_RESX, GAME_RESY)
scoreboard = Scoreboard(GAME_RESY)
# scoreboard.high_score()
screen.listen()
screen.update()

## main game function
def game():
    GAME_SPEED = 0.1
    game_on = True
    scoreboard.restart(GAME_RESY)
    ## Main game loop
    while game_on:
        screen.update()
        time.sleep(GAME_SPEED)
        ## Movement
        snake.fwd()
        screen.onkeypress(snake.t_left, "a")
        screen.onkeypress(snake.t_right, "d")
        screen.onkeypress(snake.t_up, "w")
        screen.onkeypress(snake.t_down, "s")
        #####################################
        screen.onkeypress(snake.t_left, "A")
        screen.onkeypress(snake.t_right, "D")
        screen.onkeypress(snake.t_up, "W")
        screen.onkeypress(snake.t_down, "S")
        #####################################
        
        current_x = snake.head.xcor()
        current_y = snake.head.ycor()

        ## food detection
        if snake.head.distance(food) < 10 :
            food.move()
            game_on = True
            GAME_SPEED -= 0.0025
            scoreboard.update()
            snake.add()
            # print("food")

        ## collision with wall
        if current_x > (GAME_RESX/2 - 10) or current_x<-(GAME_RESX/2 - 20) or current_y>(GAME_RESY/2 - 10) or current_y<-(GAME_RESX/2 - 20):
            game_on = False
            time.sleep(0.4)
            # print("wall")

        ## collision with tail
        for seg in range(len(snake.segment)-1,1,-1):
            if snake.head.distance(snake.segment[seg].position()) < 10 :
                time.sleep(0.4)
                game_on = False
                # print("tail")
    
    if game_on == False :
        screen.onkey(game, "space")
        snake.delete()
        if scoreboard.score > scoreboard.hs :
                scoreboard.hs = scoreboard.score
                scoreboard.high_score()

        scoreboard.over()

    screen.mainloop()

## main code
screen.onkeypress(game)
screen.mainloop()

