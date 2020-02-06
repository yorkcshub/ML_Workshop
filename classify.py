import json
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.models import model_from_json
from keras.optimizers import RMSprop
#
from PIL import Image
from resizeimage import resizeimage

def load_model():
    # add code below:
    return model

def predict(model, df):
    y_prediction = np.argmax(model.predict(df), axis=1)
    return y_prediction[0]

def convert_image(path):
    # add code below:
    return df

def crop_center(pil_img, crop_width, crop_height):
    img_width, img_height = pil_img.size
    return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

def main():
    model = load_model()
    print("Input path of image:")
    img_path = input()

    while True:
        try:
            img_df = convert_image(img_path)
        except FileNotFoundError:
            print("File not found, try again")
            continue
        num = predict(model, img_df)
        print("The number of the image is " + str(num))
        input()

if __name__ == '__main__':
    main()
