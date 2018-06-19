from sys import argv
import numpy as np
from skimage.io import imread, imsave

def bindImage():
    # Open multiple images and bind them all
    k = 1
    exported_img = np.zeros((imread(argv[1]).shape[0], imread(argv[1]).shape[1], 1))
    while(k < 3):
        print "Image numero "+str(k)
        img = imread(argv[k], plugin="tifffile")
        print img.shape
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):        
                if img[i,j]!=0:
                    exported_img[i, j] = k
        k+= 1
    imsave(argv[k], exported_img[:,:], plugin="tifffile")

def main():
    bindImage()

if __name__ == "__main__":
    main()
