# https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
import os, sys
from PIL import Image
import glob

size = 200, 200

images = glob.glob("/Users/jamesmccrory/documents/dev/pinterest_dataset/images/*.jpg")
for img in images:
    with open(img, 'rb') as file:
        outfile = os.path.splitext(file.name)[0] + ".png"
        im = Image.open(file)
        im = im.resize(size)#, Image.ANTIALIAS)
        im.save(outfile, "PNG")
