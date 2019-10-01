# https://stackoverflow.com/questions/9506841/using-python-pil-to-turn-a-rgb-image-into-a-pure-black-and-white-image

import os, sys
from PIL import Image
import glob

images = glob.glob("/Users/jamesmccrory/documents/dev/pinterest_dataset/images copy/*.png")
for img in images:
    with open(img, 'rb') as file:
        outfile = os.path.splitext(file.name)[0] + ".jpg"
        file_parts = outfile.split('/')
        outfile = "/".join(file_parts[:-1]) + "/BW" + file_parts[-1]
        # print(outfile)
        # break
        im = Image.open(file)
        im = im.convert('1') # convert image to black and white
        im.save(outfile, "PNG")
