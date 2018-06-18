from sys import argv
import cv2
import numpy as np

img = cv2.imread(argv[1], 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow('Edges', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()