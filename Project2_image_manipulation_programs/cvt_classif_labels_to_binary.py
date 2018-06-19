from osgeo import gdal
import numpy as np
from sys import argv

def main():
    print "Reading data...",
    ds = gdal.Open(argv[1])
    band = ds.GetRasterBand(1)
    img = band.ReadAsArray()
    print "Done"
    print "Converting to binary...",
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] == 2 :
                img[i, j] = 1
            elif img[i, j] == 1 :
                img[i, j] = 0
    print "Done"
    print "Saving image",
    ####Save Image:
    driver = gdal.GetDriverByName("GTiff")
    dataset_expo = driver.Create(argv[2], img.shape[0], img.shape[1], 1, eType=gdal.GDT_Float32)
    _ = dataset_expo.GetRasterBand(1).WriteArray(img[:, :])
    dataset_expo.FlushCache()              # write to disk
    dataset_expo = None
    print "done."
    
if __name__ == "__main__":
    main()