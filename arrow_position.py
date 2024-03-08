from typing import Any


class minecraft_coordinate_real:
    def __init__(self, x, z) -> None:
        self.x:float = float(x)
        self.z:float = float(z)
    def __add__(self, o):
        new = minecraft_coordinate_real(self.x + o.x, self.z + o.z)
        return new
    def __sub__(self, o):
        new = minecraft_coordinate_real(self.x - o.x, self.z - o.z)
        return new
    def __repr__(self) -> str:
        return "X: {:.2f}  Z: {:.2f}".format(self.x, self.z)
    def tuple(self, inverse = 1) -> tuple:
        return (self.x, self.z* inverse)

arrowDIR = {
    "NORTH"     : int(0),
    "SOUTH"     : int(1),
    "EAST"      : int(2),
    "WEST"      : int(3),
    "NORTHEAST" : int(4),
    "NORTHWEST" : int(5),
    "SOUTHEAST" : int(6),
    "SOUTHWEST" : int(7),
}

class arrow:
    class __coor:
        def __init__(self, x, z, deg, rail_deg):
            self.__x = x
            self.__z = z
            self.__deg = deg % 360
            self.__railDeg = rail_deg % 360
        def x(self):
            return self.__x
        def z(self):
            return self.__z
        def deg(self):
            return self.__deg
        def railDeg(self):
            return self.__railDeg
        def __call__(self) -> Any:
            return self.__dict__
        def tuple(self) -> tuple:
            return (self.__x, self.__z)
        

    def __init__(self, block_coordinate:minecraft_coordinate_real, DIR:int, rail_dir:float) -> None:
        arrow_deg_conv = [
            int(180),
            int(0),
            int(-90),
            int(90),
            int(-135),
            int(135),
            int(-45),
            int(45),
        ]
        arrowDIR__ = [
            minecraft_coordinate_real( 0  , 0.5),
            minecraft_coordinate_real( 0  ,-0.5),
            minecraft_coordinate_real(-0.5, 0  ),
            minecraft_coordinate_real( 0.5, 0  ),
            minecraft_coordinate_real(-0.5, 0.5),
            minecraft_coordinate_real( 0.5, 0.5),
            minecraft_coordinate_real(-0.5,-0.5),
            minecraft_coordinate_real( 0.5,-0.5),
        ]
        self.block_center = block_coordinate + minecraft_coordinate_real(0.5, 0.5) + arrowDIR__[DIR]
        self.minecraft = self.__coor(self.block_center.x, self.block_center.z, arrow_deg_conv[DIR], rail_dir)
        self.processing = self.__coor(self.block_center.x, -(self.block_center.z), (arrow_deg_conv[DIR]-90), (rail_dir-90))

    def __repr__(self) -> str:
        l1 = "Minecraft  coordinate:  X:{:10.1f}  Z:{:10.1f}  deg:{:7.2f}  railDeg:{:7.2f}\n".format(self.minecraft.x(), self.minecraft.z(), self.minecraft.deg(), self.minecraft.railDeg())
        l2 = "Processing coordinate:  X:{:10.1f}  Z:{:10.1f}  deg:{:7.2f}  railDeg:{:7.2f}".format(self.processing.x(), self.processing.z(), self.processing.deg(), self.processing.railDeg())
        
        return l1 + l2