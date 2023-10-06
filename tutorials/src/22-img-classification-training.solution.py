from utils.get_image_from_web import grab_image
from ultralytics import YOLO  # pip install ultralytics needed


# TODO retrieve multiple images
def grab_more_images(query, image_count, save_path="./tutorials/data/myimages/", test_percentage=0.2):
    for i in range((int)(image_count * test_percentage)):
        grab_image('/1280x720/?' + query, True, save_path + "/test/{0}/{1}.jpg".format(query, i))
    for i in range((int)(image_count * (1 - test_percentage))):
        grab_image('/1280x720/?' + query, True, save_path + "/train/{0}/{1}.jpg".format(query, i))


# TODO retrieve images for training
# create folder structure as shown here: https://docs.ultralytics.com/datasets/classify/ with "train" and "test folder
def grab_training_images(image_types, image_count, save_path="./tutorials/data/myimages/"):
    for image_type in image_types:
        grab_more_images(image_type, image_count, save_path)


# TODO train model
# base model needs to be downloaded first
def train_model(data_path, num_epochs):
    # TODO download base model from https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8s-cls.pt
    model = YOLO("./tutorials/data/models/yolov8s-cls.pt")
    results = model.train(data=data_path, epochs=num_epochs)
    return results


# TODO Test your new model
def test_model(image_descriptors, model_path):
    model = YOLO(model_path)
    index = 0
    for image_type in image_descriptors:
        # retrieve new image from web
        query = image_type  # change to 1 for other category
        img = grab_image('/1280x720/?' + query, False, "./tutorials/data/myimages/test.jpg")
        # detect objects in image
        results = model.predict(source=img, stream=True, show=True)  # detect objects in img
        # show results
        for result in results:
            print("Result for " + query + ": " + str(result.probs.data[index]))
        index += 1


def main():

    # define categories
    image_descriptors = ["bird", "forest"]
    # set number of images
    image_count = 30
    # set save path
    save_path = "./tutorials/data/myimages/"
    # start grabbing images
    # grab_training_images(image_descriptors, image_count, save_path)

    # define data path
    data_path = './tutorials/data/myimages'
    # define number of training epochs
    num_epochs = 5
    # define model path (where to save the model)
    #model_path = "./tutorials/data/mymodel.pt"
    # run the training process
    # results = train_model(data_path, num_epochs)
    # show results
    # print(results)

    # test the trained model manually
    model_path = "./runs/classify/train3/weights/best.pt"  # obey number of training runs
    test_model(image_descriptors, model_path)


if __name__ == "__main__":
    main()
