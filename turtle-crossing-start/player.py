import turtle as t
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t.Turtle):
    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto_start()

    def movee(self):
        self.forward(MOVE_DISTANCE)

    def goto_start(self):
        self.goto(STARTING_POSITION)
    def is_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False