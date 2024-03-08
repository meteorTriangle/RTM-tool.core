import drawsvg as draw
import linearCore.linear as linear

class canvas(draw.Drawing):
    def setcenterscale(self, x, y, scale):
        self.offsetX = x
        self.offsetY = y
        self.offsetScale = scale
    def drawlinearFunc(self, Func: linear.linearFunc, color):
        self.__initcenter()
        self.Xp = ((self.width /self.offsetScale) / 2  ) + self.offsetX
        self.Xm = ((self.width /self.offsetScale) / -2 ) + self.offsetX
        self.Yp = ((self.height/self.offsetScale) / 2 ) + self.offsetY
        self.Ym = ((self.height/self.offsetScale) / -2) + self.offsetY
        self.crossPoint = [
            [self.Xp, Func.findY(self.Xp)],
            [self.Xm, Func.findY(self.Xm)],
            [Func.findX(self.Yp), self.Yp],
            [Func.findX(self.Ym), self.Ym],
            ]
        dis = []
        for i in range(4):
            coor = self.crossPoint[i]
            dis.append(pow(pow(coor[0] - self.offsetX, 2) + pow(coor[1] - self.offsetY, 2), 0.5))
        mp1 = min(dis)
        mp1i = dis.index(mp1)
        mp1c = self.crossPoint[mp1i]
        mp1c = [(mp1c[0]  - self.offsetX)* self.offsetScale, -(mp1c[1]  - self.offsetY)* self.offsetScale]
        dis.pop(mp1i)
        self.crossPoint.pop(mp1i)
        
        mp2 = min(dis)
        mp2i = dis.index(mp2)
        mp2c = self.crossPoint[mp2i]
        mp2c = [(mp2c[0]  - self.offsetX)* self.offsetScale, -(mp2c[1]  - self.offsetY)* self.offsetScale]
        self.append(draw.Line(*mp1c, *mp2c, stroke=color, stroke_width=2))
    
    def __initcenter(self):
        if self.offsetX != None:
            pass
        else:
            self.setcenterscale(0, 0, 1)
    def drawpoint(self, point: tuple[int, int], color= "black"):
        point_ = [(point[0]  - self.offsetX)* self.offsetScale, -(point[1]  - self.offsetY)* self.offsetScale]
        self.append(draw.Circle(*point_, 5*self.offsetScale, fill=color))