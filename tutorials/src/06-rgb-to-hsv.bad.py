# Exercise #6
# -----------
#
# Playing around with colors. We convert some values from RGB to HSV and then find colored objects in the image and mask
# them out. Includes a color picker on double-click now. The RGB version is meant to demonstrate that this does not work
# in RGB color space.

import numpy as np
import cv2

# Rrint keyboard usage
print("This is a RGB color detection demo. Use the keys to adjust the \
selection color in RGB space. Circle in bottom left.")
print("The masked image shows only the pixels with the given HSV color within \
a given range.")
print("Use r/R to de-/increase the red value.")
print("Use g/G to de-/increase the green value.")
print("Use b/B to de-/increase the blue value.\n")
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

blue = (255, 0, 0)
red = (0, 0, 255)
green = (20, 200, 20)
black = (0, 0, 0)

font_size_large = 3
font_size_small = 1
font_size_smaller = 0.6
font = cv2.FONT_HERSHEY_SIMPLEX

# Color ranges, default values
red_channel = 10
red_range = 30
green_channel = 10
green_range = 30
blue_channel = 245
blue_range = 30


def color_picker(event, x, y, flags, param):
    global blue_channel, green_channel, red_channel
    if event == cv2.EVENT_LBUTTONDBLCLK:
        (r, g, b) = rgb[y, x]
        blue_channel = int(b)
        red_channel = int(r)
        green_channel = int(g)
        print("New color selected:", (blue_channel, green_channel, red_channel))


# Initialize windows
title_orig_window = "Original image"
cv2.namedWindow(title_orig_window)
cv2.setMouseCallback(title_orig_window, color_picker)
# Show the masked image in another window
title_masked_window = "Masked image"
cv2.namedWindow(title_masked_window)
title_mask_window = "Mask image"
cv2.namedWindow(title_mask_window)

while True:
    # Get video frame (always BGR format!)
    ret, frame = cap.read()
    if ret:
        # Copy image to draw on
        img = frame.copy()

        # Compute color ranges for display
        lower_rgb = np.array([red_channel - red_range, green_channel - green_range, blue_channel - blue_range])
        upper_rgb = np.array([red_channel + red_range, green_channel + green_range, blue_channel + blue_range])

        # Draw selection color circle
        img = cv2.circle(img, (width - 50, height - 50), 30, (blue_channel, green_channel, red_channel), -1)
        img = cv2.putText(img, "R = " + str(red_channel), (width - 200, height - 75), font, font_size_smaller, red,
                          thinner)
        img = cv2.putText(img, "G = " + str(green_channel), (width - 200, height - 50), font, font_size_smaller, green,
                          thinner)
        img = cv2.putText(img, "B = " + str(blue_channel), (width - 200, height - 25), font, font_size_smaller, blue,
                          thinner)

        # Convert from BGR to RGB
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Create a mask
        mask = cv2.inRange(rgb, lower_rgb, upper_rgb)

        # Apply mask
        result = cv2.bitwise_and(img, img, mask=mask)

        # Show the original image in one window
        cv2.imshow(title_orig_window, img)

        # Show the masked image in another window
        cv2.imshow(title_masked_window, result)

        # show the mask image in another window
        cv2.imshow(title_mask_window, mask)

        # Deal with keyboard input
        key = cv2.waitKey(10)
        if key == ord("q"):
            break
        if key == ord("r"):
            red_channel -= 1
        if key == ord("R"):
            red_channel += 1
        if key == ord("g"):
            green_channel -= 1
        if key == ord("G"):
            green_channel += 1
        if key == ord("b"):
            blue_channel -= 1
        if key == ord("B"):
            blue_channel += 1
    else:
        print("Could not start video camera")
        break

cap.release()
cv2.destroyAllWindows()
