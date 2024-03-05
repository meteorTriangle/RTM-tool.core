from arrow_position import *
import math


class arcCurve:
    class linearFunc:
        def __init__(self) -> None:  
            ## (y_)y = (x_)x + (const)
            self.x_: float = None
            self.y_: float = None
            self.const: float = None
        def point_deg(self, point: minecraft_coordinate_real, deg: float):
            self.x_ = math.sin(math.radians(deg))
            self.y_ = math.cos(math.radians(deg))
            self.const = (self.y_*point.z) - (self.x_*point.x)
        def __repr__(self) -> str:
            return "{:.2f}y = {:.2f}x + {:.2f}".format(self.y_, self.x_, self.const)
        
        class linearray:
            def __init__(self, point: minecraft_coordinate_real, deg: float) -> None:
                self.sX = point.x
                self.sY = point.z
                self.deg = deg % 360

    def __init__(self, arrow1: arrow, arrow2: arrow, radius: int):
        self.arrow1 = arrow1
        self.arrow2 = arrow2
        self.radius = radius
        self.line1 = self.linearFunc()
        self.line1.point_deg(minecraft_coordinate_real(self.arrow1.processing.x(), self.arrow1.processing.z()), 
                             self.arrow1.processing.railDeg())
