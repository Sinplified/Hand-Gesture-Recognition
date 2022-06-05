import numpy as np
import cv2
def func(path):
    frame = cv2.imread(path)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),2)
    canny = cv2.Canny(blur,0,35)
    
    return canny