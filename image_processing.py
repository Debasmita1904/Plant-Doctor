import cv2
import numpy as np


def load_image(image_path):
    """
    Load an image using OpenCV.
    OpenCV loads images in BGR format.
    """
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Could not load image: {image_path}")

    return image


def convert_bgr_to_rgb(image):
    """
    Convert an OpenCV BGR image to RGB format.
    """
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return rgb_image


def split_rgb_channels(rgb_image):
    """
    Separate an RGB image into Red, Green and Blue channels.
    """
    red = rgb_image[:, :, 0]
    green = rgb_image[:, :, 1]
    blue = rgb_image[:, :, 2]

    return red, green, blue


def convert_rgb_to_hsv(rgb_image):
    """
    Convert an RGB image to HSV format.
    """
    hsv_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2HSV)
    return hsv_image


def process_image(image_path):
    """
    Complete image-processing pipeline:

    Image
       ↓
    BGR
       ↓
    RGB
       ↓
    Separate R, G, B
       ↓
    HSV
    """

    # Load image
    image = load_image(image_path)

    # Convert BGR → RGB
    rgb_image = convert_bgr_to_rgb(image)

    # Separate RGB channels
    red, green, blue = split_rgb_channels(rgb_image)

    # Convert RGB → HSV
    hsv_image = convert_rgb_to_hsv(rgb_image)

    return {
        "rgb": rgb_image,
        "red": red,
        "green": green,
        "blue": blue,
        "hsv": hsv_image
    }