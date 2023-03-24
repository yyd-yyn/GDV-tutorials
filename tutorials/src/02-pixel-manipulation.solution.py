# Tutorial #2
# -----------
#
# Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place,
# count the used colors in the image

import cv2
import numpy as np

# Loading images in grey and color
img_gray = cv2.imread("./exercises/data/images/logo.png", cv2.IMREAD_GRAYSCALE)
img_color = cv2.imread("./exercises/data/images/logo.png", cv2.IMREAD_COLOR)

# Do some print out about the loaded data
print(type(img_gray))  # Prints class numpy.ndarray
print(type(img_color))  # Prints class numpy.ndarray

print(img_gray.dtype)  # Prints the data type of the image array
print(img_color.dtype)  # Prints the date type of the image array

print(img_gray.shape)  # Prints the size of the image array
print(img_color.shape)  # Prints the size of the image array

# Continue with the grayscale image
img = img_gray.copy()

# Extract the size or resolution of the image
height = img.shape[0]
width = img.shape[1]
last_dim = img.shape[-1]
print("height = " + str(img.shape[0]))
print("width = " + str(img.shape[1]))
print("last dimension = " + str(last_dim))

# Resize image
new_width = 7
new_height = 5
new_size = (new_width, new_height)
img = cv2.resize(img, new_size)

# Row and column access, see https://numpy.org/doc/stable/reference/arrays.ndarray.html for general access on ndarrays
# Print first row
print(img[0])

# Print first column
print(img[:, 0])

# Continue with the color image
img = img_color.copy()

# Set area of the image to black
for i in range(30):
    for j in range(width):
        img[i][j] = [0, 0, 0]

# Show the image
title = "OpenCV Python Tutorial"

# Note that window parameters have no effect on MacOS
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, img)
cv2.waitKey(0)

# Find all used colors in the image
# See: https://stackoverflow.com/questions/51705187/list-of-all-colors-in-an-image-using-opencv-and-python
all_rgb_codes = img.reshape(-1, img.shape[-1])
unique_rgb_codes = np.unique(all_rgb_codes, axis=0, return_counts=False)
print("Those color values are in the image:\n " + str(unique_rgb_codes))

# Copy one part of an image into another one
letters = img[30:105, 5:130]
img[115:190, 150:275] = letters

# Save image
cv2.imwrite("img_tutorial02.jpg", img)

# Show the image again
cv2.imshow(title, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Show the original image (copy demo)
title = "How a copy works"
cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)
cv2.imshow(title, img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
