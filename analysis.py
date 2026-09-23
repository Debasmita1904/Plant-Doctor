import cv2
import numpy as np


def analyze_plant_health(image, green_mask, yellow_mask, brown_mask):
    """
    Analyzes plant leaf health based on color segmentation masks.

    Parameters:
        image: Original input image (RGB or BGR numpy array).
        green_mask: Binary mask for green areas (0 or 255).
        yellow_mask: Binary mask for yellow areas (0 or 255).
        brown_mask: Binary mask for brown areas (0 or 255).

    Returns:
        Dictionary containing health percentages, diagnostic observation,
        and the annotated output image.
    """
    # 1. Combine masks cleanly to avoid double counting overlaps
    affected_mask = cv2.bitwise_or(yellow_mask, brown_mask)
    leaf_mask = cv2.bitwise_or(green_mask, affected_mask)

    # 2. Count non-zero pixel areas
    total_leaf_pixels = int(cv2.countNonZero(leaf_mask))
    green_pixels = int(cv2.countNonZero(green_mask))
    yellow_pixels = int(cv2.countNonZero(yellow_mask))
    brown_pixels = int(cv2.countNonZero(brown_mask))
    affected_pixels = int(cv2.countNonZero(affected_mask))

    # Guard: No leaf detected
    if total_leaf_pixels == 0:
        return {
            "green_percentage": 0.0,
            "yellow_percentage": 0.0,
            "brown_percentage": 0.0,
            "affected_percentage": 0.0,
            "observation": "No leaf tissue detected in segmentation masks.",
            "highlighted_image": image.copy(),
        }

    # 3. Calculate percentage breakdown relative to total leaf area
    green_pct = round((green_pixels / total_leaf_pixels) * 100, 2)
    yellow_pct = round((yellow_pixels / total_leaf_pixels) * 100, 2)
    brown_pct = round((brown_pixels / total_leaf_pixels) * 100, 2)
    affected_pct = round((affected_pixels / total_leaf_pixels) * 100, 2)

    # 4. Highlight affected regions on the original image (red contours)
    highlighted_image = image.copy()
    contours, _ = cv2.findContours(
        affected_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # Draw red outlines: (255, 0, 0) for RGB, or (0, 0, 255) for BGR
    cv2.drawContours(highlighted_image, contours, -1, (255, 0, 0), 2)

    # 5. Diagnostic observation
    if affected_pct < 5.0:
        observation = "Healthy: Minimal to no discoloration detected."
    elif affected_pct < 20.0:
        observation = "Noticeable discoloration detected: Early-stage infection or nutrient deficiency."
    else:
        observation = "Severe discoloration detected: Significant necrotic or chlorotic tissue observed."

    return {
        "green_percentage": green_pct,
        "yellow_percentage": yellow_pct,
        "brown_percentage": brown_pct,
        "affected_percentage": affected_pct,
        "observation": observation,
        "highlighted_image": highlighted_image,
    }
