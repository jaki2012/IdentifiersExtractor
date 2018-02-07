#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image

#  jpg :
im = Image.open('test.jpg')
#  :
w, h = im.size
print('Original image size: %sx%s' % (w, h))
#  50%:
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
#  jpeg :
im.save('thumbnail.jpg', 'jpeg')
