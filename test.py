from curve_processing import *
from PIL import Image, ImageDraw, ImageColor
import drawFunc as dF



coordinate_block1 = minecraft_coordinate_real(120, -120)
coordinate_block2 = minecraft_coordinate_real(-100, 40)

dirr = arrowDIR["SOUTHWEST"]

cc = arrow(coordinate_block1, dirr, -90)
cc2 = arrow(coordinate_block2, dirr, 160)

arc1 = arcCurve(cc, cc2)


print(cc)
print(cc2)
print(arc1.line1)
print(arc1.line2)
print(arc1.maxRadius)
print(arc1.Bezier_L)

tp = dF.Bezier.Bezier(0.5, *arc1.Bezier())

d = dF.canvas(600, 600, origin='center')
d.setcenterscale(tp.x, tp.y, 1)
d.drawlinearFunc(arc1.line1, "green")
d.drawlinearFunc(arc1.line2, "green")
d.drawlinearFunc(arc1.line1p, "gray")
d.drawlinearFunc(arc1.line2p, "gray")
#d.drawpoint(arc1.newArrow1p, color="yellow")
#d.drawpoint(arc1.crossPoint, color="red")
#d.drawpoint(arc1.arc_center, color="red")
#d.drawpoint(arc1.newArrow2p, color="yellow")
d.drawArrow(cc, color="black")
d.drawArrow(cc2, color="black")
d.drawBezier(*arc1.Bezier())
#d.drawArc(arc1.arc_center, arc1.maxRadius, arc1.endAngle, arc1.stAngle, fill="None", stroke="red")
d.save_svg("im.svg")

