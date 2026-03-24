from manim import *

class D3_1(Scene):
  def construct(self):
    text1 = Text("Nabin")
    text2 = Text("Katwal")

    self.play(Write(text1))
    self.wait()

    self.play(Transform(text1, text2))
    self.wait()

class D3_2(Scene):
  def construct(self):
    circle = Circle()
    square = Square()

    self.play(Create(circle))
    self.wait()

    self.play(Transform(circle, square))
    self.wait()

class D3_3(Scene):
  def construct(self):
    t1 = Text("Step 1")
    t2 = Text("Step 2")

    self.play(Write(t1))
    self.wait()

    self.play(ReplacementTransform(t1, t2))
    self.wait()

class D3_4(Scene):
  def construct(self):
    circle = Circle().shift(LEFT * 3)
    square = Square().shift(RIGHT * 3)

    self.play(Create(circle), Create(square))

    self.play(
      Transform(circle, square.copy()),
      square.animate.shift(UP * 3)
    )
    self.wait()

class D3_5(Scene):
  def construct(self):
    title = Text("Transform")
    self.play(Write(title))
    self.wait(1)

    new_title = Text("With Animation")
    self.play(Transform(title, new_title))
    self.wait(1)

    circle = Circle(color=BLUE)
    self.play(ReplacementTransform(title, circle))
    self.wait(1)

    square = Square(color=GREEN)
    self.play(Transform(circle, square))
    self.wait(1)

    triangle = Triangle(color=RED)
    self.play(
      Transform(circle, triangle),
      circle.animate.shift(UP)
    )
    self.wait(1)

# text 1 -> text 2 -> text 3 -> text 4
class D3_6(Scene):
  def construct(self):
    text1 = Text("Text 1", color=BLUE)
    text2 = Text("Text 2", color=GREEN)
    text3 = Text("Text 3", color=RED)
    text4 = Text("Text 4", color=YELLOW)

    self.play(Write(text1))
    self.wait(1)
    self.play(ReplacementTransform(text1, text2))
    self.wait(1)
    self.play(ReplacementTransform(text2, text3))
    self.wait(1)
    self.play(ReplacementTransform(text3, text4))
    self.wait(1)

# circle -> square -> triangle -> circle
class D3_7(Scene):
  def construct(self):
    circle = Circle(color=BLUE)
    square = Square(color=GREEN)
    triangle = Triangle(color=RED)

    self.play(Create(circle))
    self.wait(1)

    self.play(ReplacementTransform(circle, square))
    self.wait(1)

    self.play(ReplacementTransform(square, triangle))
    self.wait(1)

    self.play(ReplacementTransform(triangle, circle))
    self.wait(1)

# move and transform at same time
class D3_8(Scene):
  def construct(self):
    text = Text("Text")
    circle = Circle(color=BLUE)

    self.play(Write(text))
    self.wait(1)

    circle.move_to(text.get_center())
    circle.shift(UP)

    self.play(ReplacementTransform(text, circle))
    self.wait(1)

# text on left -> shape on right -> transform both
class D3_9(Scene):
  def construct(self):
    text = Text("Text").shift(LEFT * 3)
    text2 = Text("Text New").shift(LEFT * 3)

    circle = Circle(color=BLUE).shift(RIGHT * 3)
    square = Square(color=GREEN).shift(RIGHT * 3)

    self.play(Write(text), Write(circle))
    self.wait(1)

    self.play(ReplacementTransform(text, text2), ReplacementTransform(circle, square))
    self.wait(1)

# text -> circle -> square -> text again
class D3_10(Scene):
  def construct(self):
    text = Text("Text")
    circle = Circle(color=BLUE).shift(LEFT * 1)
    square = Square(color=GREEN).shift(LEFT * 2)
    text2 = Text("Text New").shift(LEFT * 3)

    self.play(Write(text))
    self.wait(1)

    self.play(ReplacementTransform(text, circle))
    self.wait(1)

    self.play(ReplacementTransform(circle, square))
    self.wait(1)

    self.play(ReplacementTransform(square, text2))
    self.wait(1)

# clean text morph chain
class T1(Scene):
  def construct(self):
    text1 = Text("Text 1")

    self.play(Write(text1))
    self.wait()

    self.play(Transform(text1, Text("Text 2")))
    self.wait()

    self.play(Transform(text1, Text("Text 3")))
    self.wait()

# shape morph cycle
class T2(Scene):
  def construct(self):
    shape1 = Circle(color=BLUE)

    self.play(Create(shape1))
    self.wait()

    self.play(Transform(shape1, Square(color=GREEN)))
    self.play(Transform(shape1, Triangle(color=RED)))
    self.play(Transform(shape1, Circle(color=BLUE)))
    self.wait()

# move and morph together
class T3(Scene):
  def construct(self):
    circle = Circle(color=BLUE).shift(LEFT * 3)
    square = Square(color=GREEN).shift(RIGHT * 3)

    self.play(Create(circle))

    self.play(Transform(circle, square))
    self.wait()

# cross transformation (swap positions)
class T4(Scene):
  def construct(self):
    circle = Circle(color=BLUE).shift(LEFT * 2)
    square = Square(color=GREEN).shift(RIGHT * 2)

    self.play(Create(circle), Create(square))
    self.wait()

    self.play(
      Transform(circle, square.copy()),
      Transform(square, circle.copy())
    )

    self.wait()

# split transformation (group into smaller parts)
class T5(Scene):
  def construct(self):
    group = VGroup(Circle(color=BLUE), Square(color=GREEN), Triangle(color=RED))
    group.arrange(RIGHT, buff=1)

    self.play(Create(group))
    self.wait()

    self.play(group.animate.arrange(DOWN))
    self.wait()

# partial morph
class T6(Scene):
  def construct(self):
    text1 = Text("HELLO")
    text2 = Text("WORLD")

    self.play(Write(text1))
    self.wait()

    self.play(TransformMatchingShapes(text1, text2))
    self.wait()