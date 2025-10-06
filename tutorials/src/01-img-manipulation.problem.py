# Exercise #1
# -----------
#
# Load, resize and rotate an image. And display it to the screen.

# TODO First step is to 'import' the opencv module which is called 'cv2'.
import cv2

# TODO Check the opencv version and display it with 'print'.
print(cv2.__version__)

# TODO Load an image with image reading modes using 'imread'.
# cv2.IMREAD_UNCHANGED  - If set, return the loaded image as is (with alpha
#                         channel, otherwise it gets cropped). Ignore EXIF
#                         orientation.
# cv2.IMREAD_GRAYSCALE  - If set, always convert image to the single channel
#                         grayscale image (codec internal conversion).
# cv2.IMREAD_COLOR      - If set, always convert image to the 3 channel BGR
#                         color image.
img = cv2.imread("tutorials/data/images/nl_clown.jpg")

# TODO Check if image is loaded fine and raise a FileNotFoundError if not.
if img is None:
    raise FileNotFoundError("image file not found")

# TODO Resize image with 'resize'.

# TODO Rotate image (but keep it rectangular) with 'rotate'.

# TODO Save image with 'imwrite'.
cv2.imwrite("output.jpg", img)

# TODO Show the image with 'imshow'.
cv2.imshow("clawn", img)

# TODO Avoid the immediate closing of the image window with 'waitKey'.
cv2.waitKey(0)
