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
def grab_more_images(query, image_count, save_path="tutorials/data/myimages/", test_percentage=0.2):
    for i in range((int)(image_count * test_percentage)):
        grab_image('/1280x720/?' + query, False, True, save_path + "test/", "{0}_{1}.jpg".format(query, i))
    for i in range((int)(image_count * (1 - test_percentage))):
        grab_image('/1280x720/?' + query, False, True, save_path + "train/", "{0}_{1}.jpg".format(query, i))


# TODO retrieve images for training
# create folder structure as shown here: https://docs.ultralytics.com/datasets/classify/ with "train" and "test folder
def grab_training_images(image_types, image_count, save_path="tutorials/data/myimages/"):
    for image_type in image_types:
        grab_more_images(image_type, image_count, save_path + image_type + "/")


# If you want to use a detection model instead, do the following:
# TODO follow roboflow tutorial (https://github.com/ultralytics/yolov5/wiki/Train-Custom-Data - Chapter 1.2 & 1.3)
# to create dataset and download it
# you also have to use an appropriate yolo model (e.g. yolov5s).


# TODO train model
# base model needs to be downloaded first
def train_model(data_path, _epochs):
    model = YOLO("./tutorials/data/models/yolov8n-cls.pt")
    results = model.train(data=data_path, epochs=_epochs)
    return results


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
        print(result.names[0] + ": " + str(result.probs.data[0].item()))
    # show image with bounding boxes
    cv2.imshow("result", img)
    return results


# TODO Create interactive application to choose between steps
while True:
    # present options
    print("press q to quit")
    print("press 1 to grab images")
    print("press 2 to train model")
    print("press 3 to test model")
    cv2.namedWindow("result", cv2.WINDOW_NORMAL)
    key = cv2.waitKey(0)
    # press q to close the window
    if key == ord('q'):
        break
    # press 1 to grab image
    if key == ord('1'):
        image_descriptors = ["bird", "forest"]
        # ask for image count
        image_count = (int)(input("input the number of images you want to download: "))
        # set save path
        save_path = "tutorials/data/myimages/"
        grab_training_images(image_descriptors, image_count, save_path)
    # press 2 to train model
    if key == ord('2'):
        data_path = './tutorials/data/myimages'
        _epochs = (int)(input("input the number of epochs: "))
        train_model(data_path, _epochs)
    # press 3 to test model
    if key == ord('3'):
        model_path = "./tutorials/data/runs/classify/train3/weights/best.pt"
        while True:
            test_model(model_path)
            if cv2.waitKey(0) == ord('q'):
                break
        break
