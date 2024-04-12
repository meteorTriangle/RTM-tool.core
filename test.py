from curve_processing import *
from PIL import Image, ImageDraw, ImageColor
import drawFunc as dF


d = dF.canvas(600, 600, origin='center')
d.setcenterscale(0, 0, 2)

coordinate_block1 = minecraft_coordinate_real(120, -40)
coordinate_block2 = minecraft_coordinate_real(12, 10)

dirr = arrowDIR["SOUTHWEST"]

cc = arrow(coordinate_block1, dirr, -90)
cc2 = arrow(coordinate_block2, dirr, 135)

arc1 = arcCurve(cc, cc2, 50)


print(cc)
print(cc2)
print(arc1.line1)
print(arc1.line2)
print(arc1.crossPoint)
print(arc1.arcAngle)
print(arc1.stAngle)
print(arc1.endAngle)

X0 = linear.point(150, 150)
X1 = linear.point(-50, 150)
X2 = linear.point(-150, 50)
X3 = linear.point(-150, -150)

d.drawlinearFunc(arc1.line1, "red")
d.drawlinearFunc(arc1.line2, "red")
d.drawlinearFunc(arc1.line1p, "gray")
d.drawlinearFunc(arc1.line2p, "gray")
d.drawpoint(arc1.newArrow1p, color="yellow")
d.drawpoint(arc1.crossPoint, color="red")
d.drawpoint(arc1.newArrow2p, color="yellow")
d.drawArrow(cc, color="black")
d.drawArrow(cc2, color="black")
d.drawBezier(X0, X1, X2, X3)
d.save_svg("im.svg")

