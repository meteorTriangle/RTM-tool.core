import math

class linearFunc:
    def __init__(self) -> None:  
        ## (y_)y = (x_)x + (const)
        self.x_: float = None
        self.y_: float = None
        self.const: float = None
    def point_deg(self, point: tuple, deg: float):
        self.x_ = round(math.sin(math.radians(deg)), 7)
        self.y_ = round(math.cos(math.radians(deg)), 7)
        self.const = round((self.y_*point[1]) - (self.x_*point[0]), 7)
    def findX(self, y: int) -> float:
        if self.x_:
            x = ((self.y_ * y) - self.const)/self.x_
        else:
            x = math.inf
        return x
    def findY(self, x: int) -> float:
        if self.y_:
            y = ((self.x_*x) + self.const)/self.y_
        else:
            y = math.inf
        return y
    

class linearFunc(linearFunc):
    def __len__(self: linearFunc) -> int:
        return 7
    def __repr__(self) -> str:
        return "{:.2f}y = {:.2f}x + {:.2f}".format(self.y_, self.x_, self.const)
    def __and__(self, o: linearFunc) -> tuple[int, int]:
        __A1 = -self.x_
        __B1 =  self.y_
        __C1 =  self.const
        __A2 = -o.x_
        __B2 =  o.y_
        __C2 =  o.const
        delta = __A1*__B2 - __A2*__B1
        deltaX = __C1*__B2 - __C2*__B1
        deltaY = __A1*__C2 - __A2*__C1
        if delta == 0:
            if (deltaX+deltaY)==0:
                return (math.inf, math.inf)
            else:
                return(math.inf, 0)
        else:
            Xr = round(deltaX / delta, 7)
            Yr = round(deltaY / delta, 7)
            return (Xr, Yr)

class point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __add__(self, o):
        if type(o) == vector:
            return point(self.x + o.x, self.y + o.y)
    def __sub__(self, o):
        if type(o) == vector:
            return point(self.x - o.x, self.y - o.y)
        if type(o) == point:
            return vector(self.x - o.x, self.y - o.y)
        pass
    def __repr__(self) -> str:
        return "({:n}, {:n})".format(self.x, self.y)


class vector:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)
    def __abs__(self)->float:
        return math.sqrt(self.x**2 + self.y**2)
    def __neg__(self):
        return vector(-self.x, -self.y)
    def __floordiv__(self, o):
        return self.div(o)
    def __truediv__(self, o):
        return self.div(o)
    def div(self, o):
        if(type(o) == float):
            return vector(self.x / o, self.y / o)
    def unit(self):
        return  (self / abs(self))
    def __mul__(self, o):
        if type(o) == float:
            return vector(self.x * o, self.y * o)
    def __repr__(self) -> str:
        return "({:n}, {:n})".format(self.x, self.y)