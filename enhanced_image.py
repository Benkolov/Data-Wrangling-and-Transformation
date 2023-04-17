import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from PIL import Image


def load_image(image_path):
    img = tf.io.read_file(image_path)
    img = tf.image.decode_jpeg(img, channels=3)
    img = tf.image.resize(img, (224, 224))
    img = tf.keras.applications.mobilenet_v2.preprocess_input(img)
    return tf.expand_dims(img, 0)


def analyze_and_enhance(image_path, model_path="https://tfhub.dev/captain-pool/esrgan-tf2/1"):
    # Заредете изображението
    image = load_image(image_path)

    # Заредете предварително обучен модел
    model = hub.load(model_path)

    # Анализирайте и подобрете изображението
    enhanced_image = model(image)

    # Преобразувайте обработеното изображение обратно в PIL Image
    enhanced_image = tf.squeeze(enhanced_image, 0)
    enhanced_image = (enhanced_image + 1) / 2 * 255
    enhanced_image = np.clip(enhanced_image, 0, 255)
    enhanced_image = Image.fromarray(enhanced_image.numpy().astype(np.uint8))

    return enhanced_image

image_path = "candles_images/image1.jpg"
enhanced_image = analyze_and_enhance(image_path)
enhanced_image.save("enhanced_images/enhanced_image.jpg")

