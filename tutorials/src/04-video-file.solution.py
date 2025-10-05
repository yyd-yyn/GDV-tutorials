# Exercise #4
# -----------
#
# Loading a video file and mirror it.

import numpy as np
import cv2

# Open a video file
file = "./tutorials/data/videos/hello_UH.m4v"
cap = cv2.VideoCapture(file)

# Get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Frame count = " + str(count))

# Create a window for the video
title = "Video image"
# Note that window parameters have no effect on MacOS
cv2.namedWindow(title, cv2.WINDOW_FREERATIO)
print("Press q to close the window.")

# Start a loop
while True:
    # Read one video frame
    ret, frame = cap.read()

    if ret:
        # Create four tiles of the image
        img = np.zeros(frame.shape, np.uint8)
        smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        img[:height // 2, :width // 2] = smaller_frame  # Top left (original)
        # Bottom left flipped horizontally
        img[height // 2:, :width // 2] = cv2.flip(smaller_frame, 0)
        # Bottom left flipped both horizontally and vertically
        img[height // 2:, width // 2:] = cv2.flip(smaller_frame, -1)
        # Top right flipped vertically
        img[:height // 2, width // 2:] = cv2.flip(smaller_frame, 1)

        # Show the image
        cv2.imshow(title, img)

        # Close the window and stop the loop if 'q' is pressed
        if cv2.waitKey(10) == ord("q"):
            break
    else:
        print("Error reading frame")
        break

# Release the video and close all windows
cap.release()
cv2.destroyAllWindows()
