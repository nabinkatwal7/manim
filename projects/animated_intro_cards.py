from manim import *

class AnimatedIntroCards(Scene):
  def construct(self):
        title = Text("Animated Intro Cards", font_size=56)
        subtitle = Text("Text + Shapes Animation", font_size=30)

        subtitle.next_to(title, DOWN, buff=0.4)

        text_group = VGroup(title, subtitle)

        circle = Circle(color=BLUE).scale(0.6)
        square = Square(color=GREEN).scale(0.6)
        triangle = Triangle(color=RED).scale(0.6)

        circle.shift(LEFT * 5)
        square.shift(RIGHT * 5)
        triangle.shift(UP * 3)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(0.5)

        self.play(
            circle.animate.move_to(title.get_left() + LEFT * 1.5),
            square.animate.move_to(title.get_right() + RIGHT * 1.5),
            triangle.animate.next_to(subtitle, DOWN, buff=1),
        )
        self.wait(1)

        final_group = VGroup(text_group, circle, square, triangle)
        self.play(final_group.animate.shift(UP * 0.5))
        self.wait(1)