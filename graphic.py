from turtle import Turtle, Screen, colormode
import random


def leave(my_screen):
    """Exit the screen"""
    my_screen.exitonclick()


class Draw:
    colormode(255)
    # timmy.shape("circle")

    def __init__(self, steps, X, Y, R, C):
        self.steps = steps
        self.X = X
        self.Y = Y
        self.R = R
        self.C = C
        pass

    def square(self, timmy):
        """ For Square"""
        screen = Screen()
        for i in range(4):
            timmy.forward(90)
            timmy.left(90)
        leave(screen)

    def dashedline(self, timmy):
        """For a dashed line"""
        screen = Screen()
        for _ in range(50):
            timmy.pendown()
            timmy.forward(5)
            timmy.penup()
            timmy.forward(5)
        leave(screen)

    # screen = Screen()
    # def screen_exit():
    #     screen.bye()
    # screen.listen()
    # screen.onkey(key='Up', fun=screen_exit)

    def allsahpes(self, timmy):
        screen = Screen()
        color = ['DarkOrchid', 'CornflowerBlue', 'gray', 'brown', 'DeepPink4', 'RosyBrown', 'DarkOrange', 'blue1']
        side = [3, 4, 5, 6, 7, 8, 9, 10]
        for i in side:
            timmy.speed("fastest")
            timmy.color(random.choice(color))
            for value in range(i):
                angle = 360 / i
                timmy.forward(90)
                timmy.right(angle)
        leave(screen)

    def randomwalk(self, timmy):
        screen = Screen()
        # color = ['SlateGray3', 'SlateBlue1', 'SkyBlue', 'snow3']
        directions = [0, 90, 180, 270]
        timmy.speed("fastest")
        # while start:
        while self.steps:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = (r, g, b)
            # timmy.color(random.choice(color))
            timmy.color(color)
            timmy.forward(random.randint(10, 20))
            timmy.setheading(random.choice(directions))
            self.steps -= 1

        leave(screen)

    def spirograph(self, timmy):
        screen = Screen()
        timmy.speed("fastest")
        for _ in range(36):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            color = (r, g, b)
            timmy.color(color)
            timmy.circle(100)
            timmy.left(10)
        leave(screen)

    def hirstpainting(self, timmy):
        screen = Screen()
        color = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
        timmy.speed("fastest")
        timmy.penup()
        timmy.setpos(-self.X, -self.Y)
        a = -self.Y
        for y in range(self.R):
            for _ in range(self.C):
                timmy.pendown()
                timmy.dot(20, random.choice(color))
                timmy.penup()
                timmy.forward(30)

            #other way
            # timmy.left(90)
            # timmy.forward(30)
            # timmy.setx(-180)
            # timmy.setheading(0)
            a = a + 30
            timmy.setpos(-self.X, a)

        leave(screen)


