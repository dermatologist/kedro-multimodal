"""
This is a boilerplate pipeline 'train'
generated using Kedro 0.18.1
"""
from sklearn.model_selection import train_test_split

from tensorflow.keras.optimizers import Adadelta, Adam, SGD
from keras_preprocessing.image import img_to_array
import numpy as np
import tensorflow as tf
import keras.layers as layers

def train_multimodal(text_dataset, image_dataset, multi_modal, parameters):
    """
    Train multimodal model
    """
    y = text_dataset.pop(parameters['TARGET'])
    text_dataset.drop(parameters['DROP'], axis=1, inplace=True)

    ids = image_dataset.keys()
    _imgs = np.array([np.array(image_dataset[id]()) for id in ids]) # column is a function that returns image data
    csv_features_dict = {name: np.array(value)
                         for name, value in text_dataset.items()}


    multi_modal.compile(loss='binary_crossentropy',
                        optimizer=Adam(), metrics=['accuracy'])

    hist = multi_modal.fit(
        x=[csv_features_dict, _imgs],
        y=y, batch_size=32, epochs=3, verbose=1,
        validation_data=None)
    return multi_modal
