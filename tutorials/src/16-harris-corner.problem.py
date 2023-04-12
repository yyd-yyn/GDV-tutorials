# Tutorial #16
# ------------
#
# Compute the Harris corner response image and detect isolated corners with non-maximum suppression. Inspired by
# https://docs.opencv.org/4.5.3/dc/d0d/tutorial_py_features_harris.html

import numpy as np
import cv2


# Display two images side by side
def show_images_side_by_side(img_A, img_B):
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


# TODO Do a non-maximum suppression
def do_non_maxima_suppression(img, window_size):
    # Loop over each pixel in the image and keep pixel only if
    # it is maximal in a window with window_size
    foo = 0  # TODO Remove this line (it is just here that the script is running)


# Load example image
img = cv2.imread("./tutorials/data/images/chessboard-contrast-squares.jpg", cv2.IMREAD_COLOR)
# Resize if needed
img = cv2.resize(img, None, fx=0.1, fy=0.1)

# Define parameters for Harris corner detection
block_size = 2
ksize = 3
k = 0.04
# TODO Create a greyscale image for the corner detection

# TODO Convert to floating point image

# TODO Harris corner detection using OpenCV method cornerHarris

# TODO Run non-maximum suppression to find isolated corner points

# TODO Dilate resulting image for increasing the corner size so that
# they become more visible than a single pixel

# TODO Threshold for an optimal value, it may vary depending on the image
# and set corner pixels in the original image to a distinct color
# HINT: use something like "img[corner_img > threshold] = color" instead
# of a draw function to keep it simple

# Create window
window_name = "Corner demo"
cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)

# Show resulting images
# TODO Replace second image with the corner response image
show_images_side_by_side(img, img)

# Wait for key to be pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
