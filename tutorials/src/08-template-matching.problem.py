# Exercise #8
# -----------
#
# Demonstrating how to do template matching in OpenCV.

# Template matching, originally with objects from the image. Typical example
# is counting blood cells
import cv2

use_color = True

if use_color:
    """"""
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image

    # TODO Read shape of the template and original image

else:
    # TODO Load image and template image, note that the template has been
    # manually cut out of the image

    # TODO Read shape of the template and original image

    # TODO Define template matching methods,
    # See https://docs.opencv.org/4.5.3/df/dfb/group__imgproc__object.html#ga3a7850640f1fe1f58fe91a2d7583695d for the
    # math behind each method

    # TODO Loop over all methods in order to compare them

    # TODO (In loop) work on a new image each time

    # TODO (In loop) do the template matching

    # TODO (In loop) get the best match location

    # TODO (In loop) draw rectangle at found location

    # TODO (In loop) show original image with found location

    # TODO (In loop) show image with the template matching result for all pixels

    # (in loop) just press any key to show the next image
    cv2.waitKey(0)

cv2.destroyAllWindows()
