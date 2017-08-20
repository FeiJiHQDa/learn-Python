# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 多线程

# import os
#
# print('Pross (%s) start ...' % os.getpid())
#
# pid = os.fork()
#
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


from PIL import Image

im = Image.open('BingWallpaper-2017-08-19.jpg')

w, h = im.size
print('Original image size: %sx%s' % (w, h))

im.thumbnail((w/2, h/2))
print('Resize image to: %sx%s' % (w//2, h//2))

im.save('thumbnail1.jpg')