# Tutorial #10
# ------------
#
# Doing the Fourier Transform for images and back. This code is based on the stackoverflow answer from Fred Weinhaus:
# https://stackoverflow.com/a/59995542

import cv2
import numpy as np

# Global helper variables
window_width = 640
window_height = 480

# TODO Implement the function get_frequencies(image):
# Convert image to floats and do dft saving as complex output

# Apply shift of origin from upper left corner to center of image

# Extract magnitude and phase images

# Get spectrum for viewing only

# Return the resulting image (as well as the magnitude and phase for the inverse)

# TODO Implement the function create_from_spectrum():
# Convert magnitude and phase into cartesian real and imaginary components

# Combine cartesian components into one complex image

# Shift origin from center to upper left corner

# Do idft saving as complex output

# Combine complex components into original image again

# Re-normalize to 8-bits


# We use a main function this time: see https://realpython.com/python-main-function/ why it makes sense
def main():
    # Load an image, compute frequency domain image from it and display both or vice versa
    image_name = "./exercises/data/images/chewing_gum_balls01.jpg"

    # Load the image.
    image = cv2.imread(image_name, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (window_width, window_height))

    # Show the original image
    # Note that window parameters have no effect on MacOS
    title_original = "Original image"
    cv2.namedWindow(title_original, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_original, window_width, window_height)
    cv2.imshow(title_original, image)

    # result = get_frequencies(image)
    result = np.zeros((window_height, window_width), np.uint8)

    # Show the resulting image
    # Note that window parameters have no effect on MacOS
    title_result = "Frequencies image"
    cv2.namedWindow(title_result, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_result, window_width, window_height)
    cv2.imshow(title_result, result)

    # back = create_from_spectrum(??)
    back = np.zeros((window_height, window_width), np.uint8)

    # And compute image back from frequencies
    # Note that window parameters have no effect on MacOS
    title_back = "Reconstructed image"
    cv2.namedWindow(title_back, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(title_back, window_width, window_height)
    cv2.imshow(title_back, back)

    key = cv2.waitKey(0)
    cv2.destroyAllWindows()


# Starting the main function
if __name__ == "__main__":
    main()
