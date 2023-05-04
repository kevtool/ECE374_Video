from manim import *
from manim.utils.color import Colors

class Graph:
    def __init__(self, scene, vertices_list, edges_list, weights_list, dists_list):
        self.scene = scene

        # set up vertices
        self.vertices = VGroup()
        self.add_vertices(vertices_list) 

        # set up lines
        self.edges = VGroup()
        self.add_edges(edges_list)

        # set up weights
        self.weights = VGroup()
        self.add_weights(weights_list)

        # set up dists
        self.dists = VGroup()
        self.add_dists(dists_list)

    # Functions to convert lists to objects
    # --------------------------- #
    def add_vertices(self, list):
        for rad, color, opac, x, y in list:
            v = Circle(radius=rad).set_fill(color, opacity=opac).shift(RIGHT*x + UP*y)
            self.vertices.add(v)

    def add_edges(self, list):
        for v1, v2 in list:
            l = Line(self.vertices[v1], self.vertices[v2])
            self.edges.add(l)

    def add_weights(self, list):
        for string, size, col, x, y in list:
            text = Tex(string, font_size=size, color=col).shift(RIGHT*x + UP*y)
            self.weights.add(text)

    def add_dists(self, list):
        for string, size, col, x, y in list:
            text = Tex(string, font_size=size, color=col).shift(RIGHT*x + UP*y)
            self.dists.add(text)
    # --------------------------- #

    # Show objects
    # --------------------------- #
    def create_vertices(self):
        animations = []
        for i in range(len(self.vertices)): 
            animations.append(Create(self.vertices[i]))
        self.scene.play(*animations)

    def show_edges(self):
        self.scene.play(FadeIn(self.edges))

    def ShowWeights(self):
        self.scene.play(FadeIn(self.weights))

    def ShowDists(self):
        self.scene.play(FadeIn(self.dists))

    def addEverything(self):
        self.scene.add(self.vertices)
        self.scene.add(self.edges)
        self.scene.add(self.weights)
        self.scene.add(self.dists)
    # --------------------------- #


class Dijkstra(Scene):
    def construct(self):

        # radius, color, opacity, X, Y
        graph1_vlist = [[0.3, WHITE, 1, -3.0, -2.0],
                        [0.3, WHITE, 1, 0.3, -2.8],
                        [0.3, WHITE, 1, 0.0, 0.0],
                        [0.3, WHITE, 1, 4.0, 0.3],
                        [0.3, WHITE, 1, 1.3, 2.5],
                        [0.3, WHITE, 1, -2.5, 1.5]]
        
        # edges list
        graph1_elist = [[0,1],
                        [0,2],
                        [0,5],
                        [1,2],
                        [1,3],
                        [2,3],
                        [2,5],
                        [3,4],
                        [5,4]]
        
        graph1_wlist = [
                # each entry corresponds to its line in line list
                [r"7", 35, WHITE, -1.5, -2.8],
                [r"9", 35, WHITE, -3.1, -0.3],
                [r"14", 35, WHITE, -1.7, -0.7], 
                [r"10", 35, WHITE, -0.1, -1.5],
                [r"15", 35, WHITE, 1.7, -1.2],
                [r"11", 35, WHITE, 1.9, 0.4],
                [r"2", 35, WHITE, -1.0, 0.9],
                [r"6", 35, WHITE, 2.7, 1.7],
                [r"9", 35, WHITE, -0.7, 2.3],

                # start and end vertices
                [r"a", 35, YELLOW, -3.0, -2.6],
                [r"b", 35, YELLOW, 1.8, 2.8]]
        
        graph1_dlist = [
                [r"0", 27, BLUE, -3.5, -1.5],
                [r"inf", 27, BLUE, -0.2, -2.3],
                [r"inf", 27, BLUE, 0.0, 0.6],
                [r"inf", 27, BLUE, 4.0, 0.9],
                [r"inf", 27, BLUE, 0.8, 3.0],
                [r"inf", 27, BLUE, -3.0, 2.0]]
        
        graph1_clist = [[r"0 + 7 \textless\ inf", r"7", -0.2, -2.3],
                [r"0 + 14 \textless\ inf", r"14", 0.3, 0.6],
                [r"0 + 9 \textless\ inf", r"9", -2.7, 2.0],
                [r"7 + 10 \textgreater\ 14", r"14", 0.3, 0.6],
                [r"7 + 15 \textless\ inf", r"22", 4.5, 0.9],
                [r"14 + 11 \textgreater\ 22", r"22", 4.5, 0.9],
                [r"14 + 2 \textgreater\ 9", r"9", -2.7, 2.0],
                [r"22 + 6 \textless\ inf", r"28", 0.8, 3.0],
                [r"9 + 9 \textless\ 28", r"18", 0.8, 3.0]]

        graph1 = Graph(self, graph1_vlist, graph1_elist, graph1_wlist, graph1_dlist)
        graph1.addEverything()

        prevv = -1
        for (v1, v2), (str1, str2, x, y) in zip(graph1_elist, graph1_clist):
            if prevv != v1:
                if prevv != -1:
                    graph1.vertices[prevv].set_fill(RED, opacity=1.0)
                graph1.vertices[v1].set_fill(YELLOW, opacity=1.0)
                self.play(Flash(graph1.vertices[v1], flash_radius=graph1_vlist[v1][0]+0.1))
                self.wait(0.5)
                prevv = v1

            arrow = Arrow(graph1.vertices[v1], graph1.vertices[v2], color=RED)
            self.blink(arrow)

            graph1.dists[v2] = Tex(str1, font_size=25, color=TEAL_A).shift(RIGHT*x + UP*y)
            self.wait(1.5)
            graph1.dists[v2] = Tex(str2, font_size=27, color=BLUE).shift(RIGHT*x + UP*y)
            self.wait(1.5)
        
        self.wait(6)

    # given an object, blink it five times.
    def blink(self, obj):
        for i in range(5):
            self.add(obj)
            self.wait(0.25)
            self.remove(obj)
            self.wait(0.25)
        
