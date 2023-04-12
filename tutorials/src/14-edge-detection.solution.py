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


def on_change(val):
    """callback function for the sliders"""
    # Read slider positions
    blur_slider_pos = cv2.getTrackbarPos("Blur: ", window_name)
    ksize = (blur_slider_pos, blur_slider_pos)
    T_lower = cv2.getTrackbarPos("T_lower: ", window_name)
    T_upper = cv2.getTrackbarPos("T_upper: ", window_name)

    # Blur the image
    img = cv2.blur(img_clone, ksize)

    # Run Canny edge detection with thresholds set by sliders
    canny = cv2.Canny(img, T_lower, T_upper)

    # Show the resulting images in one window
    show_images_side_by_side(img, canny)

    return


# Load example image as grayscale
img = cv2.imread("./tutorials/data/images/nl_clown.jpg", cv2.IMREAD_GRAYSCALE)

# Resize if needed
img = cv2.resize(img, (400, 400))

# Clone if needed
img_clone = np.copy(img)

# Initial Canny edge detection result creation
T_lower = 30
T_upper = 240
canny = cv2.Canny(img, T_lower, T_upper)
# DEBUG: print(cv2.minMaxLoc(canny))

# Define a window name
window_name = "Canny edge detection demo"
# Show the resulting images in one window
show_images_side_by_side(img, canny)
# Create trackbars (sliders) for the window and define one callback function
# note that these calls lead to an assertion error as on_change is called once on creation
cv2.createTrackbar("Blur: ", window_name, 1, 150, on_change)
cv2.createTrackbar("T_lower: ", window_name, 30, 255, on_change)
cv2.createTrackbar("T_upper: ", window_name, 240, 255, on_change)

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
