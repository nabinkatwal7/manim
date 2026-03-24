from manim import *

class PlaceboExplainer(MovingCameraScene):
    def construct(self):

        # ------------------ SCENE 1: HOOK ------------------
        title = Text("The Placebo Effect", font_size=64)
        subtitle = Text("Is it real or just belief?", font_size=32)

        subtitle.next_to(title, DOWN)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)

        self.play(
            self.camera.frame.animate.scale(0.8),
            run_time=1.5
        )

        # ------------------ SCENE 2: DEFINITION ------------------
        self.play(FadeOut(title), FadeOut(subtitle))

        text1 = Text("A placebo has no real medicine", font_size=36)
        self.play(Write(text1), run_time=2)
        self.wait(1)

        text2 = Text("But patients still feel better", font_size=36)

        self.play(Transform(text1, text2), run_time=2)
        self.wait(1)

        # ------------------ SCENE 3: VISUAL ------------------
        self.play(FadeOut(text1))

        patient = Circle(color=BLUE).shift(LEFT * 3)
        pill = Square(color=GREEN).scale(0.5).shift(RIGHT * 3)

        label1 = Text("Patient", font_size=24).next_to(patient, DOWN)
        label2 = Text("Sugar Pill", font_size=24).next_to(pill, DOWN)

        self.play(Create(patient), Write(label1))
        self.play(Create(pill), Write(label2))
        self.wait(1)

        # move pill to patient
        self.play(
            pill.animate.move_to(patient.get_center()),
            run_time=2
        )

        self.wait(1)

        # ------------------ SCENE 4: RESULT ------------------
        happy = Text("Feels Better!", font_size=36).shift(RIGHT * 3)

        self.play(
            ReplacementTransform(patient, happy),
            run_time=2
        )

        self.wait(1)

        # ------------------ SCENE 5: BRAIN EFFECT ------------------
        brain = Circle(color=RED).scale(1.2)
        brain_text = Text("Brain releases chemicals", font_size=32)

        brain_text.next_to(brain, DOWN)

        self.play(
            ReplacementTransform(happy, brain),
            Write(brain_text),
            run_time=2
        )

        self.wait(1)

        # camera zoom for emphasis
        self.play(
            self.camera.frame.animate.move_to(brain).scale(0.7),
            run_time=2
        )

        self.wait(1)

        # ------------------ SCENE 6: CONCLUSION ------------------
        self.play(FadeOut(brain), FadeOut(brain_text))

        final = Text("Belief can trigger real healing", font_size=40)

        self.play(Write(final), run_time=2)
        self.wait(2)