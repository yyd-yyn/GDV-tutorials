# Exercise #3
# -----------
#
# Show camera video and mirror it.

import numpy as np
import cv2

# Capture webcam image
cap = cv2.VideoCapture(0)

# Get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Codec = " + str(codec))

# Create a window for the video
title = "Video image"
# Note that window parameters have no effect on MacOS
cv2.namedWindow(title, cv2.WINDOW_FREERATIO)
print("Press q to close the window.")

# Start a loop
while True:
    # Read a camera frame
    ret, frame = cap.read()
    # Check if capture was successful
    if ret:
        # Create four flipped tiles of the image
        img = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        img[:height // 2, :width // 2] = smaller_frame  # Top left (original)
        # Bottom left flipped horizontally
        img[height // 2:, :width // 2] = cv2.flip(smaller_frame, 0)
        # Bottom left flipped both horizontally and vertically
        img[height // 2:, width // 2:] = cv2.flip(smaller_frame, -1)
        # Top right flipped vertically
        img[:height // 2, width // 2:] = cv2.flip(smaller_frame, 1)

        # Display the image
        cv2.imshow(title, img)

        # Press q to close the window
        if cv2.waitKey(10) == ord("q"):
            break
    else:
        print("Could not start video camera")
        break

# Release the video capture object and window
cap.release()
cv2.destroyAllWindows()
