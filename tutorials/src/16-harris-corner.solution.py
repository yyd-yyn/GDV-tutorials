# Tutorial #16
# ------------
#
# Compute the Harris corner response image and detect isolated corners with non-maximum suppression. Inspired by
# https://docs.opencv.org/4.x/dc/d0d/tutorial_py_features_harris.html

import numpy as np
import cv2


# Display two images side by side
def show_images_side_by_side(img_A, img_B):
    cv2.imshow(window_name, np.concatenate((img_A, img_B), axis=1))


# Do a non-maximum suppression
def do_non_maxima_suppression(img, window_size):
    # Loop over each pixel in the image and keep pixel only if
    # it is maximal in a window with kernel_size
    h, w = img.shape
    result = np.zeros((h, w), np.uint8)
    offset = int((window_size - 1) / 2)

    for y in range(offset, h - 1 - offset):
        for x in range(offset, w - 1 - offset):
            window = img[y - offset:y + 1 + offset, x - offset:x + 1 + offset]
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(window)
            if max_loc == (offset, offset):
                result[y, x] = img[y, x]

    return result


# Load example image
img = cv2.imread("./tutorials/data/images/chessboard-contrast-squares.jpg", cv2.IMREAD_COLOR)

# Resize if needed
img = cv2.resize(img, None, fx=0.1, fy=0.1)

# Define parameters for Harris corner detection
block_size = 2
ksize = 3
k = 0.04

# Create a greyscale image for the corner detection
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Convert to floating point image
img_float = np.float32(img_gray)

# Harris corner detection using OpenCV method cornerHarris
harris_corner_img = cv2.cornerHarris(img_float, block_size, ksize, k)

# Run non-maximum suppression to find isolated corner points
img_suppressed = do_non_maxima_suppression(harris_corner_img, 5)

# Resulting image is dilated for increasing the corner size so that
# they become more visible than a single pixel
img_dilated = cv2.dilate(img_suppressed, None)

# Threshold for an optimal value, it may vary depending on the image and set
# corner pixels in the original image to a distinct color
img[img_dilated > 0.01 * img_dilated.max()] = [0, 0, 255]

# Create window
window_name = "Corner demo"
cv2.namedWindow(window_name, cv2.WINDOW_GUI_NORMAL)

# Show resulting images
show_images_side_by_side(img, cv2.cvtColor(img_suppressed, cv2.COLOR_GRAY2BGR))

# Wait for key to be pressed and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()
