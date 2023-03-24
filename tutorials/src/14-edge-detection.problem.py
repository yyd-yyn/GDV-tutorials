# Tutorial #14
# ------------
#
# Compute the edges of an image with the Canny edge detection. Adjust the parameters using sliders.

import numpy as np
import cv2


def show_images_side_by_side(img_A, img_B):
    """Helper function to draw two images side by side"""
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))
    return


# TODO: Define callback function
"""callback function for the sliders"""
# Read slider positions

# Blur the image

# Run Canny edge detection with thresholds set by sliders

# Show the resulting images in one window using the show_images_side_by_side function

# TODO Load example image as grayscale

# Resize if needed

# Clone if needed

# TODO Initial Canny edge detection result creation

# TODO Create window with sliders
# Define a window name
window_name = "Canny edge detection demo"
# TODO Show the resulting images in one window

# TODO Create trackbars (sliders) for the window and define one callback function

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
