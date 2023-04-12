# Tutorial #17
# ------------
#
# A demonstration of the OpenCV Simple Blob Detector. Adjust the parameters using sliders. The following OpenCV
# functions are meant to be used in this tutorial:
#
# SimpleBlobDetector (with params) see https://docs.opencv.org/3.4/d0/d7a/classcv_1_1SimpleBlobDetector.html#details
# drawKeypoints see https://docs.opencv.org/3.4/d4/d5d/group__features2d__draw.html#gab958f8900dd10f14316521c149a60433

import cv2
import numpy as np

# TODO Setup SimpleBlobDetector parameters

# TODO Define a function to detect blobs, draw them and display the image
# Determine the used global variables

# Create a detector with the parameters

# Create a greyscale image for the corner detection

# Detect blobs

# Use an image clone to for drawing

# Draw detected blobs as blue circles
# Note that cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size
# Of the circle corresponds to the size of blob.

# Display the image

# TODO Define the callback function

# Provide access to the global blob detector parameters

# Use an image clone to for drawing

# TODO Filter by area

# TODO Change threshold parameters

# TODO Filter by circularity

# TODO Filter by inertia

# TODO Filter by convexity

# Call the detect, draw and show function

# Load example image as color image
img = cv2.imread("./tutorials/data/images/blobtest.jpg", cv2.IMREAD_COLOR)

# TODO Create a window with sliders and show resulting image

# HINT: Create sliders for all parameters using only one callback function

# TODO Call the detect, draw and show function

# TODO Wait until a key is pressed and end the application
