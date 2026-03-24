from manim import *

class CinematicIntro(Scene):
  def construct(self):
    title = Text("Coffee Time Reminder", font_size=60)
    subtitle = Text("Dada Coffee Khana Jam", font_size=30)
    subtitle.next_to(title, DOWN)

    self.play(Write(title), run_time=1.5)
    self.wait(0.3)

    self.play(FadeIn(subtitle), run_time=1)
    self.wait(0.5)

    circle = Circle(color=BLUE).shift(LEFT * 4)
    square = Square(color=GREEN).shift(RIGHT * 4)

    self.play(
      AnimationGroup(
        circle.animate.move_to(LEFT * 2),
        square.animate.move_to(RIGHT * 2),
        lag_ratio=0.2
      ),
      run_time=2
    )
    self.wait(0.5)

    self.play(
            Transform(circle, square.copy()),
            square.animate.shift(UP * 2),
            run_time=1.5,
            rate_func=smooth
    )
    self.wait(1)

    self.play(
      FadeOut(circle),
      FadeOut(square),
      run_time=0.5
    )
    self.wait(0.5)
