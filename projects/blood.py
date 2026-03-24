from manim import *

class HeartFlowExplainer(MovingCameraScene):
    def construct(self):
        # ---------------------------
        # SCENE 1: TITLE
        # ---------------------------
        title = Text("How Blood Flows Through the Heart", font_size=42)
        subtitle = Text("A simple medical animation", font_size=26)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=1)
        self.wait(1)

        self.play(FadeOut(title), FadeOut(subtitle), run_time=1)

        # ---------------------------
        # SCENE 2: LAYOUT
        # ---------------------------
        heart = Square(color=RED).scale(1.2)
        heart_label = Text("Heart", font_size=24).next_to(heart, DOWN)

        body = Circle(color=BLUE).shift(LEFT * 4)
        body_label = Text("Body", font_size=24).next_to(body, DOWN)

        lungs = Circle(color=GREEN).shift(RIGHT * 4)
        lungs_label = Text("Lungs", font_size=24).next_to(lungs, DOWN)

        self.play(
            Create(body),
            Create(heart),
            Create(lungs),
            Write(body_label),
            Write(heart_label),
            Write(lungs_label),
            run_time=2
        )
        self.wait(1)

        # ---------------------------
        # SCENE 3: DEOXYGENATED BLOOD
        # Body -> Heart
        # ---------------------------
        deoxy_text = Text("Low-oxygen blood returns from the body", font_size=28)
        deoxy_text.to_edge(UP)

        blood1 = Dot(color=BLUE).move_to(body.get_center())

        self.play(Write(deoxy_text), run_time=1.5)
        self.play(FadeIn(blood1), run_time=0.5)

        self.play(
            blood1.animate.move_to(heart.get_center()),
            self.camera.frame.animate.move_to(heart).scale(0.9),
            run_time=2
        )
        self.wait(1)

        # ---------------------------
        # SCENE 4: HEART -> LUNGS
        # ---------------------------
        lungs_text = Text("The heart sends it to the lungs", font_size=28)
        lungs_text.to_edge(UP)

        self.play(ReplacementTransform(deoxy_text, lungs_text), run_time=1)

        self.play(
            blood1.animate.move_to(lungs.get_center()),
            self.camera.frame.animate.move_to(lungs),
            run_time=2
        )
        self.wait(1)

        # ---------------------------
        # SCENE 5: OXYGEN PICKUP
        # ---------------------------
        oxy_text = Text("In the lungs, blood picks up oxygen", font_size=28)
        oxy_text.to_edge(UP)

        oxygen_blood = Dot(color=YELLOW).move_to(lungs.get_center())

        self.play(
            ReplacementTransform(lungs_text, oxy_text),
            ReplacementTransform(blood1, oxygen_blood),
            run_time=1.5
        )
        self.wait(1)

        # ---------------------------
        # SCENE 6: LUNGS -> HEART
        # ---------------------------
        return_text = Text("Oxygen-rich blood returns to the heart", font_size=28)
        return_text.to_edge(UP)

        self.play(ReplacementTransform(oxy_text, return_text), run_time=1)

        self.play(
            oxygen_blood.animate.move_to(heart.get_center()),
            self.camera.frame.animate.move_to(heart),
            run_time=2
        )
        self.wait(1)

        # ---------------------------
        # SCENE 7: HEART -> BODY
        # ---------------------------
        pump_text = Text("Then the heart pumps it out to the body", font_size=28)
        pump_text.to_edge(UP)

        self.play(ReplacementTransform(return_text, pump_text), run_time=1)

        self.play(
            oxygen_blood.animate.move_to(body.get_center()),
            self.camera.frame.animate.move_to(body),
            run_time=2
        )
        self.wait(1)

        # ---------------------------
        # SCENE 8: SUMMARY VIEW
        # ---------------------------
        summary = Text("Heart → Lungs → Heart → Body", font_size=34)
        summary.to_edge(UP)

        self.play(
            FadeOut(pump_text),
            Write(summary),
            self.camera.frame.animate.move_to(ORIGIN).scale(1.8),
            run_time=2
        )
        self.wait(2)

        # ---------------------------
        # SCENE 9: FINAL MESSAGE
        # ---------------------------
        final_text = Text("This cycle keeps your body alive", font_size=34)

        self.play(
            FadeOut(summary),
            FadeOut(body_label),
            FadeOut(heart_label),
            FadeOut(lungs_label),
            FadeOut(oxygen_blood),
            run_time=1
        )

        self.play(Write(final_text), run_time=2)
        self.wait(2)