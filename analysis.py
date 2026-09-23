import cv2
import numpy as np


def analyze_plant_health(image, green_mask, yellow_mask, brown_mask):
    """
    Analyzes plant leaf health based on color segmentation masks.

    Parameters:
        image: Original input image (numpy array).
        green_mask: Binary mask of healthy green leaf tissue (values 0 or 255).
        yellow_mask: Binary mask of chlorotic/yellow tissue (values 0 or 255).
        brown_mask: Binary mask of necrotic/brown tissue (values 0 or 255).

    Returns:
        results: Dictionary containing area breakdown, percentages, observation,
                 and the annotated output image.
    """
    # 1. Combine masks to determine total leaf area
    combined_leaf_mask = cv2.bitwise_or(green_mask, yellow_mask)
    combined_leaf_mask = cv2.bitwise_or(combined_leaf_mask, brown_mask)

    # 2. Count non-zero pixels (pixel areas)
    total_leaf_pixels = cv2.countNonZero(combined_leaf_mask)
    green_pixels = cv2.countNonZero(green_mask)
    yellow_pixels = cv2.countNonZero(yellow_mask)
    brown_pixels = cv2.countNonZero(brown_mask)

    # Guard against division by zero if no leaf was segmented
    if total_leaf_pixels == 0:
        return {
            "green_percentage": 0.0,
            "yellow_percentage": 0.0,
            "brown_percentage": 0.0,
            "affected_percentage": 0.0,
            "observation": "No leaf tissue detected in segmentation masks.",
            "highlighted_image": image.copy(),
        }

    # 3. Calculate percentages relative to total leaf area
    green_pct = round((green_pixels / total_leaf_pixels) * 100, 2)
    yellow_pct = round((yellow_pixels / total_leaf_pixels) * 100, 2)
    brown_pct = round((brown_pixels / total_leaf_pixels) * 100, 2)
    affected_pct = round(yellow_pct + brown_pct, 2)

    # 4. Combine yellow and brown regions (affected/diseased area)
    affected_mask = cv2.bitwise_or(yellow_mask, brown_mask)

    # 5. Highlight affected regions on the original image using red contours
    highlighted_image = image.copy()
    contours, _ = cv2.findContours(
        affected_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    # Draw red outline around affected regions (thickness = 2)
    cv2.drawContours(highlighted_image, contours, -1, (0, 0, 255), 2)

    # 6. Generate plant health observation
    if affected_pct < 5.0:
        observation = "Healthy: Minimal to no discoloration detected."
    elif affected_pct < 20.0:
        observation = "Noticeable discoloration detected: Early-stage infection or nutrient deficiency."
    else:
        observation = "Severe discoloration detected: Significant necrotic or chlorotic tissue observed."

    # 7. Final structured output
    return {
        "green_percentage": green_pct,
        "yellow_percentage": yellow_pct,
        "brown_percentage": brown_pct,
        "affected_percentage": affected_pct,
        "observation": observation,
        "highlighted_image": highlighted_image,
    }
