from manim import *

class D5_1(MovingCameraScene):
  def construct(self):
    text = Text("Hello, World!")

    self.play(Write(text))
    self.wait()

    self.play(self.camera.frame.animate.scale(0.5))
    self.wait()

class D5_2(MovingCameraScene):
  def construct(self):
    c = Circle().shift(LEFT * 3)
    s = Square().shift(RIGHT * 3)

    self.play(Create(c), Create(s))

    self.play(self.camera.frame.animate.move_to(c))
    self.wait()

    self.play(self.camera.frame.animate.move_to(s))
    self.wait()

class D5_3(MovingCameraScene):
  def construct(self):
    c = Circle()

    self.play(Create(c))

    self.play(
      c.animate.shift(RIGHT * 4),
      self.camera.frame.animate.move_to(c)
    )

    self.wait()

class D5_4(MovingCameraScene):
  def construct(self):
    c = Circle().shift(RIGHT * 3)

    self.play(Create(c))

    self.play(
      self.camera.frame.animate.move_to(c).scale(0.5)
    )

    self.wait()

class D5_5(MovingCameraScene):
    def construct(self):
        title = Text("Manim Camera", font_size=60)
        circle = Circle(color=BLUE).shift(LEFT * 4)
        square = Square(color=GREEN).shift(RIGHT * 4)

        self.play(Write(title))
        self.play(Create(circle), Create(square))
        self.wait(1)

        self.play(
            self.camera.frame.animate.move_to(circle).scale(0.6),
            run_time=2
        )
        self.wait(0.5)

        self.play(
            circle.animate.shift(RIGHT * 3),
            self.camera.frame.animate.move_to(circle),
            run_time=2
        )

        self.wait(0.5)

        self.play(
            self.camera.frame.animate.move_to(square),
            run_time=2
        )

        self.wait(0.5)

        self.play(
            self.camera.frame.animate.move_to(ORIGIN).scale(2),
            run_time=2
        )

        self.wait(1)