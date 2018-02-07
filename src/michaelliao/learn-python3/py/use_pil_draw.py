#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random

#  :
def rndChar():
    return chr(random.randint(65, 90))

#  1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

#  2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
#  Font :
font = ImageFont.truetype('Arial.ttf', 36)
#  Draw :
draw = ImageDraw.Draw(image)
#  :
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
#  :
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
#  :
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
