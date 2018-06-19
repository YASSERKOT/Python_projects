from osgeo import gdal
import numpy as np
from sys import argv

def main():
    img_adr1 = argv[1]
    img_adr2 = argv[2]
    export_adr = argv[3]
    
    ds1 = gdal.Open(img_adr1)
    ds2 = gdal.Open(img_adr1)

    img1 = np.zeros((ds1.GetRasterBand(1).ReadAsArray().shape[0], ds1.GetRasterBand(1).ReadAsArray().shape[1], ds1.RasterCount))
    img2 = np.zeros((ds2.GetRasterBand(1).ReadAsArray().shape[0], ds2.GetRasterBand(1).ReadAsArray().shape[1], ds2.RasterCount))
    
    for k in range(ds1.RasterCount):
        band = ds1.GetRasterBand(k+1)
        ds = band.ReadAsArray()
        img1[:, :, k] = ds
    
    for k in range(ds2.RasterCount):
        band = ds2.GetRasterBand(k+1)
        ds = band.ReadAsArray()
        img2[:, :, k] = ds
    
    exported_img = np.zeros((2100, 2100, 6))
    diff = img1.shape[0] - img2.shape[0]
    print "ecart is "+ str(diff)
    print img1.shape
    print img2.shape
    for i in range(2100):
        for j in range(2100):
            for k in range(6):
                    if (i > diff/2) and (i < 2100-diff/2) and (j > diff/2) and (j < 2100-diff/2):
                        exported_img[i, j, k] = img2[i-diff/2, j-diff/2, k]
                            
    print "Saving image",
    ####Save Image:
    driver = gdal.GetDriverByName("GTiff")
    x_size = img1.shape[0]
    y_size = img1.shape[1]
    dataset_expo = driver.Create(export_adr, x_size, y_size, 6, eType=gdal.GDT_Float32)
    _ = dataset_expo.GetRasterBand(1).WriteArray(exported_img[:, :, 0])
    _ = dataset_expo.GetRasterBand(2).WriteArray(exported_img[:, :, 1])
    _ = dataset_expo.GetRasterBand(3).WriteArray(exported_img[:, :, 2])
    _ = dataset_expo.GetRasterBand(4).WriteArray(exported_img[:, :, 3])    
    _ = dataset_expo.GetRasterBand(5).WriteArray(exported_img[:, :, 4])
    _ = dataset_expo.GetRasterBand(6).WriteArray(exported_img[:, :, 5])
    dataset_expo.FlushCache()              # write to disk
    dataset_expo = None
    print "done."
    
if __name__ == "__main__":
    main()
