from sys import argv
from osgeo import gdal

def cvtRGB2Gray(r, g, b):
    gray = (0.299*r + 0.587*g + 0.114*b)
    return gray

def main():
    dataset = gdal.Open(argv[1])
    
    band1 = dataset.GetRasterBand(1)
    r = band1.ReadAsArray()
    
    band2 = dataset.GetRasterBand(2)
    g = band2.ReadAsArray()
    
    band3 = dataset.GetRasterBand(3)
    b = band3.ReadAsArray()
    
    #Convert_img_to_gray
    img_gray = cvtRGB2Gray(r, g, b)
    driver = gdal.GetDriverByName('GTiff')
    x_size = r.shape[1]
    y_size = r.shape[0]
    dataset = driver.Create(argv[2], x_size, y_size, eType=gdal.GDT_Float32)
    _ = dataset.GetRasterBand(1).WriteArray(img_gray)
if __name__ == "__main__":
    main()