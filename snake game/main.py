from turtle import Screen;
from Snake import snake;
from Food import Food;
from scoreboard import Scoreboard;
import time;

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=snake()
food = Food()
scoreboard = Scoreboard()

# print(snake.segments)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# starting_positions= [(0,0),(-20,0),(-40,0)]
# for position in starting_positions:
#   new_segment=Turtle('square')
#   new_segment.color('white')
#   new_segment.goto(position)
# segement_1= Turtle("square")
# segement_1.color("white")

# segement_2= Turtle("square")
# segement_2.color("white")
# segement_2.goto(-20,0)

# segement_3= Turtle("square")
# segement_3.color("white")
# segement_3.goto(-40,0)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    ## collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_count()        

    if snake.head.xcor()> 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        # game_is_on=False

    for segments in snake.segments:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            # game_is_on=False
            scoreboard.game_over()
            snake.reset()


screen.exitonclick()