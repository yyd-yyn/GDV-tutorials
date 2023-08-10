import numpy as np
import cv2
import requests
import html
from ultralytics import YOLO  # pip install ultralytics needed


# TODO Implement image retrieval from web
def grab_image(query, save_image=False, save_path="tutorials/data/myimages/", filename="image.jpg"):
    # retrieve image from url
    response = requests.get("https://source.unsplash.com/random{0}".format(html.escape(query)))
    nparr = np.frombuffer(response.content, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imshow("result", img_np)
    # save image to path
    if save_image:
        cv2.imwrite(save_path + filename, img_np)
    cv2.waitKey(0)
    return img_np


query = "bird"
grab_image('/1280x720/?' + query, True, "tutorials/data/myimages/", "{0}.jpg".format(query))
