import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
import numpy as np
from PIL import Image

# Load pre-trained model
model = MobileNetV2(weights='imagenet')

def predict_image(img_path):
    img = Image.open(img_path).resize((224, 224))
    img_array = np.array(img)

    # Preprocess
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=1)[0][0]

    return decoded[1], float(decoded[2])  # label, confidence
