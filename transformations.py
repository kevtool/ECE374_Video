from manim import *
from manim.utils.color import Colors

class Transformations(Scene):
    def construct(self):
        
        # Today we are going to talk about an example of transformations
        text = Text("Transformations", font_size = 90)
        self.add(text)
        self.wait(5)
        self.play(FadeOut(text))
        self.remove(text)

        # Here's the definition of half(L). The langauge half(L) contains strings that are exactly half of strings accepted in the langauge L.
        half_l_def = Tex(r"half(L) := \{w $\vert$ ww $\in$ L\}", font_size = 70)
        self.play(FadeIn(half_l_def))
        self.wait(10)

        self.play(half_l_def.animate.shift(3.6*UP).scale(0.6), run_time=1)
        self.wait(1)

        # For example, let's say that the language L contains the following strings: aaaa, abab, abc.
        # Then half(L) contains these strings: aa, ab.
        L = Text("L", font_size = 60, color=YELLOW)
        L_box=Rectangle(width=4.0, height=5.0,  color=YELLOW)
        L_group = Group(L, L_box).arrange(DOWN, buff=0.3)
        half_L = Text("half(L)", font_size = 45, color=GREEN)
        half_L_box = Rectangle(width=4.0, height=5.0,  color=GREEN)
        half_L_group = Group(half_L, half_L_box).arrange(DOWN, buff=0.3)
        box_group = Group(L_group, half_L_group).arrange(RIGHT, buff=0.6)

        aaaa = Text("aaaa", font_size = 40, color=YELLOW)
        abab = Text("abab", font_size = 40, color=YELLOW)
        abc = Text("abc", font_size = 40, color=YELLOW)
        aa = Text("aa", font_size = 40, color=GREEN)
        ab = Text("ab", font_size = 40, color=GREEN)
        L_ex = Group(aaaa, abab, abc).arrange(DOWN)
        half_L_ex = Group(aa, ab).arrange(DOWN)
        L_ex.shift(2.3*LEFT)
        half_L_ex.shift(2.3*RIGHT)

        self.play(FadeIn(box_group))
        self.wait(0.5)
        self.play(FadeIn(L_ex))
        self.wait(4)
        self.play(FadeIn(half_L_ex))
        self.wait(5)
        self.play(FadeOut(box_group, L_ex, half_L_ex))

        # We can draw an NFA of L, like this. Because we know what strings are in L, 
        # we can also easily construct an NFA of half(L).
        ex_start, ex_a, ex_ab, ex_aaa, ex_aaaa, ex_aa, ex_aba, ex_abab, ex_abc, reject = self.ExampleGroup()
        arrows = self.ExampleArrows()
        ex_txt = self.ExampleText()
        self.play(Create(ex_start), Create(ex_a), Create(ex_aa), Create(ex_aaa), Create(ex_aaaa), Create(ex_ab), Create(ex_aba), Create(ex_abab), Create(ex_abc), Create(reject), FadeIn(arrows), FadeIn(ex_txt))
        self.wait(10)
        self.play(FadeOut(ex_aaaa, ex_aa, ex_aba, ex_abab, ex_abc, reject))
        self.wait(4)
        self.play(FadeOut(ex_start, ex_a, ex_ab, ex_aaa, arrows, ex_txt))
        

        # But what if the language L is arbitrary?
        # Let's say we have an arbitrary language L. We don’t know what strings are inside the language L.
        # L is represented by the NFA M.
        # Our goal is to create a new NFA, that is based on M, that accepts half(L).
        # and turns out we can construct a new NFA using transformations.
        obj_text = MarkupText(f'We are given a DFA <span fgcolor="{YELLOW}">M</span> that accepts L\n(we don\'t know what strings are in L)', font_size = 30, color=BLUE)
        goal_text = MarkupText(f'Our goal is to create an NFA <span fgcolor="{YELLOW}">M\'</span>, based on M, that accepts half(L)', font_size = 30, color=BLUE)
        obj_text.shift(0.7*UP)
        goal_text.shift(0.7*DOWN)

        self.play(FadeIn(obj_text))
        self.wait(10)
        self.play(FadeIn(goal_text))
        self.wait(12)
        self.play(FadeOut(obj_text, goal_text))

        # So how do we approach this problem?
        # Let's try with our example half(L).
        # Here's our strategy. When we receieve an input string, and we want to know if it is in half(L), 
        # then we can try to run it twice on M, the NFA for L.
        # once from the start, and once from the middle point.
        # note that we need to run these simulations simultaneously, 
        # otherwise we run out of input by the time we get to the middle point.

        # So we need to create an NFA, M', based on M, that runs our input string and keeps track of two current states 
        # of the NFA at the same time.

        # we can do this by having M' predict which state M will be in after it has processed w.
        # M’ then processes its received w on two copies of M, one starting at the start of M, 
        # and one starting at the guessed state.
        # If M’ ‘s guess is correct, then M’ will be at an accepting state of M when it finishes processing w.
        strat = Text("Strategy", font_size = 60, color=PINK)
        self.play(FadeIn(strat))
        self.wait(7)

        self.play(strat.animate.shift(2.6*UP).scale(0.6), run_time=1)
        self.wait(1)

        # arbitrary NFA
        start, ac1, ac2, ac3, ac4, ac5, ac6, ac7, ac8 = self.CircleGroup()
        border = Circle(radius=0.6)
        border.shift(5.0*RIGHT + 0.7*DOWN)
        arbarrows = self.ArbArrows()
        self.play(Create(start), Create(ac1), Create(ac2), Create(ac3), Create(ac4), Create(ac5), Create(ac6), Create(ac7), Create(ac8), Create(border), FadeIn(arbarrows))
        self.wait(0.3)

        wxxxx = Text("w = xxxx", font_size = 40, color=Colors.gold_e.value)
        wxxxx.shift(3*DOWN)
        self.play(FadeIn(wxxxx))
        self.wait(4)

        ac1.set_fill(RED, opacity=1.0)
        ac5.set_fill(RED, opacity=1.0)
        wxxxx[2].set_color(WHITE)
        self.wait(1)
        ac2.set_fill(RED, opacity=1.0)
        ac6.set_fill(RED, opacity=1.0)
        ac1.set_fill(PINK, opacity=0.5)
        ac5.set_fill(PINK, opacity=0.5)
        wxxxx[3].set_color(WHITE)
        self.wait(1)
        ac3.set_fill(RED, opacity=1.0)
        ac7.set_fill(RED, opacity=1.0)
        ac2.set_fill(PINK, opacity=0.5)
        ac6.set_fill(PINK, opacity=0.5)
        wxxxx[4].set_color(WHITE)
        self.wait(1)
        ac4.set_fill(RED, opacity=1.0)
        ac8.set_fill(RED, opacity=1.0)
        ac3.set_fill(PINK, opacity=0.5)
        ac7.set_fill(PINK, opacity=0.5)
        wxxxx[5].set_color(WHITE)
        self.wait(9.5)

        self.play(FadeOut(start, ac1, ac2, ac3, ac4, ac5, ac6,  ac7, ac8, border, wxxxx, strat, arbarrows))
        
    

        # Let's write down our strategy so far.
        # First, have our NFA guess the state the original NFA is in,
        # after it has processed our half-word input.
        # We can do this by having our NFA guess every state in the original NFA
        # by creating a new start state s'.
        # if the half word is valid,
        line1 = MarkupText(f'First, have our NFA guess the state the original NFA is in,', font_size = 30, color=BLUE)
        line2 = MarkupText(f'after it has processed our half-word input.', font_size = 30, color=BLUE)
        line3 = MarkupText(f'Let\'s call this the halfway state.', font_size = 30, color=BLUE)
        line4 = MarkupText(f'We can have our NFA guess every state in the original NFA.', font_size = 30, color=BLUE)
        line5 = MarkupText(f'by creating a new start state s\'.', font_size = 30, color=BLUE)
        # we are guaranteed to have one guess that is correct. it's ok if the others guesses are incorrect -- explained after.
        line1.shift(1.1*UP)
        line2.shift(0.7*UP)
        line3.shift(0.3*UP)
        line4.shift(0.7*DOWN)
        line5.shift(1.1*DOWN)

        self.play(FadeIn(line1, line2, line3))
        self.wait(1)
        self.play(FadeIn(line4, line5))
        self.wait(1)
        self.play(FadeOut(line1, line2, line3, line4, line5))

        # now we need to keep track of three things: the guessed state, the current state of the original NFA simulation,
        # and the current state of the simulation starting from the halfway state.

        txt1 = MarkupText(f'Guessed State', font_size = 30, color=BLUE)
        txt2 = MarkupText(f'Current State of Simulation from the Start', font_size = 30, color=BLUE)
        txt3 = MarkupText(f'Current State of Simulation from Halfway', font_size = 30, color=BLUE)

        txt1.shift(0.7*UP)
        txt3.shift(0.7*DOWN)

        self.play(FadeIn(txt1))
        self.wait(0.5)
        self.play(FadeIn(txt2))
        self.wait(0.5)
        self.play(FadeIn(txt3))
        self.wait(0.5)
        self.play(FadeOut(txt1, txt2, txt3))

        # to do this, we can create N copies of the original NFA, N equal to the amount of states in the original NFA.
        # next, we can create epsilon transitions from s' to different states in each copy of the original NFA.
        # we have now guessed every state in the NFA as the midway point. 

        #ANIMATION HERE
        arbnfa = Group(start, ac1, ac2, ac3, ac4, ac5, ac6, ac7, ac8, border)
        arb0 = Group(arbnfa, arbarrows)
        arb1 = arb0.copy().shift(0.2*DOWN)
        self.play(FadeIn(arb1))
        self.wait(1)
        self.play(ScaleInPlace(arb1, 0.2))
        self.wait(1)
        arb2 = arb1.copy().shift(2.8*UP)
        arb3 = arb1.copy().shift(1.4*UP)
        c1 = Circle(radius=0.05, color=WHITE, fill_opacity=1).shift(1.4*DOWN)
        c2 = Circle(radius=0.05, color=WHITE, fill_opacity=1).shift(1.7*DOWN)
        c3 = Circle(radius=0.05, color=WHITE, fill_opacity=1).shift(2.0*DOWN)
        arb4 = Group(c1, c2, c3)
        arb5 = arb1.copy().shift(2.8*DOWN)
        self.play(FadeIn(arb2, arb3, arb4, arb5))
        self.wait(1)

        #then, simultaneously for each guessed state, this NFA will simulate the input string starting from the guessed state.

        #but we also need to keep track of the input string from the original starting state.

        # we need to create N copies of this whole thing.

        #ANIMATION HERE
        arbgroup1 = Group(arb1, arb2, arb3, arb4, arb5)
        self.play(arbgroup1.animate.shift(3.5*LEFT))
        arbgroup2 = arbgroup1.copy().shift(3.5*RIGHT)
        arbgroup3 = arbgroup1.copy().shift(7*RIGHT)
        self.play(FadeIn(arbgroup2, arbgroup3))
        self.wait(1)
        self.play(FadeOut(arbgroup1, arbgroup2, arbgroup3))

        #now The NFA will also run the simulation from the original starting state.

        # Now, if the simulation from the original starting state ends at the guessed state, then we have correctly guessed the halfway state.
        # and if the simultation from the halfway state ends at an accepting state, then the input is accepted by half(L).

        # we will need to keep track of the current states at once, and the guessed halfway state.
        # 
        # (notation)
        qp = Tex(f'Q\' = (Q x Q x Q) ', r"$\cup$" ,' {{s\'}}', font_size = 30, color=BLUE)

        # the accepting states of our new NFA should be states where the simulation from the original starting state ends at the guessed state.
        # (notation)
        # we also need the simultation from the halfway state to end at an accepting state. We can write this as follows:
        # (notation)
        ap = Tex(f'A\'', r' = \{(h, h, q) $\vert$ h $\in$', ' Q and q ', r"$\in$ A\}", font_size = 30, color=BLUE)
        # for the simulation from the original starting state, we should start at s'
        # and for the simultation from the halfway state, we should start at the halfway state.
        # therefore the starting state of our new NFA should be as follows:
        # (notation)
        sp = Tex(f's\' = s\'', font_size = 30, color=BLUE)

        # the transitions should be as follows
        tp1 = Tex(r"$\delta$", f'\' (s\', ' , r"$\epsilon$) = \{(s, h, h) $\vert$ h $\in$ Q\}" ,font_size = 30, color=BLUE)
        tp2 = Tex(r"$\delta$", f'\' (s\', ' , r"a) = $\emptyset$" ,font_size = 30, color=BLUE)
        tp3 = Tex(r"$\delta$", f'\' ((p, h, q), ' , r"$\epsilon$) = $\emptyset$" ,font_size = 30, color=BLUE)
        tp4 = Tex(r"$\delta$", f'\' ((p, h, q), ' , r"a) = \{($\delta$(p, a), h, $\delta$(q, a))\}" ,font_size = 30, color=BLUE)


        qp.shift(1.5*UP)
        ap.shift(1*UP)
        sp.shift(0.5*UP)
        tp1.shift(0.0*DOWN)
        tp2.shift(0.5*DOWN)
        tp3.shift(1*DOWN)
        tp4.shift(1.5*DOWN)

        self.play(FadeIn(qp))
        self.wait(1)
        self.play(FadeIn(ap))
        self.wait(1)
        self.play(FadeIn(sp, tp1, tp2, tp3, tp4))
        self.wait(1)
        self.play(FadeOut(qp, ap, sp, tp1, tp2, tp3, tp4))

        # here's how this looks with our previous example
        # example DFA, show state
        self.play(Create(ex_start), Create(ex_a), Create(ex_aa), Create(ex_aaa), Create(ex_aaaa), Create(ex_ab), Create(ex_aba), Create(ex_abab), Create(ex_abc), Create(reject), FadeIn(arrows), FadeIn(ex_txt))
        self.wait(1)
        currStateOld = Text("current state (original): s", font_size = 30, color=Colors.gold_e.value).shift(2.8*DOWN)
        currStateNew = Text("current state (new NFA): s', ab, ab", font_size = 30, color=Colors.gold_e.value).shift(3.2*DOWN)
        self.play(FadeIn(currStateOld, currStateNew))
        self.wait(1)
        currStateOld.become(Text("current state (original): a", font_size = 30, color=Colors.gold_a.value).shift(2.8*DOWN))
        currStateNew.become(Text("current state (new NFA): a, ab, aba", font_size = 30, color=Colors.gold_a.value).shift(3.2*DOWN))
        ex_a.set_fill(RED, opacity=1.0)
        self.wait(1)
        currStateOld.become(Text("current state (original): ab", font_size = 30, color=Colors.gold_e.value).shift(2.8*DOWN))
        currStateNew.become(Text("current state (new NFA): ab, ab, abab", font_size = 30, color=Colors.gold_e.value).shift(3.2*DOWN))
        ex_a.set_fill(PINK, opacity=0.5)
        ex_ab.set_fill(RED, opacity=1.0)
        self.wait(1)
        self.play(FadeOut(currStateOld, currStateNew))
        self.play(FadeOut(ex_start, ex_a, ex_aa, ex_aaa, ex_aaaa, ex_ab, ex_aba, ex_abab, ex_abc, reject, arrows, ex_txt))

        self.play(half_l_def.animate.shift(3.6*DOWN).scale(1.667), run_time=1)
        self.wait(1)
        
        # hopefully this video has helped you understand transformations.

    def CircleGroup(self):
        start = Circle(radius=0.5, color=Colors.green_a.value)
        start.set_fill(Colors.green_e.value, opacity=0.5)
        start.shift(5.0*LEFT + 0.7*DOWN)

        ac1 = Circle(radius=0.5)
        ac1.set_fill(PINK, opacity=0.5)
        ac1.shift(3.75*LEFT + 0.7*UP)

        ac2 = Circle(radius=0.5)
        ac2.set_fill(PINK, opacity=0.5)
        ac2.shift(2.5*LEFT + 0.7*DOWN)

        ac3 = Circle(radius=0.5)
        ac3.set_fill(PINK, opacity=0.5)
        ac3.shift(1.25*LEFT + 0.7*UP)

        ac4 = Circle(radius=0.5)
        ac4.set_fill(PINK, opacity=0.5)
        ac4.shift(0.0*LEFT + 0.7*DOWN)

        ac5 = Circle(radius=0.5)
        ac5.set_fill(PINK, opacity=0.5)
        ac5.shift(1.25*RIGHT + 0.7*UP)

        ac6 = Circle(radius=0.5)
        ac6.set_fill(PINK, opacity=0.5)
        ac6.shift(2.5*RIGHT + 0.7*DOWN)

        ac7 = Circle(radius=0.5)
        ac7.set_fill(PINK, opacity=0.5)
        ac7.shift(3.75*RIGHT + 0.7*UP)

        ac8 = Circle(radius=0.5)
        ac8.set_fill(PINK, opacity=0.5)
        ac8.shift(5.0*RIGHT + 0.7*DOWN)

        return start, ac1, ac2, ac3, ac4, ac5, ac6, ac7, ac8

    def ExampleGroup(self):
        start = Circle(radius=0.5, color=Colors.green_a.value)
        start.set_fill(Colors.green_e.value, opacity=0.5)
        start.shift(4.0*LEFT + 2.0*UP)

        ex_a = Circle(radius=0.5)
        ex_a.set_fill(PINK, opacity=0.5)
        ex_a.shift(4.0*LEFT + 0.5*UP)

        ex_aa = Circle(radius=0.5)
        ex_aa.set_fill(PINK, opacity=0.5)
        ex_aa.shift(4.0*LEFT + 1.6*DOWN)

        ex_aaa = Circle(radius=0.5)
        ex_aaa.set_fill(PINK, opacity=0.5)
        ex_aaa.shift(1.5*LEFT + 2.0*UP)

        ex_aaaa = Circle(radius=0.5)
        ex_aaaa.set_fill(PINK, opacity=0.5)
        ex_aaaa.shift(0.5*RIGHT + 2.0*UP)

        ex_ab = Circle(radius=0.5)
        ex_ab.set_fill(PINK, opacity=0.5)
        ex_ab.shift(3.3*RIGHT + 2.0*UP)

        ex_aba = Circle(radius=0.5)
        ex_aba.set_fill(PINK, opacity=0.5)
        ex_aba.shift(1.7*LEFT + 0.5*DOWN)

        ex_abab = Circle(radius=0.5)
        ex_abab.set_fill(PINK, opacity=0.5)
        ex_abab.shift(0.9*RIGHT + 1.6*DOWN)

        ex_abc = Circle(radius=0.5)
        ex_abc.set_fill(PINK, opacity=0.5)
        ex_abc.shift(3.3*RIGHT + 1.6*DOWN)

        reject = Circle(radius=0.5)
        reject.set_fill(PINK, opacity=0.5)
        reject.shift(4.0*RIGHT + 0.5*UP)

        return start, ex_a, ex_aa, ex_aaa, ex_aaaa, ex_ab, ex_aba, ex_abab, ex_abc, reject

    def ExampleArrows(self):
        arrow1 = Arrow(start=1*LEFT, end=1*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.1).shift(2.75*LEFT + 2.0*UP)
        arrow2 = Arrow(start=0.75*LEFT, end=0.75*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(0.5*LEFT + 2.0*UP)
        arrow3 = Arrow(start=1.1*LEFT, end=1.1*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.1).shift(1.85*RIGHT + 2.0*UP)
        arrow4 = Arrow(start=0.5*UP, end=0.5*DOWN, color=WHITE, max_stroke_width_to_length_ratio=6, max_tip_length_to_length_ratio=0.25).shift(4.0*LEFT + 1.25*UP)
        arrow5 = Arrow(start=0.75*UP, end=0.75*DOWN, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(4.0*LEFT + 0.55*DOWN)
        arrow6 = Arrow(start=2.2*LEFT, end=2.2*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=1, max_tip_length_to_length_ratio=0.05).shift(1.55*LEFT + 1.6*DOWN)
        arrow7 = Arrow(start=0.9*LEFT, end=0.9*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(2.05*RIGHT + 1.6*DOWN)
        arrow8 = Arrow(start=1*LEFT, end=0.75*UP+0.8*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.1).shift(2.85*LEFT + 1.35*DOWN)
        arrow9 = Arrow(start=2.8*LEFT, end=0.75*UP+2.35*RIGHT, color=WHITE, max_stroke_width_to_length_ratio=1, max_tip_length_to_length_ratio=0.05).shift(1.425*RIGHT + 0.35*DOWN)
        arrow10 = Arrow(start=0.55*LEFT+0.5*UP, end=0.4*DOWN, color=WHITE, max_stroke_width_to_length_ratio=6, max_tip_length_to_length_ratio=0.25).shift(3.9*RIGHT + 1.15*UP)
        arrow11 = Arrow(start=0.5*LEFT+1*DOWN, end=0.55*UP, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.15).shift(4.0*RIGHT + 0.3*DOWN)
        border1 = Circle(radius=0.6).shift(3.3*RIGHT + 2.0*UP)
        border2 = Circle(radius=0.6).shift(1.7*LEFT + 0.5*DOWN)
        border3 = Circle(radius=0.6).shift(3.3*RIGHT + 1.6*DOWN)
        arrows = Group(arrow1, arrow2, arrow3, arrow4, arrow5, arrow6, arrow7, arrow8, arrow9, arrow10, arrow11, border1, border2, border3)

        return arrows

    def ExampleText(self):
        txt1 = Text("a", font_size = 25, color=WHITE).shift(4.0*LEFT + 0.5*UP)
        txt2 = Text("ab", font_size = 25, color=WHITE).shift(4.0*LEFT + 1.6*DOWN)
        txt3 = Text("aa", font_size = 25, color=WHITE).shift(1.5*LEFT + 2.0*UP)
        txt4 = Text("aaa", font_size = 25, color=WHITE).shift(0.5*RIGHT + 2.0*UP)
        txt5 = Text("aaaa", font_size = 25, color=WHITE).shift(3.3*RIGHT + 2.0*UP)
        txt6 = Text("abc", font_size = 25, color=WHITE).shift(1.7*LEFT + 0.5*DOWN)
        txt7 = Text("aba", font_size = 25, color=WHITE).shift(0.9*RIGHT + 1.6*DOWN)
        txt8 = Text("abab", font_size = 25, color=WHITE).shift(3.3*RIGHT + 1.6*DOWN)
        txt9 = Text("reject", font_size = 25, color=WHITE).shift(4.0*RIGHT + 0.5*UP)

        txt = Group(txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9)

        return txt

    def ArbArrows(self):
        arrow1 = Arrow(start=0.47*LEFT+0.47*DOWN, end=0.47*RIGHT+0.47*UP, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(4.35*LEFT)
        arrow2 = Arrow(start=0.47*LEFT+0.47*UP, end=0.47*RIGHT+0.47*DOWN, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(3.1*LEFT)
        arrow3 = Arrow(start=0.47*LEFT+0.47*DOWN, end=0.47*RIGHT+0.47*UP, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(1.85*LEFT)
        arrow4 = Arrow(start=0.47*LEFT+0.47*UP, end=0.47*RIGHT+0.47*DOWN, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(0.6*LEFT)
        arrow5 = Arrow(start=0.47*LEFT+0.47*DOWN, end=0.47*RIGHT+0.47*UP, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(0.6*RIGHT)
        arrow6 = Arrow(start=0.47*LEFT+0.47*UP, end=0.47*RIGHT+0.47*DOWN, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(1.85*RIGHT)
        arrow7 = Arrow(start=0.47*LEFT+0.47*DOWN, end=0.47*RIGHT+0.47*UP, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(3.1*RIGHT)
        arrow8 = Arrow(start=0.47*LEFT+0.47*UP, end=0.45*RIGHT+0.45*DOWN, color=WHITE, max_stroke_width_to_length_ratio=3, max_tip_length_to_length_ratio=0.18).shift(4.35*RIGHT)

        arrows = Group(arrow1, arrow2, arrow3, arrow4, arrow5, arrow6, arrow7, arrow8)

        return arrows