from manim import *

class IdentischeEbenen(Scene):
    def construct(self):
        Title = Text("Schauen wir uns identische Ebenen an!")
        self.play(Write(Title), runtime=3)
        self.play(ApplyMethod(Title.move_to, [0,3.5,0]), runtime=1)
        #"Wären die beiden Ebenen von gerade identisch gewesen, hätten wir das am Normalvektor erkennen können. Wenn die Normalvektoren kollinear sind und ein Punkt der Ebene auch in der anderen liegt, sind die Ebenen identisch"
        #Ebenen L und R, diesmal gleich
        
        #[0,0,3] in eine Ebene einsetzen, zeigen, dass sie gleich sind
        #"Der Stützvektor einer Ebene ist hier sehr beliebt, da wir nicht rechnen müssen, um zu wissen, ob er in dieser Ebene liegt. Jetzt prüfen wir, ob sich beim Einsetzen in die andere ein Widerspruch ergibt"
        #kein Widerspruch
        #"Wie wir sehen können, ergibt sich kein Widerspruch, sondern eine schöne Gleichung. Beide Ebenen sind also gleich. Das war's auch schon mit identischen Ebenen, das Verfahren ist hier sehr einfach."