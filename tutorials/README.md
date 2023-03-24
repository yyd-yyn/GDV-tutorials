# GDV Tutorial sources

This folder contains the source code files for the tutorials.

## List of tutorials

### Tutorial #1
Load, resize and rotate an image. And display it to the screen.)

### Tutorial #2
Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place, count the used colors in the image

### Tutorial #3
Show camera video and mirror it.

### Tutorial #4
Loading a video file and mirror it.

### Tutorial #5
Use the webcam image stream and draw something on it. Animate one of the drawings.

### Tutorial #6
Playing around with colors. We convert some values from RGB to HSV and then find colored objects in the image and mask them out. Includes a color picker on double-click now. The RGB version is meant to demonstrate that this does **not** work in RGB color space.
- [rgb example](tutorials\src\06-rgb-to-hsv.bad.py)

### Tutorial #7
Counting colored objects by finding connected components in the binary image. Modify the binary image to improve the results.

### Tutorial #8
Demonstrating how to do template matching in OpenCV. 

### Tutorial #9
Demonstrating Gaussian blur filter with OpenCV. 
- [complete code with 3D plot of the kernel using matplotlib](./GDV_tutorial_09_3Dplot.py)
  - Note that matplotlib and PyQT5 need to be installed as described [here](https://matplotlib.org/stable/users/installing.html)

### Tutorial #10
Doing the Fourier Transform for images and back.

### Tutorial #11
Geometric transformations a.k.a. image warping.

### Tutorial #12
Select three points in two images and compute the appropriate affine transformation.

### Tutorial #13
Select four points in two images and compute the appropriate projective/perspective transformation.

### Tutorial #14
Compute the edges of an image with the Canny edge detection. Adjust the parameters using sliders.

### Tutorial #15
Compute the features of an image with the Harris corner detection. Adjust the parameters using sliders.

### Tutorial #16
Compute the Harris corner response image and detect isolated corners with non-maximum suppression.

### Tutorial #17
A demonstration of the OpenCV Simple Blob Detector. Adjust the parameters using sliders.

### Tutorial #18
A demonstration of SIFT Detector and Descriptor for object recognition.

### Tutorial #19
A demonstration of object detection using a pre-trained deep neural network. Heavily based on https://learnopencv.com/deep-learning-with-opencvs-dnn-module-a-definitive-guide/

### Tutorial #20
Image classification with k-nearest neighbor approach using the CIFAR-10 data. Code is similar to the one used in assignment #4 and hence a bit cluttered.

