#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter

#  jpg :
im = Image.open('test.jpg')
#  :
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
