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
    # load json and create model
    with open('model.json', 'r') as f:
        model_json = f.read()
    model = model_from_json(model_json)
    # load weights into new model
    model.load_weights("model.h5")
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(0.01), metrics=['accuracy'])
    return model

def predict(model, df):
    y_prediction = np.argmax(model.predict(df), axis=1)
    return y_prediction[0]

def convert_image(path):
    img = Image.open(path)
    img.convert('L') # convert to grayscale
    img = crop_center(img, min(img.size), min(img.size))
    -
    img.save('img2.jpg', 'JPEG')

    img_np = np.asarray(img.getdata(), dtype=np.int) # convert image into ndarray
    img_np = np.dot(img_np[...,:3], [0.2989, 0.5870, 0.1140])[np.newaxis] # convert rgb into greyscale
    img_np = np.around(img_np).astype(int) # round ndrray into integers
    img_np = np.absolute(np.subtract(img_np, 255)) # flip the black and white values

    df = pd.DataFrame(img_np)

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
