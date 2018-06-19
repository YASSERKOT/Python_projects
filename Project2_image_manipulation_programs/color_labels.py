from sys import argv
import numpy as np
from skimage.io import imread, imsave
import cv2

def change_color(img):
    img_color = cv2.applyColorMap(img, cv2.COLORMAP_JET)
    return img_color

def main():
    img = imread(argv[1], cv2.IMREAD_GRAYSCALE)
    print img.shape
    img_color = change_color(img)
    imsave(argv[2], img_color, plugin='tifffile')

if __name__ == "__main__":
    main()