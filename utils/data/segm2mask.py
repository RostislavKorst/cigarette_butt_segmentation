from PIL import Image, ImageDraw
import numpy as np


def segm2mask(segm_list):
    x_list = list()
    y_list = list()

    for index, coord in enumerate(segm_list):
        if index % 2:
            y_list.append(coord)
        else:
            x_list.append(coord)

    polygon = list(zip(x_list, y_list))

    im = Image.new('1', (512, 512))
    draw = ImageDraw.Draw(im)
    draw.polygon(polygon, fill="green", outline=None)

    mask = np.array(im, dtype=int)

    return mask
