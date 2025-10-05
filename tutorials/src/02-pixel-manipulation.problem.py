# Exercise #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of 
# the image to some other place, count the used colors in the image

import cv2
import numpy as np # we will need numpy for some array manipulations

# TODO Loading images in grey and color and store them in the variables 'img_gray' and 'img_color'.

# TODO Check if images have been loaded successfully.

## Image data access

# TODO Do some print out about the loaded data using 'type', 'dtype' and 'shape'.

# TODO Continue with the grayscale image by copying it to a new variable 'img'.

# TODO Extract the size or resolution of this image.

## This is how you can access the height and width of an image stored as a numpy ndarray. 
## In all following exercises you should use this way to access the height and width of an image.
## Then, you can use the variables 'height' and 'width' in your code instead of hardcoding values. 
## This makes your code flexible and independent from the actual image size.

# TODO Resize the image to a small size (7x5) as we will later print out the pixel values.

# HINT: Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for 
# general access on ndarrays

# TODO Print first row

# TODO Print first column

# TODO Now continue with the color image by copying it to the variable 'img'.

# TODO Set an area of the image to black by looping over the pixels and setting the pixel values to [0,0,0].

# TODO Create a window with 'namedWindow' and show the image and wait until key pressed.

# TODO Find all used colors in the image by first reshaping the image to a list of pixels with 'reshape' 
# (which is a numpy function that can be applied to images as they are stored as 'ndarrays').

# TODO Use 'np.unique' to find all unique colors in the reshaped image. Use the parameter 'axis=0' to
# search for unique rows (pixels) instead of unique single values.

# TODO Copy one part of an image into another one by first defining a region of interest (ROI) and then storing 
# the data in a temporal variable before copying it to another part of the image.

# TODO Save the image to a file using 'imwrite'.

# TODO Load the image again and show it in a window.

# TODO Show the original image in another window to illustrate the effect of the copy operation. Check
# if you have used 'copy' or if you just stored a reference to the original image using the '=' operator.
