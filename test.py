from curve_processing import *

from PIL import Image, ImageDraw, ImageColor
canvas = (1600, 1200)
scale = 1
thumb = canvas[0]/scale, canvas[1]/scale
im = Image.new('RGBA', canvas, (255, 255, 255, 255))
draw = ImageDraw.Draw(im)
draw.line([(10, 10), (1000, 1000)], width=1, fill=(255, 0, 0))
im.save("im.png")



coordinate_block = minecraft_coordinate_real(5, 7)

dirr = arrowDIR["SOUTHWEST"]

cc = arrow(coordinate_block, dirr, 30)

arc1 = arcCurve(cc, cc, 50)


print(cc)
print(arc1.line1)
