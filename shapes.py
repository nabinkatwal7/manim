from manim import *

class Day2(Scene):
  def construct(self):
    circle = Circle(color=BLUE)
    square = Square(color=GREEN)
    triangle = Triangle(color=RED)

    group = VGroup(circle, square, triangle).arrange(RIGHT, buff=1)

    self.play(Create(group))

    self.wait()

class Challenge2(Scene):
  def construct(self):
    circle = Circle(color=BLUE)
    square = Square(color=GREEN)
    triangle = Triangle(color=RED)

    circle.shift(LEFT * 2 + DOWN)
    square.shift(RIGHT * 2 + DOWN)
    triangle.shift(UP * 2)

    self.play(Create(circle), Create(square), Create(triangle))
    self.wait()

class Challenge3(Scene):
  def construct(self):
    circle = Circle(color=BLUE).shift(LEFT * 3)
    square = Square(color=GREEN).shift(RIGHT * 3)

    self.play(Create(circle), Create(square))

    self.play(square.animate.move_to(circle.get_center()))
    self.wait()

class Challenge4(Scene):
  def construct(self):
    circle = Circle(color=BLUE).shift(LEFT * 3)
    square = Square(color=GREEN).shift(RIGHT * 3)
    triangle = Triangle(color=RED).shift(UP * 2)

    self.play(Create(circle), Create(square), Create(triangle))

    self.play(
      circle.animate.move_to(ORIGIN),
      square.animate.move_to(ORIGIN),
      triangle.animate.move_to(ORIGIN)
    )
    self.wait()

class Challenge5(Scene):
  def construct(self):
    circle = Circle(color=BLUE)
    square = Square(color=GREEN)
    triangle = Triangle(color=RED)

    circle.shift(LEFT * 2 + DOWN)
    square.shift(RIGHT * 2 + DOWN)
    triangle.next_to(circle, UP)

    triangle.move_to([0,2,0])

    self.play(Create(circle), Create(square), Create(triangle))
    self.wait()

# Horizontal ->  Vertical Rearrangement
class P1(Scene):
  def construct(self):
    c = Circle()
    s = Square()
    t = Triangle()

    shapes = VGroup(c, s, t).arrange(RIGHT, buff=1)

    self.play(Create(shapes))
    self.wait()

    self.play(shapes.animate.arrange(DOWN))
    self.wait()

# Center alignment fix
class P2(Scene):
  def construct(self):
    c = Circle().shift(LEFT * 2)
    s = Square().shift(RIGHT * 3)

    self.play(Create(c), Create(s))

    s.move_to([0,0,0])

    self.wait()

# animated centering
class P3(Scene):
  def construct(self):
    c = Circle().shift(LEFT * 3)
    s = Square().shift(RIGHT * 3)

    self.play(Create(c), Create(s))

    self.play(c.animate.move_to(ORIGIN), s.animate.move_to(ORIGIN))

    self.wait()

# stack using next_to
class P4(Scene):
  def construct(self):
    c = Circle()
    s = Square()
    t = Triangle()

    s.next_to(c, DOWN)
    t.next_to(s, DOWN)

    self.play(Create(c), Create(s), Create(t))
    self.wait()

# chain layout (smart positioning)
class P5(Scene):
  def construct(self):
    c = Circle()
    s = Square().next_to(c, RIGHT)
    t = Triangle().next_to(s, RIGHT)

    self.play(Create(c), Create(s), Create(t))
    self.wait()

# diagonal movement
class P6(Scene):
  def construct(self):
    c = Circle()

    self.play(Create(c))

    self.play(c.animate.shift(UP + RIGHT))
    self.wait()

# opposite directions
class P7(Scene):
  def construct(self):
    c = Circle().shift(LEFT * 2)
    s = Square().shift(RIGHT * 2)

    self.play(Create(c), Create(s))

    self.play(
      c.animate.shift(RIGHT * 2),
      s.animate.shift(LEFT * 2)
    )

    self.wait()

# follow movement (tracking)
class P8(Scene):
  def construct(self):
    c = Circle()
    s = Square().shift(RIGHT * 2)

    self.play(Create(c), Create(s))

    self.play(c.animate.move_to(s.get_center()))
    self.wait()

# expand outward from center
class P9(Scene):
  def construct(self):
    c = Circle()
    s = Square()
    t = Triangle()

    shapes = VGroup(c, s, t)

    self.play(Create(shapes))

    self.play(
      c.animate.shift(LEFT * 3),
      s.animate.shift(RIGHT * 3),
      t.animate.shift(UP * 3)
    )

    self.wait()

# rotate around object
class P10(Scene):
  def construct(self):
    c = Circle()
    s = Square().shift(RIGHT * 2)

    self.play(Create(c), Create(s))

    self.play(Rotate(c, angle=PI, about_point=s.get_center()))
    self.wait()

class P11(Scene):
  def construct(self):
    c = Circle(color=BLUE)
    s = Square(color=GREEN)
    t = Triangle(color=RED)

    shapes = VGroup(c, s, t)
    shapes.arrange(RIGHT, buff=1)

    self.play(Create(shapes))
    self.wait(1)


    self.play(t.animate.next_to(s, UP, buff=0.5))
    self.wait(0.5)

    self.play(
      c.animate.shift(LEFT * 1.5),
      s.animate.shift(RIGHT * 1.5),
      t.animate.shift(UP * 1.5)
    )
    self.wait(1)

    self.play(shapes.animate.scale(1.2))
    self.wait()