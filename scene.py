from manim import *

class ParalleleEbenen(Scene):
    def construct(self):
        self.wait(0.5)

        #Title
        #Also, rechnen wir das Beispiel aus der Animation durch:
        Title = Text("Rechnen wir das Beispiel aus der Animation!").scale(0.5)
        self.play(Write(Title, runtime=2))
        self.play(ApplyMethod(Title.move_to, [0,3.5,0]), runtime=1)

        #"Hier sehen wir die rote und lilafarbene Ebene, die sinf von mir gestellt."
        t1 = Tex(r"$\mathrm{Rote \: Ebene \: (R):} \: \vec{u_1} = \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \: \mathrm{und} \: \vec{v_1} = \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$")
        self.play(Write(t1, runtime=3))
        self.wait(2)
        t11 = Tex(r"$\mathrm{R: \:} \vec{x_1} = \begin{pmatrix} 0 \\ 0 \\ 0 \end{pmatrix} + \begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \cdot \mathrm{q} + \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} \cdot \mathrm{r}$")
        t11.move_to([0, -2, 0])
        self.play(Write(t11, runtime=1))
        self.play(ApplyMethod(t1.scale, 0.5), runtime = 0.5)
        self.play(ApplyMethod(t1.move_to, [-4.5,2.5,0]), runtime=1)
        self.play(ApplyMethod(t11.scale, 0.5), runtime = 0.5)
        self.play(ApplyMethod(t11.move_to, [-4.5,1.5,0]), runtime=1)

        t2 = Tex(r"$\mathrm{Lilafarbene \: Ebene \: (L):} \: \vec{u_2} = \begin{pmatrix} -1 \\ -2 \\ -1 \end{pmatrix} \: \mathrm{und} \: \vec{v_2} = \begin{pmatrix} -1 \\ 1 \\ -2 \end{pmatrix} \: \mathrm{mit \: St\text{ü}tzvektor} \: \vec{s} = \begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix}$").scale(0.7)
        self.play(Write(t2, runtime=3))
        self.wait(2)
        t21 = Tex(r"$\mathrm{L: \:} \vec{x_2} = \begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix} + \begin{pmatrix} -1 \\ -2 \\ -1 \end{pmatrix} \cdot \mathrm{s} + \begin{pmatrix} -1 \\ 1 \\ -2 \end{pmatrix} \cdot \mathrm{t}$")
        t21.move_to([0, -2, 0])
        self.play(Write(t21, runtime=1))
        self.play(ApplyMethod(t2.scale, 0.714), runtime = 0.5)
        self.play(ApplyMethod(t2.move_to, [2.75,2.5,0]), runtime=1)
        self.play(ApplyMethod(t21.scale, 0.5), runtime = 0.5)
        self.play(ApplyMethod(t21.move_to, [4,1.5,0]), runtime=1)

        #"Der erste Schritt ist hier immer die Berechnung der Normalvektoren. Über das Vektorprodukt beider Stützvektoren der jeweiligen Ebenen kommen wir an die Normalvektoren."
        t3 = Tex(r"$\mathrm{Normalvektoren \: berechnen:} \: \vec{n_R} = \:\begin{pmatrix} 1 \\ 2 \\ 1 \end{pmatrix} \times \begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix}$")
        self.play(Write(t3, runtime=5))
        self.wait(2)
        t31= Tex(r"$\vec{n_L} = \:\begin{pmatrix} -1 \\ -2 \\ -1 \end{pmatrix} \times \begin{pmatrix} -1 \\ 1 \\ -2 \end{pmatrix} = \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix}$")
        t31.move_to([0, -2, 0])
        self.play(Write(t31, runtime=4))

        #start transitioning to calculations
        self.play(FadeOut(t1), FadeOut(t2), FadeOut(Title), FadeOut(t3), FadeOut(t31))
        self.play(ApplyMethod(t11.move_to, [-4.5,3.5,0], aligned_edge=[0,1,0]), ApplyMethod(t21.move_to, [4,3.5,0], aligned_edge=[0,1,0]))
        n1 = Tex(r"$\vec{n_R} = \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix}$").scale(0.5)
        n2 = Tex(r"$\vec{n_L} = \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix}$").scale(0.5)
        n1.move_to([-4.5, 2.5, 0])
        n2.move_to([4, 2.5, 0])
        self.play(FadeIn(n1), FadeIn(n2))
        #"Hier fällt direkt auf, dass die Normalvektoren kollinear sind. Das ist schonmal ein gutes Zeichen, wenn wir beweisen wollen, dass zwei Ebenen parallel sind."
        t4= Text("Die Normalvektoren sind kollinear!")
        self.wait(2)
        self.play(Write(t4))
        self.wait(1)
        self.play(FadeOut(t4), runtime=1)

        #Normalformen
        #"Jetzt stellen wir die Normalformen für die Ebenen auf. Zur Erinnerung: Wir bilden immer die Differenz aus einem beliebigen Punkt und einem auf der Ebene und überprüfen dann mit dem Normalvektor, ob dieser neue Vektor im rechten Winkel zum Normalvektor steht. Wenn das stimmt, ist der beliebige Punkt teil der Ebene."
        nForm = Tex(r"$\mathrm{Normalform: \:} [\vec{x} - \vec{p}] \cdot \vec{n}$")
        R1 = Tex(r"$\mathrm{R: \:} \vec{x} \cdot \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix}$")
        R1.move_to([-2, -1.5, 0])
        L1 = Tex(r"$\mathrm{L: \:} [\vec{x} - \begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix}] \cdot \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix}$")
        L1.move_to([2, -1.5, 0])
        self.play(Write(nForm))
        self.wait(3)
        self.play(Write(R1), runtime=3)
        self.wait(3)
        self.play(Write(L1), runtime=3)
        self.wait(3)
        leftover = VGroup()
        for obj in self.mobjects:
            if issubclass(obj.__class__, VMobject):
                leftover += obj
        self.play(Unwrite(leftover))
        self.wait(1)

        #Prüfen, ob identisch!!!!!!!!!!!!!
        i1 = Text("Prüfen wir, ob die Ebenen identisch sind!")
        self.play(Write(i1), runtime=2)
        i2 = Text("Liegt ein Punkt von R in L?")
        i2.move_to([0, -1, 0])
        self.play(Write(i2), runtime=2)
        self.play(Unwrite(i1))
        self.play(ApplyMethod(i2.move_to, [0,3.5,0]), Unwrite(i1), runtime=1)
        L2 = Tex(r"$\mathrm{L \: in \: Koordinatenform: L:} \: 5x_1 - x_2 - 3x_3 = -9$")
        self.play(Write(L2), runtime=3)
        self.play(ApplyMethod(L2.move_to, [0,2.5,0]))
        L3 = Tex(r"$\begin{pmatrix} 0 \\ 0 \\ 3 \end{pmatrix} \: \mathrm{in \: L \: einsetzen:} 5 \cdot (0) - (0) -3 \cdot (0) = 0 \neq -9$")
        self.play(Write(L3), runtime=3)
        L4 = Text("Der Stützvektor von R liegt nicht in L!")
        self.play(ApplyMethod(L3.move_to, [0,1.5,0]))
        self.play(Write(L4), runtime=3)
        #Würden sie einen Punkt teilen und der Normalvektor wäre kollinear, würden sie alle Punkte teilen und deshalb identisch sein 
        leftover = VGroup()
        for obj in self.mobjects:
            if issubclass(obj.__class__, VMobject):
                leftover += obj
        self.play(Unwrite(leftover))
        self.wait(2)

        #"Jetzt wollen wir die Hilfsgerade erstellen"
        Title2 = Text("Erstellen der Hilfsgerade")
        self.play(Write(Title2), runtime=3)
        self.play(ApplyMethod(Title2.move_to, [0,3.5,0]), runtime=1)
        self.play(Write(R1), Write(L1))
        self.play(ApplyMethod(R1.move_to, [-4.5,3.5,0], aligned_edge=[0,1,0]), ApplyMethod(L1.move_to, [4,3.5,0], aligned_edge=[0,1,0]))
        #L2 = Tex(r"$\mathrm{L:} \: 5x_1 - x_2 - 3x_3 = -9$")
        #self.play(Write(L2))
        self.wait(2)
        self.play(ApplyMethod(L1.move_to, [4,2,0], aligned_edge=[0,1,0]))
        #Bemerkung: g geht von [0,0,0] aus, deshalb kein Stützvektor -> Verweis auf Animation
        G1 = Tex(r"$\mathrm{Definieren \: der \: Gerade \: g: } \: \vec{x_3} = \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix} \cdot \mathrm{w}$")
        G1.move_to([0, -2.5, 0])
        self.play(Write(G1), runtime=3)
        #Weiter mit Einsetzen der Gerade und Berechnen des SP, danach Länge der Distanz berechnen
        self.wait(3)
        self.play(ApplyMethod(L2.scale, 0.5), ApplyMethod(L2.move_to, [0, 3, 0]), ApplyMethod(G1.scale, 0.5), ApplyMethod(G1.move_to, [0, 2, 0]))
        G2 = Tex(r"$\mathrm{Einsetzen \: von \: g \: in \: L \: (zeilenweise): \:} 5 \cdot (5w) - (-w) - 3 \cdot (-3w) = -9$").scale(0.7)
        self.play(Write(G2, runtime=3))
        G3 = Tex(r"$35w = -9 <=> w = -\frac{9}{35}$")
        G3.move_to([0, -1.5, 0])
        self.play(Write(G3))
        self.play(FadeOut(L2), FadeOut(G1))
        self.play(ApplyMethod(G2.scale, 0.5), ApplyMethod(G2.move_to, [0, 3, 0]), ApplyMethod(G3.scale, 0.5), ApplyMethod(G3.move_to, [0, 2, 0]))
        G4 = Tex(r"$w = -\frac{9}{35} \: \mathrm{in \: g \: einsetzen:} \vec{x_3} = \begin{pmatrix} 5 \\ -1 \\ -3 \end{pmatrix} \cdot -\frac{9}{35} \approx \begin{pmatrix} -1.286 \\ 0.257 \\ 0.771 \end{pmatrix}$")
        G4.move_to([0, 1, 0])
        self.play(Write(G4, runtime=3))
        self.wait(3)
        G5 = Tex(r"$\vec{d} = \begin{pmatrix}0 - (-1.286) \\ 0 - 0.257 \\ 0 - 0.771\end{pmatrix} = \begin{pmatrix} 1.286 \\ -0.257 \\ -0.771\end{pmatrix}$")
        G5.move_to([0, -1.5, 0])
        self.play(Write(G5, runtime=3))
        self.wait(3)
        G6 = Tex(r"$d = \sqrt{(1.286)^2 + (-0.257)^2 + (-0.771)^2} \approx 1.516 \mathrm{\: LE}$")
        G6.move_to([0, -3, 0])
        self.play(Write(G6, runtime=3))
        self.wait(3)

    
