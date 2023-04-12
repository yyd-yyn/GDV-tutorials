# Tutorial #15
# ------------
#
# Compute the features of an image with the Harris corner detection. Adjust the parameters using sliders.

import numpy as np
import cv2


# Function to detect and draw the corners
def draw_features(corners):
    # Drawing helper variables
    thick = 5
    thin = 2
    filled = -1

    small_size = 3
    medium_size = 5
    large_size = 7

    # Get a different color array for each of the features/corners
    colors = np.random.uniform(0, 255, size=(len(corners), 3))

    # Draw a circle around each corner
    img = np.copy(img_clone)

    for corner, color in zip(corners, colors):
        # Draw the corners in the colored image
        cv2.circle(img, tuple(corner.ravel()), medium_size, color, thin)
        # DEBUG: print(tuple(corner.ravel()))

    cv2.imshow(window_name, img)


def on_change(val):
    # Read paremeters from slider positions
    max_number_of_features = cv2.getTrackbarPos("max_number_of_features", window_name)
    min_quality_trackbar_value = cv2.getTrackbarPos("min_quality", window_name)
    min_quality = min_quality_trackbar_value / 10
    min_euclid_dist = cv2.getTrackbarPos("min_euclid_dist", window_name)
    # Run corner detection
    corners = cv2.goodFeaturesToTrack(img_gray,
                                      max_number_of_features,
                                      min_quality,
                                      min_euclid_dist,
                                      useHarrisDetector=True)
    # Returns corners as floating point values, hence convert to integer
    corners = np.intp(corners)
    draw_features(corners)


# Load example image as color image
img = cv2.imread("./tutorials/data/images/logo.png", cv2.IMREAD_COLOR)
img = cv2.resize(img, (400, 400))

# Clone image
img_clone = np.copy(img)

# Create a greyscale image for the corner detection
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a window with sliders and show resulting image
window_name = "Good features demo"
cv2.imshow(window_name, img)

# Create sliders for all parameters and one callback function
# note that these calls lead to an assertion error as on_change is called once on creation
cv2.createTrackbar("max_number_of_features", window_name, 10, 500, on_change)
cv2.createTrackbar("min_quality", window_name, 3, 10, on_change)
cv2.createTrackbar("min_euclid_dist", window_name, 15, 100, on_change)

# Wait until a key is pressed and end the application
cv2.waitKey(0)
cv2.destroyAllWindows()
