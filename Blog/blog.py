from manim import *
from manim.utils.color import Colors

class Graph:
    def __init__(self, scene, vertices_list, edges_list):
        self.scene = scene

        # set up vertices
        self.vertices = VGroup()
        self.add_vertices(vertices_list) 

        # set up lines
        self.edges = VGroup()
        self.add_edges(edges_list)

    # Given a list, add vertices accordingly
    def add_vertices(self, list):
        for rad, color, opac, x, y in list:
            v = Circle(radius=rad).set_fill(color, opacity=opac).shift(RIGHT*x + UP*y)
            self.vertices.add(v)

    def add_edges(self, list):
        for v1, v2 in list:
            l = Line(self.vertices[v1], self.vertices[v2])
            self.edges.add(l)

    # Simultaneously create all vertices
    def create_vertices(self):
        animations = []
        for i in range(len(self.vertices)): 
            animations.append(Create(self.vertices[i]))
        self.scene.play(*animations)

    # Show lines
    def show_edges(self):
        self.scene.play(FadeIn(self.edges))

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

        graph1 = Graph(self, graph1_vlist, graph1_elist)
        graph1.create_vertices()
        graph1.show_edges()