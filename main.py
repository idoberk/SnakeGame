import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

SCREEN_BOUNDARIES = 290
SCREEN_SIZE = [600, 600]

screen = Screen()
screen.setup(width = SCREEN_SIZE[0], height = SCREEN_SIZE[1])
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move_snake()

    # Detect collision with food.
    if snake.head.distance(food) < 10:
        snake.extend()
        food.refresh()
        score_board.increase_score()

    # Detect collision with wall.
    if (snake.head.xcor() > SCREEN_BOUNDARIES or snake.head.xcor() < (SCREEN_BOUNDARIES * -1) or
            snake.head.ycor() > SCREEN_BOUNDARIES or snake.head.ycor() < SCREEN_BOUNDARIES * -1):
        game_is_on = False
        score_board.game_over()


    # Detect collision with tail.
    for block in snake.snake_list[1:]:
        if snake.head.distance(block) < 5:
            game_is_on = False
            score_board.game_over()


screen.exitonclick()
