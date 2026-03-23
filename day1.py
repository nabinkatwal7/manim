from manim import *

class Day1(Scene):
  def construct(self):
    title = Text("Test Text", font_size=60)
    title.set_color(BLUE)
    subtitle = Text("Subtitle Text", font_size=30)

    subtitle.next_to(title, DOWN)

    self.play(Write(title))
    self.play(Write(subtitle))
    self.wait(1)

    self.play(title.animate.shift(UP))
    self.play(subtitle.animate.shift(UP))
    self.play(title.animate.scale(1.2))
    self.play(subtitle.animate.scale(1.2))
    self.play(title.animate.shift(DOWN))
    self.play(subtitle.animate.shift(DOWN))
    self.wait(1)