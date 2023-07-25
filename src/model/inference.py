import os

import utils.constant as const
import utils.helper_functions as helper


import tensorflow as tf


def preprocess_img(file):
    img = tf.keras.utils.load_img(file, target_size=const.IMAGE_SIZE)
    img_array = tf.keras.utils.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)

    return img_array


def inference(file):
    model_path = os.path.join(helper.get_parent_folder(__file__), "model.h5")
    model = tf.keras.models.load_model(model_path)

    image = preprocess_img(file)

    predictions = model.predict(image)
    predicted_class_index = tf.argmax(predictions[0])
    predicted_class = const.LABELS[predicted_class_index]
    confidence_score = predictions[0][predicted_class_index]

    return predicted_class, confidence_score
