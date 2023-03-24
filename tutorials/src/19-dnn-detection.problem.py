# Exercise #19
# ------------
#
# A demonstration of object detection using a pre-trained deep neural network. Heavily based on
# https://learnopencv.com/deep-learning-with-opencvs-dnn-module-a-definitive-guide/

import cv2
import time
import numpy as np

# Load the COCO class names (TODO: files not available, download needed)
with open("models/object_detection_classes_coco.txt", "r", encoding="utf-8") as f:
    class_names = f.read().split("\n")
# DEBUG: print(class_names)

# Generate a different color array for each of the classes
colors = np.random.uniform(0, 255, size=(len(class_names), 3))

# TODO Load the DNN model with cv2.dnn.readNet()
net = cv2.dnn.readNet("your code here")

# Capture the video  (TODO: file not available, download needed)
cap = cv2.VideoCapture("./videos/objects_UH.MOV")
# cap = cv2.VideoCapture(0) # uncomment to use the webcam

# Get the video frames' width and height for proper saving of videos
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# Create the `VideoWriter()` object
do_write_video = False
if do_write_video:
    out = cv2.VideoWriter("video_result.mp4", cv2.VideoWriter_fourcc(*"mp4v"), 30, (frame_width, frame_height))

# Initialize window and helper variables
cv2.namedWindow("image", cv2.WINDOW_GUI_NORMAL)
conf_thresh = 0.1  # TODO Play with this value
max_object_size = 1.0  # TODO Play with this value

# Detect objects in each frame of the video
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        image = frame
        image_height, image_width, _ = image.shape

        # TODO Create blob from image using cv2.dnn.blobFromImage
        blob = cv2.dnn.blobFromImage("your code here")

        # Start time to calculate FPS
        start = time.time()

        # Set the blob as input
        net.setInput(blob)

        # TODO The inference: compute the output by running a forward pass
        output = "your code here"

        # End time after detection
        end = time.time()

        # Calculate the FPS for current frame detection
        fps = 1 / (end - start)

        # Loop over each of the detections that are stored in output
        for detection in output[0, 0, :, :]:
            # TODO Extract the confidence of the detection
            confidence = "your code here"

            # Draw bounding boxes only if the detection confidence is above
            # a certain threshold, else skip
            if confidence > conf_thresh:
                # TODO Get the class id
                class_id = "your code here"

                # Map the class id to the class
                class_name = class_names[int(class_id) - 1]
                color = colors[int(class_id)]

                # Get the bounding box coordinates
                box_x = detection[3] * image_width
                box_y = detection[4] * image_height

                # Get the bounding box width and height
                box_width = detection[5] * image_width
                box_height = detection[6] * image_height

                # Check if object is too large
                if (detection[5] > max_object_size) or (detection[6] > max_object_size):
                    # DEBUG: print('Object is too big.')
                    continue

                # Draw a rectangle around each detected object
                cv2.rectangle(image, (int(box_x), int(box_y)), (int(box_width), int(box_height)), color, thickness=2)

                # Put the class name text and the confidence on the detected
                # object
                output_text = class_name + " %.2f" % confidence
                cv2.putText(image, output_text, (int(box_x), int(box_y - 5)), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

                # Put the FPS text on top of the frame
                cv2.putText(image, f"{fps:.2f} FPS", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                # Detection results are sorted, hence after first object
                # under threshold, we can exit the for loop
                break

        # Show the image with the results
        cv2.imshow("image", image)

        # Write the video if intended
        if do_write_video:
            out.write(image)

        # Abort with 'q'
        key = cv2.waitKey(10)
        if key == ord("q"):
            break
    else:
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
