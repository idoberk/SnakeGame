from turtle import Turtle

STARTING_POS = [(0, 0), (-10, 0), (-20, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 10

class Snake:
    def __init__(self):
        """Snake class constructor."""
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]
        self.tail = self.snake_list[-1]
        self.last_direction = self.head.heading()

    def create_snake(self):
        """Initialize a snake sized 3 blocks."""
        for pos in STARTING_POS:
            self.add_block(pos)

    def add_block(self, position):
        """Adds a new block to the tail of the snake."""
        snake_block = Turtle(shape = "square")
        snake_block.turtlesize(0.5, 0.5)
        snake_block.color("white")
        snake_block.speed("fastest")
        snake_block.penup()
        snake_block.goto(position)
        self.snake_list.append(snake_block)

    def extend(self):
        """Extends the size of the snake once it consumed food."""
        self.add_block(self.tail.position())

    def move_snake(self):
        """Moves the snake forward."""
        for block in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[block - 1].xcor()
            new_y = self.snake_list[block - 1].ycor()
            self.snake_list[block].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        self.last_direction = self.head.heading()

    def reset_snake(self):
        """Deletes the previous snake, and create a new one in the center of the screen."""
        for block in self.snake_list:
            block.goto(1000, 1000)
        self.snake_list.clear()
        self.create_snake()
        self.head = self.snake_list[0]
        self.tail = self.snake_list[-1]
        self.last_direction = self.head.heading()

    def up(self):
        """Makes the snake to go up."""
        if self.head.heading() != DOWN and self.last_direction != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Makes the snake to go down."""
        if self.head.heading() != UP and self.last_direction != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Makes the snake to go left."""
        if self.head.heading() != RIGHT and self.last_direction != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Makes the snake to go right."""
        if self.head.heading() != LEFT and self.last_direction != LEFT:
            self.head.setheading(RIGHT)