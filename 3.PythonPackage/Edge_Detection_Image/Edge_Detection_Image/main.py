# Import the necessary Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import argparse
 
def Edge_Detection_Image(image_path): 
    # Read image from disk.
    img = cv2.imread(image_path)
    # Convert BGR image to RGB
    image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Apply Canny edge detection
    edges = cv2.Canny(image= image_rgb, threshold1=100, threshold2=700)
   
    cv2.imwrite('output.jpg',edges)
    
if __name__ == "__main__":  
    parser = argparse.ArgumentParser(description='Detect Edge Of image')
    parser.add_argument('--input', help='Input image path')
    args = parser.parse_args()
    Edge_Detection_Image(args.input)