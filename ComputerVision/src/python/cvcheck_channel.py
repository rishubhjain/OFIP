import cv2
import numpy as np

def check_channel(image):
    if len(image.shape)==2:
        x=2
    elif len(image.shape)==3:
        x=3
    
   
    return x
