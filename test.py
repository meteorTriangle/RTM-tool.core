from curve_processing import *
from PIL import Image, ImageDraw, ImageColor
import drawFunc as dF


d = dF.canvas(300, 300, origin='center')
d.setcenterscale(0, 0, 1)

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

d.drawlinearFunc(arc1.line1, "red")
d.drawlinearFunc(arc1.line2, "red")
d.drawlinearFunc(arc1.line1p, "gray")
d.drawlinearFunc(arc1.line2p, "gray")
d.drawpoint(arc1.newArrow1p, color="yellow")
d.drawpoint(arc1.crossPoint, color="red")
d.drawpoint(arc1.newArrow2p, color="yellow")
d.drawArrow(cc, color="black")
d.drawArrow(cc2, color="black")
d.save_svg("im.svg")

