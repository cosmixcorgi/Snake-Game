from turtle import Turtle
import random
import math

NEON_COLORS = ['#FF073A', '#FF6B35', '#FFE600', '#0FF0FC', '#BC13FE', '#FF44CC']


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self._color_index = 0
        self.shapesize(0.6, 0.6)
        self.color(NEON_COLORS[0])
        self.refresh()

    def refresh(self):
        x = random.randrange(-280, 281, 20)
        y = random.randrange(-280, 281, 20)
        self.goto(x, y)
        self._color_index = random.randint(0, len(NEON_COLORS) - 1)
        self.color(NEON_COLORS[self._color_index])

    def animate(self, frame):
        size = 0.5 + 0.15 * math.sin(frame * 0.25)
        self.shapesize(size, size)
