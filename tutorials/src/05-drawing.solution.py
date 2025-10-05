# Exercise #5
# -----------
#
# Create a white image and draw something on it.

import cv2
import numpy as np

# Create a white image
width, height = 625, 512
img = np.ones((height, width, 3), np.uint8) * 255

## Drawing helper variables
# Thickness
thick = 10
thin = 3

# Colors in BGR (which is used by default in OpenCV)
blue = (255, 0, 0)
red = (0, 0, 255)
darkgreen = (20, 200, 20)
black = (0, 0, 0)

# Fonts
font_size_large = 3
font_size_small = 1
font = cv2.FONT_HERSHEY_SIMPLEX

# Display the image
cv2.namedWindow("Drawing image")


# Draw a green diagonal cross over the image
img = cv2.line(img, (0, 0), (width, height), darkgreen, thick)
img = cv2.line(img, (0, height), (width, 0), darkgreen, thick)

# Draw a circle
img = cv2.circle(img, (width - 40, 40), 20, red, cv2.FILLED, cv2.LINE_4)

# Write some text
img = cv2.putText(img, "Hello World!", (10, height - 10), font, font_size_large, black, thick)

# Draw arrows (potential assignment)
img = cv2.arrowedLine(img, (10, 10), (100, 10), blue, thin)
img = cv2.putText(img, "X", (115, 25), font, font_size_small, blue, thin)
img = cv2.arrowedLine(img, (10, 10), (10, 100), blue, thin)
img = cv2.putText(img, "Y", (5, 130), font, font_size_small, blue, thin)

# Display the image
cv2.imshow("Drawing image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
