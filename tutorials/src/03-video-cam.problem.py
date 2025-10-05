# Exercise #3
# -----------
#
# Show camera video and mirror it.

import numpy as np
import cv2

# TODO Capture webcam image using 'VideoCapture' and store it in the variable 'cap'. Typically, 
# the parameter is 0 for the default camera.

# TODO Get camera image parameters using 'get' on the 'cap' object:
# - width (use 'CAP_PROP_FRAME_WIDTH')
# - height (use 'CAP_PROP_FRAME_HEIGHT')
# - codec (use 'CAP_PROP_CODEC_PIXEL_FORMAT')
# Print the values to the console.

# TODO Create a window for the video using 'namedWindow' with the title "Video image".

# TODO Start a loop to continuously read frames from the camera using 'while True:'.

# TODO (In loop) Read a camera frame with 'read' and check if that was successful.

# TODO (In loop, if successful) (Skip this step for now and implement the display first in order 
# to see the camera image.)
# Create four flipped tiles of the image by first creating an empty image 
# with 'np.zeros'. Then resize the frame to half size using 'cv2.resize' with fx=0.5 and fy=0.5.
# Finally, fill in the four quadrants of the empty image with the original and flipped images
# using 'cv2.flip' with the appropriate flip codes (check the documentation).

# TODO (In loop, if successful) Display the image.

# TODO (In loop) Check if 'q' is pressed by comparing the return value of 'waitKey' with the 'ord'
# of the letter "q". Use simply 'break' to exit the loop.

# TODO Release the video capture object with 'release' and close the window with 'destroyAllWindows'.
