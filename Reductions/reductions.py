from manim import *
from manim.utils.color import Colors

class Reductions(Scene):
    def construct(self):
        
        # Today we are going to look at an example of reductions.
        text = Text("Reductions", font_size = 90)
        self.add(text)
        self.wait(5)
        self.play(FadeOut(text))
        self.remove(text)

        # Let's look at the known NP-Hard problem CLIQUE.
        clique_text = Tex(r"CLIQUE", font_size = 70)
        self.play(FadeIn(clique_text))
        self.wait(6)
        self.play(clique_text.animate.shift(2.8*UP).scale(0.6), run_time=1)
        self.wait(0.2)

        # The problem CLIQUE is the following: (show CLIQUE)
        # Given an undirected graph G and an integer k, 
        # does G have a subset of vertices of size greater than or equal to k
        # where every two vertices are connected by an edge?

        txt1 = MarkupText(f'Given an undirected graph G and an integer k,', font_size = 30, color=BLUE).shift(1.4*UP)
        txt2 = MarkupText(f'does G have a subset of vertices of size greater than or equal to k', font_size = 30, color=BLUE)
        txt3 = MarkupText(f'where every two vertices are connected by an edge?', font_size = 30, color=BLUE).shift(1.4*DOWN)

        self.play(FadeIn(txt1))
        self.wait(3)
        self.play(FadeIn(txt2, txt3))
        self.wait(8)
        self.play(FadeOut(txt1, txt2, txt3))

        # This is what a clique looks like. Given this graph, 
        # if k is 7, or any number smaller than 7, 
        # then the output to the CLIQUE problem is YES.

        clique1 = self.clique()
        self.play(FadeIn(clique1))
        self.wait(4)
        txt1 = Tex(r"k = 7", font_size = 30).shift(2.5*DOWN)
        txt2 = Tex(r"YES", font_size = 30).shift(2.9*DOWN)

        self.play(FadeIn(txt1))
        self.wait(5)
        self.play(FadeIn(txt2))
        self.wait(8)
        self.play(FadeOut(clique1, txt1, txt2))

        # To clarify, the graph doesn't have to be exactly the clique, 
        # it just has to include the clique.
        # if the graph has extra vertices, like this, 
        # if k is 7, or any number smaller than 7, 
        # then the output to the CLIQUE problem is also YES.

        clique1 = self.clique_alt()
        self.play(FadeIn(clique1))
        self.wait(4)

        self.play(FadeIn(txt1))
        self.wait(4.5)
        self.play(FadeIn(txt2))
        self.wait(2)
        self.play(FadeOut(clique1, txt1, txt2))

        self.play(FadeOut(clique_text))
        self.wait(3)

        # We know that the problem CLIQUE is NP-Hard.
        # Now consider the following: DUMBBELL.
        
        dumbbell_text = Tex(r"DUMBBELL", font_size = 70)
        self.play(FadeIn(dumbbell_text))
        self.wait(0.5)
        self.play(dumbbell_text.animate.shift(2.8*UP).scale(0.6), run_time=1)
        self.wait(1.5)

        # A dumbbell looks like this:
        # two disjoint cliques connected by a single edge.
        dumbbell1 = self.dumbbell()
        self.play(FadeIn(dumbbell1))
        self.wait(0.5)
        subtxt = MarkupText(f'(7, 7)-dumbbell', font_size = 30, color=BLUE).shift(2.5*DOWN)
        self.play(FadeIn(subtxt))
        self.wait(4.5)
        self.play(FadeOut(subtxt))
        self.play(FadeOut(dumbbell1))

        # Then, the DUMBBELL problem is the following:
        # Given an undirected graph G and an integer k,
        # does G contain a (k, k)-dumbbell as a subgraph?
        txt1 = MarkupText(f'Given an undirected graph G and an integer k', font_size = 30, color=BLUE).shift(0.7*UP)
        txt2 = MarkupText(f'does G contain a (k, k)-dumbbell as a subgraph?', font_size = 30, color=BLUE).shift(0.7*DOWN)
        self.play(FadeIn(txt1))
        self.wait(3)
        self.play(FadeIn(txt2))
        self.wait(5)
        self.play(FadeOut(txt1, txt2))

        self.play(FadeOut(dumbbell_text))
        self.wait(9)

        # in order to prove that DUMBBELL is NP-Hard, 
        # we need to prove that some known NP-Hard problem is reducible to DUMBBELL.
        # we pick CLIQUE, because they are similar problems.
        # so how do we reduce from CLIQUE to DUMBBELL?
        # we need to prove that for each DUMBBELL instance we have a corresponding CLIQUE instance.
        txt1 = MarkupText(f'CLIQUE -> DUMBBELL', font_size = 30, color=BLUE).shift(0.7*UP)
        txt2 = MarkupText(f'Prove that for each DUMBBELL we have a corresponding CLIQUE.', font_size = 30, color=BLUE).shift(0.7*DOWN)

        self.play(FadeIn(txt1))
        self.wait(9)
        self.play(FadeIn(txt2))
        self.wait(5)
        self.play(FadeOut(txt1, txt2))

        # Meaning, when we encounter a DUMBBELL instance, we can point to its CLIQUE instance, 
        # and say, "If that particular CLIQUE instance produces a YES output,
        # then this particular DUMBBELL problem must also produce a YES output.
        # and if that particular CLIQUE instance produces a NO output, 
        # then this particular DUMBBELL problem must also produce a NO output."

        txt1 = MarkupText(f'CLIQUE', font_size = 30, color=BLUE).shift(1.5*UP)
        txt2 = MarkupText(f'Does this graph have a k-clique?', font_size = 20, color=BLUE).shift(1.0*UP)
        gsq1 = Rectangle(width=2.0, height=2.0,  color=YELLOW).shift(1.5*UP+4.0*LEFT)
        arrow1 = Arrow(start=0.75*LEFT, end=0.75*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=2, max_tip_length_to_length_ratio=0.1).shift(2.5*LEFT + 1.5*UP)
        arrow2 = Arrow(start=0.75*LEFT, end=0.75*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=2, max_tip_length_to_length_ratio=0.1).shift(2.5*RIGHT + 1.5*UP)
        txtG = MarkupText(f'G', font_size = 30, color=YELLOW).shift(1.5*UP+4.0*LEFT)
        txt3 = MarkupText(f'DUMBBELL', font_size = 30, color=BLUE).shift(1.5*DOWN)
        txt4 = MarkupText(f'Does this graph have a (k, k)-dumbbell?', font_size = 20, color=BLUE).shift(2.0*DOWN)
        gsq2 = Rectangle(width=2.0, height=2.0,  color=PINK).shift(1.5*DOWN+4.0*LEFT)
        arrow3 = Arrow(start=0.75*LEFT, end=0.75*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=2, max_tip_length_to_length_ratio=0.1).shift(2.5*LEFT + 1.5*DOWN)
        arrow4 = Arrow(start=0.75*LEFT, end=0.75*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=2, max_tip_length_to_length_ratio=0.1).shift(2.5*RIGHT + 1.5*DOWN)
        txtP = MarkupText(f'G\'', font_size = 30, color=PINK).shift(1.5*DOWN+4.0*LEFT)
        txtY1 = MarkupText(f'YES', font_size = 32, color=BLUE).shift(1.5*UP+4.0*RIGHT)
        txtY2 = MarkupText(f'YES', font_size = 32, color=BLUE).shift(1.5*DOWN+4.0*RIGHT)
        txtN1 = MarkupText(f'NO', font_size = 32, color=BLUE).shift(1.5*UP+4.0*RIGHT)
        txtN2 = MarkupText(f'NO', font_size = 32, color=BLUE).shift(1.5*DOWN+4.0*RIGHT)
        gtop = Group(txt1, txt2, gsq1, arrow1, arrow2, txtG)
        gbot = Group(txt3, txt4, gsq2, arrow3, arrow4, txtP)
        gyes = Group(txtY1, txtY2)
        gno = Group(txtN1, txtN2)

        self.play(FadeIn(gtop, gbot))
        self.wait(7.5)
        self.play(FadeIn(txtY1))
        self.wait(4)
        self.play(FadeIn(txtY2))
        self.wait(3.5)
        self.play(FadeOut(gyes))
        self.wait(1)
        self.play(FadeIn(txtN1))
        self.wait(4.5)
        self.play(FadeIn(txtN2))
        self.wait(3)
        self.play(FadeOut(gtop, gbot, gno))
        self.wait(1)


        # How do we do this?
        # Let's start by considering the problem CLIQUE, where k=7.
        # The output of this problem tells us if a graph has a 7-clique or not.

        clique_text = Tex(r"CLIQUE, k = 7", font_size = 70).shift(0.5*UP)
        k7_text = Tex(r"Does this graph have a 7-clique?", font_size = 30).shift(0.5*DOWN)
        self.play(FadeIn(clique_text, k7_text))
        self.wait(10)
        self.play(FadeOut(clique_text, k7_text))

        # Now, imagine an arbitrary graph G.
        # Right now we don't know what G looks like, or if G has a 7-clique or not.

        clique1 = self.clique()
        self.play(FadeIn(clique1))
        self.wait(2)
        gsq1 = Rectangle(width=4.0, height=4.0, color=YELLOW)
        txtG = MarkupText(f'G', font_size = 65, color=YELLOW)
        box1 = Group(gsq1, txtG)
        self.play(Transform(clique1, box1))
        self.wait(9)

        # First, we copy the existing graph G to form a new graph G'.
        # Right now, G' is the exact same graph as G.

        self.play(clique1.animate.shift(2.0*LEFT).scale(0.6), run_time=1)
        gsq1 = Rectangle(width=4.0, height=4.0, color=PINK)
        txtG = MarkupText(f'G\'', font_size = 65, color=PINK)
        box2 = Group(gsq1, txtG).shift(2.0*RIGHT).scale(0.6)
        self.play(FadeIn(box2))
        self.play(FadeOut(clique1), box2.animate.shift(2.0*LEFT), run_time=1)
        self.wait(9)
        
        # Then, we create a 7-clique.

        self.play(box2.animate.shift(2.5*LEFT).scale(1.4), run_time=1)
        clique1 = self.clique().shift(2.0*RIGHT)
        self.play(FadeIn(clique1))
        self.wait(6)
        
        # Now, choose one of the vertices from the 7-clique,
        # and connect it to every vertex in G'.

        vertex = clique1[0][3]
        lines = VGroup()
        for i in range(6):
            l1 = Line(vertex)
            l1.put_start_and_end_on(vertex.get_center(), (1.5-0.6*i)*UP+0.8*LEFT)
            lines.add(l1) 
        self.play(FadeIn(lines))
        self.wait(5)
        self.play(FadeOut(box2, clique1, lines))
        self.wait(2)

        # For example, if G looks like this:

        clique1 = self.clique_alt()
        self.play(FadeIn(clique1))
        self.wait(3)

        # Then, G' would look like this. 
        # You can see that this vertex is connected to every vertex in the original graph.
        # G has a clique, so G' has a dumbbell.

        self.play(clique1.animate.shift(2.5*LEFT))
        clique2 = self.clique().shift(2.5*RIGHT+0.2*DOWN)
        vertex = clique2[0][3]
        lines = VGroup()
        for i in range(len(clique1[0])):
            l1 = Line(vertex, clique1[0][i])
            lines.add(l1) 
        self.play(FadeIn(clique2, lines))
        self.wait(1)
        for i in range(6):
            vertex.set_fill(WHITE, opacity=1.0)
            self.wait(0.25)
            vertex.set_fill(PINK, opacity=0.5)
            self.wait(0.25)
        self.wait(8)
        self.play(FadeOut(clique1, clique2, lines))
        self.wait(1.8)

        # and if G looks like this:

        tri1 = self.triangle()
        self.play(FadeIn(tri1))
        self.wait(2.5)

        # then, G' would look like this. 
        # G doesn't have a clique, so G' doesn't have a dumbbell.

        self.play(tri1.animate.shift(2.5*LEFT))
        clique2 = self.clique().shift(2.5*RIGHT)
        vertex = clique2[0][3]
        lines = VGroup()
        for i in range(len(tri1[0])):
            l1 = Line(vertex, tri1[0][i])
            lines.add(l1) 
        self.play(FadeIn(clique2, lines))
        self.wait(7)
        self.play(FadeOut(tri1, clique2, lines))
        self.wait(8)

        # if we apply this graph transformation to every instance,
        # we can claim that G' has a (k, k)-dumbbell 
        # if and only if G has a clique of size k.
        # IMPORTANT!

        txt1 = MarkupText(f'G\' has a (k, k)-dumbbell...', font_size = 30, color=BLUE).shift(0.7*UP)
        txt2 = MarkupText(f'if and only if G has a clique of size k.', font_size = 30, color=BLUE).shift(0.7*DOWN)

        self.play(FadeIn(txt1))
        self.wait(2.5)
        self.play(FadeIn(txt2))
        self.wait(2.5)
        self.play(FadeOut(txt1, txt2))
        self.wait(4)

        # We have successfully reduced the problem CLIQUE to DUMBBELL.
        # Because CLIQUE can be reduced to DUMBBELL, 
        # we can say that DUMBBELL is at least as hard as CLIQUE.
        # Then, since CLIQUE is NP-Hard, DUMBBELL is NP-Hard.

        txt1 = MarkupText(f'CLIQUE -> DUMBBELL', font_size = 50, color=WHITE)
        self.play(FadeIn(txt1))
        self.wait(16)


    def clique(self):
        c1 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.0*LEFT + 1.6*UP)
        c2 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.4*LEFT + 0.87*UP)
        c3 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.4*RIGHT + 0.87*UP)
        c4 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.8*LEFT + 0.26*DOWN)
        c5 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.8*RIGHT + 0.26*DOWN)
        c6 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.9*LEFT + 1.4*DOWN)
        c7 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.9*RIGHT + 1.4*DOWN)
        
        clique = Group(c1, c2, c3, c4, c5, c6, c7)
        lines = VGroup()
        for i in range(7):
            for j in range(7):
                if i != j:
                    l1 = Line(clique[i], clique[j])
                    lines.add(l1)

        clique1 = Group(clique, lines)
        return clique1

    def clique_alt(self):
        c1 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.0*LEFT + 1.6*UP)
        c2 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.4*LEFT + 0.87*UP)
        c3 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.4*RIGHT + 0.87*UP)
        c4 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.8*LEFT + 0.26*DOWN)
        c5 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.8*RIGHT + 0.26*DOWN)
        c6 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.9*LEFT + 1.4*DOWN)
        c7 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.9*RIGHT + 1.4*DOWN)
        c8 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.4*LEFT + 1.8*UP)
        c9 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.4*RIGHT + 1.8*UP)
        c10 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.9*LEFT + 1.8*DOWN)
        c11 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.9*RIGHT + 1.8*DOWN)

        clique = Group(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11)
        lines = VGroup()
        for i in range(7):
            for j in range(7):
                if i != j:
                    l1 = Line(clique[i], clique[j])
                    lines.add(l1)

        l1 = Line(clique[7], clique[8])
        l2 = Line(clique[1], clique[7])
        l3 = Line(clique[2], clique[8])
        l4 = Line(clique[9], clique[10])
        l5 = Line(clique[5], clique[9])
        l6 = Line(clique[6], clique[10])
        lines.add(l1, l2, l3, l4, l5, l6)

        clique1 = Group(clique, lines)
        return clique1


    def triangle(self):
        c1 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.0*LEFT + 1.0*UP)
        c2 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.0*LEFT + 1.0*DOWN)
        c3 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.0*RIGHT + 1.0*DOWN)
        
        triangle = Group(c1, c2, c3)
        lines = VGroup()
        for i in range(3):
            for j in range(3):
                if i != j:
                    l1 = Line(triangle[i], triangle[j])
                    lines.add(l1)

        triangle1 = Group(triangle, lines)
        return triangle1
            

    def dumbbell(self):
        c1 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(2.5*LEFT + 1.6*UP)
        c2 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(3.9*LEFT + 0.87*UP)
        c3 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.1*LEFT + 0.87*UP)
        c4 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(4.3*LEFT + 0.26*DOWN)
        c5 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.7*LEFT + 0.26*DOWN)
        c6 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(3.4*LEFT + 1.4*DOWN)
        c7 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.6*LEFT + 1.4*DOWN)
        c8 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(2.5*RIGHT + 1.6*UP)
        c9 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.1*RIGHT + 0.87*UP)
        c10 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(3.9*RIGHT + 0.87*UP)
        c11 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(0.7*RIGHT + 0.26*DOWN)
        c12 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(4.3*RIGHT + 0.26*DOWN)
        c13 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(1.6*RIGHT + 1.4*DOWN)
        c14 = Circle(radius=0.1).set_fill(PINK, opacity=0.5).shift(3.4*RIGHT + 1.4*DOWN)

        dumbbell = Group(c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14)

        lines = VGroup()
        for i in range(7):
            for j in range(7):
                if i != j:
                    l1 = Line(dumbbell[i], dumbbell[j])
                    lines.add(l1)

        for i in range(7, 14):
            for j in range(7, 14):
                if i != j:
                    l1 = Line(dumbbell[i], dumbbell[j])
                    lines.add(l1)
        l = Line(dumbbell[4], dumbbell[10])
        lines.add(l)

        dumbbell1 = Group(dumbbell, lines)
        return dumbbell1