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
        self.line1 = linear.linearFunc()
        self.line1.point_deg((self.arrow1.processing.x(), self.arrow1.processing.z()), 
                             self.arrow1.processing.railDeg())
        self.line2 = linear.linearFunc()
        self.line2.point_deg((self.arrow2.processing.x(), self.arrow2.processing.z()), 
                             self.arrow2.processing.railDeg())