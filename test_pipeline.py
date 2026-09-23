import cv2
from analysis import analyze_plant_health
from image_processing import process_image
from segmentation import segment_colors

# 1. Provide a test image path from the images directory
# Replace with any image name present in your images/ folder
image_path = "images/leaf.jpg"

# 2. Debasmita's module processes the image
processed = process_image(image_path)
rgb_img = processed["rgb"]
hsv_img = processed["hsv"]

# 3. Adrija's module segments colors using the HSV image
green_mask, yellow_mask, brown_mask = segment_colors(hsv_img)

# 4. Your module computes stats and draws highlights
results = analyze_plant_health(rgb_img, green_mask, yellow_mask, brown_mask)

# 5. Display the output
print("\n========== PLANT DOCTOR REPORT ==========")
print(f"Observation:         {results['observation']}")
print(f"Healthy (Green):     {results['green_percentage']}%")
print(f"Chlorotic (Yellow):  {results['yellow_percentage']}%")
print(f"Necrotic (Brown):    {results['brown_percentage']}%")
print(f"Total Affected Area: {results['affected_percentage']}%")
print("=========================================\n")

# 6. Save highlighted image (convert RGB back to BGR for cv2.imwrite)
output_bgr = cv2.cvtColor(results["highlighted_image"], cv2.COLOR_RGB2BGR)
cv2.imwrite("test_output.jpg", output_bgr)
print("Saved output to 'test_output.jpg'.")
