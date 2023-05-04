from manim import *

class Test(Scene):
    def construct(self):
        rad = 0.5
        c1 = Circle(rad)
        self.add(c1)
        self.play(Flash(c1, flash_radius=rad))