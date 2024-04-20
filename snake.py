from turtle import Turtle

STARTING = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares= []
        self.create_snake()
        self.head  = self.squares[0]

    def create_snake(self):
        for posi in STARTING:
            self.add_segment(posi)

    def add_segment(self, posi):
        new_square = Turtle("square")
        new_square.penup()

        new_square.color("white")
        new_square.goto(posi)
        self.squares.append(new_square)


    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for seg_num in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[seg_num - 1].xcor()
            new_y = self.squares[seg_num - 1].ycor()
            self.squares[seg_num].goto(new_x, new_y)



        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.squares[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.squares[0].setheading(LEFT)





