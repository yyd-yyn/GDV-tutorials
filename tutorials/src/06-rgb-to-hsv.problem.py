# Tutorial #6
# -----------
#
# Playing around with colors. We convert some values from RGB to HSV and then find colored objects in the image and mask
# them out. Includes a color picker on double-click now. The RGB version is meant to demonstrate that this does not work
# in RGB color space.

import numpy as np
import cv2

# Print keyboard usage
print("This is a HSV color detection demo. Use the keys to adjust the \
selection color in HSV space. Circle in bottom left.")
print("The masked image shows only the pixels with the given HSV color within \
a given range.")
print("Use h/H to de-/increase the hue.")
print("Use s/S to de-/increase the saturation.")
print("Use v/V to de-/increase the (brightness) value.\n")
print("Double-click an image pixel to select its color for masking.")

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

# Drawing helper variables
thick = 10
thin = 3
thinner = 2
font_size_large = 3
font_size_small = 1
font_size_smaller = 0.6
font = cv2.FONT_HERSHEY_SIMPLEX

# TODO Define  RGB colors as variables

# Exemplary color conversion (only for the class), tests usage of cv2.cvtColor

# TODO Enter some default values and uncomment
# hue =
hue_range = 10
# saturation =
saturation_range = 100
# value =
value_range = 100


# Callback to pick the color on double click
def color_picker(event, x, y, flags, param):
    global hue, saturation, value
    if event == cv2.EVENT_LBUTTONDBLCLK:
        (h, s, v) = hsv[y, x]
        hue = int(h)
        saturation = int(s)
        value = int(v)
        print("New color selected:", (hue, saturation, value))


while True:
    # Get video frame (always BGR format!)
    ret, frame = cap.read()
    if ret:
        # Copy image to draw on
        img = frame.copy()

        # TODO Compute color ranges for display

        # TODO Draw selection color circle and text for HSV values

        # TODO Convert to HSV
        hsv = "TODO: replace this with the conversion code"

        # TODO Create a bitwise mask

        # TODO Apply mask

        # TODO Show the original image with drawings in one window

        # TODO Show the masked image in another window

        # TODO Show the mask image in another window

        # TODO Deal with keyboard input

    else:
        print("Could not start video camera")
        break

cap.release()
cv2.destroyAllWindows()
