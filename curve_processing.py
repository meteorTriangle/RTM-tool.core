from arrow_position import *
import math
from linearCore import linear



class arcCurve:
    class linearRay:
        def __init__(self, point: minecraft_coordinate_real, deg: float) -> None:
            self.sX = point.x
            self.sY = point.z
            self.deg = deg % 360
    def __init__(self, arrow1: arrow, arrow2: arrow, radius: int):
        self.arrow1 = arrow1
        self.arrow2 = arrow2
        self.radius = radius
        self.a1point = linear.point(self.arrow1.processing.x(), self.arrow1.processing.z())
        self.a2point = linear.point(self.arrow2.processing.x(), self.arrow2.processing.z())
        self.line1 = linear.linearFunc()
        self.line1.point_deg((self.arrow1.processing.x(), self.arrow1.processing.z()), 
                             self.arrow1.processing.railDeg())
        self.line2 = linear.linearFunc()
        self.line2.point_deg((self.arrow2.processing.x(), self.arrow2.processing.z()), 
                             self.arrow2.processing.railDeg())
    
        self.crossPoint = linear.point(*(self.line1 & self.line2))
        self.arcAngle = abs(self.arrow1.processing.railDeg() - ((self.arrow2.processing.railDeg()+180)% 360))
        a1tC = self.crossPoint - self.a1point
        a2tC = self.crossPoint - self.a2point
        a1tC_abs = abs(a1tC)
        a2tC_abs = abs(a2tC)
        if a1tC_abs>a2tC_abs:
            c11 = a2tC_abs
        else: 
            c11 = a1tC_abs
        self.newArrow1p = self.crossPoint - ((a1tC.unit())*c11)
        self.newArrow2p = self.crossPoint - ((a2tC.unit())*c11)
        self.line1p = linear.linearFunc()
        self.line1p.point_deg((self.newArrow1p.x, self.newArrow1p.y), 
                             self.arrow1.processing.railDeg()+90)
        self.line2p = linear.linearFunc()
        self.line2p.point_deg((self.newArrow2p.x, self.newArrow2p.y), 
                             self.arrow2.processing.railDeg()+90)
        self.arc_center = linear.point(*(self.line1p & self.line2p))
        self.maxRadius = c11 / math.tan(math.radians(self.arcAngle / 2))
        