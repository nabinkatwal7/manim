from manim import *

class D4_1(Scene):
  def construct(self):
    text = Text("Smooth Animation")

    self.play(Write(text), run_time=0.5)
    self.wait()

    self.play(text.animate.shift(RIGHT * 3), run_time=3)
    self.wait()

class D4_2(Scene):
  def construct(self):
    circle = Circle(color=BLUE)

    self.play(Create(circle))

    self.play(circle.animate.shift(RIGHT * 4), rate_func=rush_into)
    self.wait()

    self.play(circle.animate.shift(LEFT * 4), rate_func=rush_from)
    self.wait()

class D4_3(Scene):
  def construct(self):
    words = VGroup(Text("Alchi"), Text("lagyo"), Text("Ram"), Text("Sir"))
    words.arrange(RIGHT, buff=0.5)

    self.play(
      AnimationGroup(
        *[Write(word) for word in words],
        lag_ratio=0.3
      )
    )
    self.wait()

class D4_4(Scene):
  def construct(self):
    c = Circle()
    s = Square().shift(RIGHT * 3)

    self.play(Create(c), Create(s))

    self.play(
      AnimationGroup(
        c.animate.shift(RIGHT * 3),
        s.animate.shift(UP * 2),
        lag_ratio=0.2
      ),
      run_time=2
    )
    self.wait()