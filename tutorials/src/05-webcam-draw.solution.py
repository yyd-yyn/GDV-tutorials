# Exercise #5
# -----------
#
# Use the webcam image stream and draw something on it. Animate one of the drawings.
#
# Note that the solution uses the "map" function. Check this tutorial
# (https://www.learnpython.org/en/Map%2C_Filter%2C_Reduce) if you are
# not familiar with map paradigm from functional programming.

import cv2
import math
import operator

# Capture webcam image
cap = cv2.VideoCapture(0)

# Get camera image parameters from get()
width = int(cap.get(cv2.cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.cv2.CAP_PROP_CODEC_PIXEL_FORMAT))

print("Video properties:")
print("  Width = " + str(width))
print("  Height = " + str(height))
print("  Codec = " + str(codec))

# Drawing helper variables
# Thickness
thick = 10
thin = 3

# Color
blue = (255, 0, 0)
red = (0, 0, 255)
green = (20, 200, 20)
black = (0, 0, 0)

# Fonts
font_size_large = 3
font_size_small = 1
font = cv2.FONT_HERSHEY_SIMPLEX


# Function and timer variable for the moving rectangle
def circle_path(t, scale, offset):
    res = (int(scale * math.cos(t) + offset), int(scale * math.sin(t) + offset))
    return res


timer = 0.0

while True:
    # Capture the image
    ret, img = cap.read()

    # Check if capture succeeded
    if ret:
        # Draw a green diagonal cross over the image
        img = cv2.line(img, (0, 0), (width, height), green, thick)
        img = cv2.line(img, (0, height), (width, 0), green, thick)

        # Draw a circle
        img = cv2.circle(img, (width - 40, 40), 20, red, cv2.FILLED, cv2.LINE_4)

        # Write some text
        img = cv2.putText(img, "Hello World!", (10, height - 10), font, font_size_large, black, thick)

        # Draw arrows (potential assignment)
        img = cv2.arrowedLine(img, (10, 10), (100, 10), blue, thin)
        img = cv2.putText(img, "X", (115, 25), font, font_size_small, blue, thin)
        img = cv2.arrowedLine(img, (10, 10), (10, 100), blue, thin)
        img = cv2.putText(img, "Y", (5, 130), font, font_size_small, blue, thin)

        # Draw a rectangle that moves on a circular path
        timer += 0.1
        pt1 = circle_path(timer, 100, 300)
        size = (20, 20)
        pt2 = tuple(map(operator.add, pt1, size))
        img = cv2.rectangle(img, pt1, pt2, red, thin)

        # Display the image
        cv2.imshow("Video image", img)

        # Press q to close the window
        if cv2.waitKey(10) == ord("q"):
            break
    else:
        print("Could not start video camera")
        break

# Release the video capture object and window
cap.release()
cv2.destroyAllWindows()
