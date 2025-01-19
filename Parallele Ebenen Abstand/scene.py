from manim import *

class GetAxisLabelsExample(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(0, PI/2)
        self.wait(1)
        axes = ThreeDAxes()
        self.play(FadeIn(axes, runtime=2))
        self.wait(1)

        self.move_camera(phi=3*PI/5, theta=PI/10, runtime = 3)
        # u = (1, 2, 1); v = (1, -1, 2); Polygon(-10u, -10v, 10u, 10v)
        plane1 = Polygon([-2, -4, -2], [-2, 2, -4], [2,4,2], [2,-2,4], color=RED)
        plane2 = Polygon([-2, -4, 1], [-2, 2, -1], [2,4,5], [2,-2,7], color=PURPLE)
        plane2.set_fill(PURPLE, opacity=0.5)
        plane1.set_fill(RED, opacity=0.5)

        
        #adding planes: "Zur Veranschaulichung hier zwei Ebenen"
        self.play(FadeIn(plane1, runtime=1))
        self.begin_ambient_camera_rotation(0.3)
        self.wait(4.15)
        self.stop_ambient_camera_rotation()
        self.wait(1)
        self.play(FadeIn(plane2, runtime=1))
        self.wait(1)

        #add hilfsgerade
        line = Line3D(start=np.array([0, 0, 0]), end=np.array([-1.285, 0.257, 0.771]), color=GREY)
        self.play(Write(line, runtime=2))

        #add text for hilfsgerade
        lineText = Text("Hilfsgerade", color=WHITE)
        lineText.move_to([-0.5, 0, 0])
        self.add_fixed_in_frame_mobjects(lineText)
        self.play(Write(lineText, runtime=0.5))

        #remove text for hilfsgerade
        self.play(FadeOut(lineText, runtime=0.5))
        self.wait(0.5)

        #add lotfußpunkt
        lotfußpunkt = Dot3D(point=[-1.285, 0.257, 0.771], color=PINK)
        self.play(FadeIn(lotfußpunkt, runtime=0.5))
        self.wait(1)

        #add text for lotfußpunkt
        punktText = Text("Lotfußpunkt", color=WHITE)
        punktText.move_to([3.75, 1.5, 0])
        self.add_fixed_in_frame_mobjects(punktText)
        self.play(Write(punktText, runtime=0.5))
        self.wait(0.5)

