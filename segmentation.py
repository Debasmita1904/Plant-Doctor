import cv2
import numpy as np


def segment_colors(hsv_image):
    """
    Segment green, yellow and brown regions
    from an HSV image.
    """

    # Green color range
    green_lower = np.array([35, 50, 40])
    green_upper = np.array([85, 255, 255])

    # Yellow color range
    yellow_lower = np.array([20, 50, 50])
    yellow_upper = np.array([35, 255, 255])

    # Brown color range
    brown_lower = np.array([5, 50, 20])
    brown_upper = np.array([25, 255, 200])

    # Create masks
    green_mask = cv2.inRange(
        hsv_image, green_lower, green_upper
    )

    yellow_mask = cv2.inRange(
        hsv_image, yellow_lower, yellow_upper
    )

    brown_mask = cv2.inRange(
        hsv_image, brown_lower, brown_upper
    )

    # Remove small noise
    kernel = np.ones((5, 5), np.uint8)

    green_mask = cv2.morphologyEx(
        green_mask, cv2.MORPH_OPEN, kernel
    )

    yellow_mask = cv2.morphologyEx(
        yellow_mask, cv2.MORPH_OPEN, kernel
    )

    brown_mask = cv2.morphologyEx(
        brown_mask, cv2.MORPH_OPEN, kernel
    )

    return green_mask, yellow_mask, brown_mask