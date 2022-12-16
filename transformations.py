from manim import *
from manim.utils.color import Colors

class Transformations(Scene):
    def construct(self):
        #  Transformations
        text = Text("Transformations", font_size = 90)
        self.add(text)
        self.wait(1)
        self.play(FadeOut(text))
        self.remove(text)

        # "half(L)"
        half_l_def = Text("half(L) := {w | ww is in L}", font_size = 70)
        self.play(FadeIn(half_l_def))
        self.wait(1)

        self.play(half_l_def.animate.shift(3.6*UP).scale(0.6), run_time=1)
        self.wait(1)

        # boxes
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
        self.wait(1)
        self.play(FadeIn(L_ex))
        self.wait(1)
        self.play(FadeIn(half_L_ex))
        self.wait(1)
        self.play(FadeOut(box_group, L_ex, half_L_ex))

        # NFAs
        ex_start, ex_a, ex_aa, ex_aaa, ex_aaaa, ex_ab, ex_aba, ex_abab, ex_abc, reject = self.ExampleGroup()
        arrows = self.ExampleArrows()
        self.play(Create(ex_start), Create(ex_a), Create(ex_aa), Create(ex_aaa), Create(ex_aaaa), Create(ex_ab), Create(ex_aba), Create(ex_abab), Create(ex_abc), Create(reject), FadeIn(arrows))
        self.wait(1)
        self.play(FadeOut(ex_start, ex_a, ex_aa, ex_aaa, ex_aaaa, ex_ab, ex_aba, ex_abab, ex_abc, reject, arrows))
        

        # objective
        obj_text = MarkupText(f'We are given a DFA <span fgcolor="{YELLOW}">M</span> that accepts L\n(we don\'t know what strings are in L)', font_size = 30, color=BLUE)
        goal_text = MarkupText(f'Our goal is to create an NFA <span fgcolor="{YELLOW}">M\'</span>, based on M, that accepts half(L)', font_size = 30, color=BLUE)
        obj_text.shift(0.7*UP)
        goal_text.shift(0.7*DOWN)

        self.play(FadeIn(obj_text))
        self.wait(1)
        self.play(FadeIn(goal_text))
        self.wait(1)
        self.play(FadeOut(obj_text, goal_text))

        # strategy
        strat = Text("Strategy", font_size = 60, color=PINK)
        self.play(FadeIn(strat))
        self.wait(1)

        self.play(strat.animate.shift(2.6*UP).scale(0.6), run_time=1)
        self.wait(1)

        # arbitrary NFA
        start, ac1, ac2, ac3, ac4, ac5, ac6, ac7, ac8 = self.CircleGroup()
        border = Circle(radius=0.6)
        border.shift(5.0*RIGHT + 0.7*DOWN)
        self.play(Create(start), Create(ac1), Create(ac2), Create(ac3), Create(ac4), Create(ac5), Create(ac6), Create(ac7), Create(ac8), Create(border))
        self.wait(0.3)

        wxxxx = Text("w = xxxx", font_size = 40, color=Colors.gold_e.value)
        wxxxx.shift(3*DOWN)
        self.play(FadeIn(wxxxx))
        self.wait(1)

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
        self.wait(1)

        self.play(FadeOut(start, ac1, ac2, ac3, ac4, ac5, ac6,  ac7, ac8, border, wxxxx, strat))

        # example NFA
        self.play(Create(ex_start), Create(ex_a), Create(ex_aa), Create(ex_aaa), Create(ex_aaaa), Create(ex_ab), Create(ex_aba), Create(ex_abab), Create(ex_abc), Create(reject), FadeIn(arrows))
        self.wait(1)
        self.play(FadeOut(ex_start, ex_a, ex_aa, ex_aaa, ex_aaaa, ex_ab, ex_aba, ex_abab, ex_abc, reject, arrows))

        # steps
        step1 = MarkupText(f'Step 1: Have our NFA guess the state the original DFA is in,\n after it has processed our half-word input.', font_size = 30, color=BLUE)
        step2 = MarkupText(f'We can have our NFA guess every state in the original DFA\n by creating a new start state s\',\n and adding a e-transition from s\' to each state.', font_size = 30, color=BLUE)
        step1.shift(0.7*UP)
        step2.shift(0.9*DOWN)

        self.play(FadeIn(step1))
        self.wait(1)
        self.play(FadeIn(step2))
        self.wait(1)
        self.play(FadeOut(step1, step2))

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