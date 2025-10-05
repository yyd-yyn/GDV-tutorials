import numpy as np
import cv2
from ultralytics import YOLO  # pip install ultralytics needed

# load model (TODO: download before running from https://github.com/ultralytics/assets/)
model = YOLO("./tutorials/data/models/yoloXXX.pt")

# capture webcam image
cap = cv2.VideoCapture(0)

# get camera image parameters from get()
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
codec = int(cap.get(cv2.CAP_PROP_CODEC_PIXEL_FORMAT))
focus = int(cap.get(cv2.CAP_PROP_AUTOFOCUS))

print('Video properties:')
print('  Width = ' + str(width))
print('  Height = ' + str(height))
print('  Codec = ' + str(codec))
print('  Autofocus = ' + str(focus))

title = 'Video image'
cv2.namedWindow(title, cv2.WINDOW_FREERATIO)  # Note that window parameters have no effect on MacOS
print('Press q to close the window.')

while True:
    ret, frame = cap.read()
    if (ret):
        # show the image
        img = frame.copy()
        # detect objects in img
        results = model.predict(source=img, stream=True, show=False)
        # parse results and draw bounding boxes on img
        for result in results:
            boxes = result.boxes
            class_names = result.names
            # draw bounding boxes on img
            for i in range(len(boxes)):
                box = boxes[i]
                # print(box) # print box object to find out which information is available
                # draw bounding box
                x1 = (int)(box.xyxy.numpy()[0][0])
                y1 = (int)(box.xyxy.numpy()[0][1])
                x2 = (int)(box.xyxy.numpy()[0][2])
                y2 = (int)(box.xyxy.numpy()[0][3])
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # draw class name and score
                class_name = class_names[(int)(box.cls.numpy()[0])]
                cv2.putText(img, class_name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                score = box.conf.numpy()[0]
                cv2.putText(img, str(score), (x1, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        # show image with bounding boxes
        cv2.imshow(title, img)

        # press q to close the window
        if cv2.waitKey(10) == ord('q'):
            break
    else:
        print('Could not start video camera')
        break

cap.release()
cv2.destroyAllWindows()
