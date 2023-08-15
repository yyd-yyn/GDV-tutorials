import numpy as np
import cv2
import requests
import html
from ultralytics import YOLO  # pip install ultralytics needed
from roboflow import Roboflow


# TODO Implement image retrieval from web
def grab_image(query, show_image, save_image=False, save_path="tutorials/data/myimages/", filename="image.jpg"):
    # retrieve image from url
    response = requests.get("https://source.unsplash.com/random{0}".format(html.escape(query)))
    nparr = np.frombuffer(response.content, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if show_image:
        cv2.imshow("result", img_np)
    # save image to path
    if save_image:
        cv2.imwrite(save_path + filename, img_np)
    return img_np


# TODO retrieve multiple images
def grab_more_images(query, image_count, save_path="tutorials/data/myimages/"):
    images = []
    for i in range(image_count):
        images.append(grab_image('/1280x720/?' + query, False, True, save_path, "{0}_{1}.jpg".format(query, i)))
    return images


# TODO retrieve images for training
def grab_training_images(image_types, image_count, save_path="tutorials/data/myimages/"):
    images = []
    for image_type in image_types:
        images.append(grab_more_images(image_type, image_count, save_path + image_type + "/"))
    return images


# images = grab_training_images(["bird", "forest"], 20)

# TODO follow roboflow tutorial (https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data - Chapter 1.2 & 1.3)
# to create dataset


def download_dataset(key, workspace, project_name, version, format):
    rf = Roboflow(api_key=key)
    project = rf.workspace(workspace).project(project_name)
    dataset = project.version(version).download(format)
    return dataset


# download_dataset("UgfrdbqnWJsvblKXzK6f", "hfu", "bird-or-forest", 2, "yolov5")


# TODO train model
def train_model(data_path, _epochs):
    model = YOLO("./tutorials/data/models/yolov5su.pt")
    results = model.train(data=data_path, epochs=_epochs)
    return results


# results = train_model('./tutorials/data/bird-or-forest-2/data.yaml', 10)


# TODO Test your new model
def test_model(model_path):
    model = YOLO(model_path)
    # retrieve new image from web
    query = input("Enter your query: ")
    img = grab_image('/1280x720/?' + query, False, False, "./tutorials/data/myimages/", "test.jpg")
    # detect objects in image
    results = model.predict(source=img, stream=True, show=False)  # detect objects in img
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
    cv2.imshow("result", img)
    cv2.waitKey(0)
    return results


test_model("./tutorials/data/runs/detect/train2/weights/best.pt")
