from sys import argv
from skimage.io import imread, imsave
import numpy as np

def main():
    img = imread(argv[1])
    values = np.unique(img) 
    l = len(values)
    img_exported = np.zeros((img.shape[0], img.shape[1], l), dtype='uint8')
    for k in values:
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i,j] == k:
                    img_exported[i, j, k] = img[i, j]
    for k in values:
        imsave('im_SPOT6_classe_'+str(k)+'.tif', img_exported[:,:, k], plugin='tifffile')
if __name__ == "__main__":
    main()