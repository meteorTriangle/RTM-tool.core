from curve_processing import *
import drawsvg as draw
from PIL import Image, ImageDraw, ImageColor

d = draw.Drawing(200, 300, origin='center')
d.append(draw.Line(10, -50, -80, -50, stroke="red", stroke_width=5))
d.save_svg("im.svg")

coordinate_block = minecraft_coordinate_real(5, 7)

dirr = arrowDIR["SOUTHWEST"]

cc = arrow(coordinate_block, dirr, 30)

arc1 = arcCurve(cc, cc, 50)


print(cc)
print(arc1.line1)
