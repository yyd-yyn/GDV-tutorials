# Tutorial #8
# -----------
#
# Demonstrating how to do template matching in OpenCV.

# Template matching, originally with objects from the image. Typical example is
# counting blood cells
import cv2

use_color = True

if use_color:
    # Load image and template image, note that the template has been manually
    # cut out of the image
    img = cv2.imread("./tutorials/data/images/chewing_gum_balls06.jpg", cv2.IMREAD_COLOR)
    template = cv2.imread("./tutorials/data/images/cgb_green.jpg", cv2.IMREAD_COLOR)

    # Read shape of the template and original image
    h, w, c = template.shape
    H, W, C = img.shape
else:
    # Load image and template image, note that the template has been manually
    # cut out of the image
    img = cv2.imread("./tutorials/data/images/chewing_gum_balls06.jpg", cv2.IMREAD_GRAYSCALE)
    template = cv2.imread("./tutorials/data/images/cgb_green.jpg", cv2.IMREAD_GRAYSCALE)

    # Read shape of the template and original image
    h, w = template.shape
    H, W = img.shape

# Define template matching methods,
# See https://docs.opencv.org/4.x/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the math
# behind each method
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
method_names = [
    "cv2.TM_CCOEFF",
    "cv2.TM_CCOEFF_NORMED",
    "cv2.TM_CCORR",
    "cv2.TM_CCORR_NORMED",
    "cv2.TM_SQDIFF",
    "cv2.TM_SQDIFF_NORMED",
]

# Loop over all methods in order to compare them
for method, method_name in zip(methods, method_names):
    # Work on a new image each time
    img2 = img.copy()

    # Do the template matching
    result = cv2.matchTemplate(img2, template, method)

    # Get the best match location
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]:
        best_match_location = min_loc
    else:
        best_match_location = max_loc

    # Draw rectangle at found location
    bottom_right = (best_match_location[0] + w, best_match_location[1] + h)
    cv2.rectangle(img2, best_match_location, bottom_right, 255, 5)

    # Show original image with found location
    cv2.imshow("Location", img2)

    # Show image with the template matching result for all pixels
    result_title = "Result with %s" % method_name
    cv2.imshow(result_title, result)
    cv2.waitKey(0)
    cv2.destroyWindow(result_title)

cv2.destroyAllWindows()
