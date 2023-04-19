import os

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image


image_directory = "candles_images"
image_filenames = [f for f in os.listdir(image_directory) if f.endswith(".jpg") or f.endswith(".png")]

def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_image(img, channels=3)
    img = tf.image.resize(img, [224, 224])
    img = img / 255.0
    return img


def analyze_and_enhance(image_path, model_path="https://tfhub.dev/captain-pool/esrgan-tf2/1"):
    # Заредете изображението
    image = load_image(image_path)
    image = tf.expand_dims(image, axis=0)

    # Заредете предварително обучен модел
    model = hub.load(model_path)

    # Анализирайте и подобрете изображението
    enhanced_image = model(image)

    # Преобразувайте обработеното изображение обратно в PIL Image
    enhanced_image = tf.squeeze(enhanced_image, 0)
    enhanced_image = (enhanced_image + 1) / 2 * 255
    enhanced_image = np.clip(enhanced_image, 0, 255)
    enhanced_image = Image.fromarray(enhanced_image.astype(np.uint8))


    return enhanced_image


output_directory = "enhanced_images"

# Създайте директорията за изходните изображения, ако не съществува
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for image_name in image_filenames:
    image_path = os.path.join(image_directory, image_name)
    enhanced_image = analyze_and_enhance(image_path)

    # Запишете обработеното изображение в директорията за изход
    output_path = os.path.join(output_directory, f"enhanced_{image_name}")
    enhanced_image.save(output_path)


