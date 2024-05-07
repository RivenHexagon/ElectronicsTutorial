from manim import *

config.media_width = "75%"
config.verbosity = "INFO"

%%manim -qm CircleToSquare

class CircleToSquare(Scene):
    def construct(self):
        p1 = [-1,-1, 0]
        p2 = [ 1,-1, 0]
        p3 = [ 1, 1, 0]
        p4 = [-1, 1, 0]
        l1 = Line(p1,p2)
        l2 = Line(p2,p3)
        l3 = Line(p3,p4)
        sr = Rectangle(fill_color=BLACK, fill_opacity=1.0).shift(UP).scale(0.1)
        
        #a  = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        #point_start  = a.get_start()
        #point_end    = a.get_end()
        #point_center = a.get_center()
        self.add(l1)
        self.add(l2)
        self.add(l3)
        self.add(sr)
