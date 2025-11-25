from manim import *
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Hello from fp!")


if __name__ == "__main__":
    main()




class create_coord_system(Scene):
    def construct(self):
        graph = Axes(x_range = 8, y_range = 8, x_length=4, y_length=4)  # create coordinate axes
        self.play(Create(graph))  # show the circle on screen

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation