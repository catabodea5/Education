import glob
import cv2
img=cv2.imread
import numpy as np
from PIL import Image

from skimage.io import imread
import numpy as np
inputs=[]
outputs=[]
width=50;
height=50;
for f in glob.glob("D:/Facultate/An2/Sem2/AI/lab100/databasesepia/training_set/normal/*.jpg"):
    image = imread(f)
    print(image)

