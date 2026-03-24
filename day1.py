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

class Text1(Scene):
  def construct(self):
    title = Text("Test Text", font_size=64)
    subtitle = Text("Subtitle Text", font_size=36)

    subtitle.next_to(title, DOWN * 2)

    self.play(Write(title))
    self.play(FadeIn(subtitle))
    self.wait()

class Text2(Scene):
  def construct(self):
    t1 = Text("Test Text")
    t2 = Text("Subtitle Text")
    t3 = Text("Subtitle Text 2")

    self.play(Write(t1))
    self.wait(1)

    self.play(Transform(t1, t2))
    self.wait(1)

    self.play(Transform(t1, t3))
    self.wait(1)

class Text3(Scene):
  def construct(self):
    text = Text("Test Text")

    text.shift(LEFT * 4)

    self.play(text.animate.shift(RIGHT * 4))
    self.wait()

class Text4(Scene):
  def construct(self):
    text = Text("IMPORTANT")

    self.play(Write(text))
    self.wait(0.5)

    self.play(text.animate.scale(1.5))
    self.play(text.animate.scale(0.7))
    self.wait()

class Text5(Scene):
  def construct(self):
    words = VGroup(Text("Hello"), Text("World"))
    words.arrange(RIGHT, buff=0.5)

    for word in words:
      self.play(Write(word))

    self.wait(0.5)

class Text6(Scene):
  def construct(self):
    text = Text("Manim is Powerful")

    self.play(Write(text))
    self.wait()

    text[0:5].set_color(BLUE)
    text[5:].set_color(GREEN)

    self.wait()

class Text7(Scene):
  def construct(self):
    t1 = Text("Test Text 1")
    t2 = Text("Test Text 2")
    t3 = Text("Test Text 3")

    self.play(FadeIn(t1))
    self.wait()

    self.play(FadeOut(t1), FadeIn(t2))
    self.wait()

    self.play(FadeOut(t2), FadeIn(t3))
    self.wait()

class IntroScene(Scene):
  def construct(self):
    title = Text("Welcome to the Course", font_size=64)
    subtitle = Text("This is a test", font_size=36)

    title.set_color(BLUE)
    subtitle.set_color(GREEN)

    subtitle.next_to(title, DOWN)

    self.play(Write(title))
    self.play(Write(subtitle))
    self.wait()
