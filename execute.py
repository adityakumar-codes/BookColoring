from PIL import Image, ImageSequence
'''import sys, os
filename = sys.argv[1]
im = Image.open(filename)
original_duration = im.info['duration']
frames = [frame.copy() for frame in ImageSequence.Iterator(im)]    
frames.reverse()

from images2gif import writeGif
writeGif("reverse_" + os.path.basename(filename), frames, duration=original_duration/1000.0, dither=0)'''

import imageio
import cv2
import numpy as np

color = [255,00,255]
img = cv2.imread("sample.png",cv2.IMREAD_COLOR)
[length,breadth,height] = img.shape

frames = []

[page,total] = input("How many pages have you finished reading/total?")
percentage = float(page)/total

for x in range(int(percentage*length),length):
    for y in range(0,breadth):
        img[x][y] = color
    frames.push(img)

frames = [frame.copy() for frame in ImageSequence.Iterator(frames)]     


from images2gif import writeGif
writeGif("reverse_" + os.path.basename(), frames, duration=1000.0, dither=0)

cv2.imwrite("output.png",img)
