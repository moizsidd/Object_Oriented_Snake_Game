from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()

screen.setup(600,600)

screen.bgcolor("black")

screen.title("mysnakegame")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:

        food.food_move()
        score.write_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        score.game_over()

    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_on = False
            score.game_over()








screen.exitonclick()