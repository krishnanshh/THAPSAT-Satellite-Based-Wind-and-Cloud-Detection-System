import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function for cloud detection using adaptive thresholding and morphological operations
def detect_cloud(image):
    # Preprocess the image for cloud detection
    blurred = cv2.GaussianBlur(image, (7, 7), 0)
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    # Apply morphological operations to enhance cloud regions
    kernel = np.ones((5, 5), np.uint8)
    cloud_mask = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel, iterations=2)

    return cloud_mask

# Load the SST data 
sst_image = cv2.imread('sea_temp.jpg', cv2.IMREAD_GRAYSCALE)

# Detect clouds using adaptive thresholding and morphological operations
cloud_mask = detect_cloud(sst_image)

# Check if cloud_mask is loaded successfully and contains valid data
if cloud_mask is None or not np.any(cloud_mask):
    raise ValueError("Error: Failed to detect cloud regions. Please check the detection implementation.")

# Calculate the temperature gradient using Sobel filter
gradient_x = cv2.Sobel(sst_image, cv2.CV_64F, 1, 0, ksize=3)
gradient_y = cv2.Sobel(sst_image, cv2.CV_64F, 0, 1, ksize=3)

# Compute the magnitude and angle of the gradient vectors
magnitude = np.sqrt(gradient_x*2 + gradient_y*2)
angle_rad = np.arctan2(gradient_y, gradient_x)

# Convert the angle from radians to degrees and shift range to [0, 360)
angle_deg = (angle_rad * 180.0 / np.pi) % 360

# Approximate wind directions based on the angle_deg
wind_directions = []
for row in angle_deg:
    directions_row = []
    for angle in row:
        if 45 <= angle < 135:
            directions_row.append("North")
        elif 135 <= angle < 225:
            directions_row.append("West")
        elif 225 <= angle < 315:
            directions_row.append("South")
        else:
            directions_row.append("East")
    wind_directions.append(directions_row)

# Restrict wind direction prediction to cloud regions
cloud_regions = np.where(cloud_mask > 0)
for y, x in zip(*cloud_regions):
    direction = wind_directions[y][x]
    print(f"At position ({x}, {y}): Wind direction is {direction}")

# Optionally, you can visualize the wind directions on the SST image at cloud regions
# Convert the SST image to RGB for visualization
sst_image_rgb = cv2.cvtColor(sst_image, cv2.COLOR_GRAY2RGB)

# Draw arrows indicating wind directions on the SST image for cloud regions
arrow_length = 30
for y, x in zip(*cloud_regions):
    direction = wind_directions[y][x]
    if direction == "North":
        cv2.arrowedLine(sst_image_rgb, (x, y), (x, y - arrow_length), (0, 255, 0), 2)
    elif direction == "West":
        cv2.arrowedLine(sst_image_rgb, (x, y), (x - arrow_length, y), (0, 255, 0), 2)
    elif direction == "South":
        cv2.arrowedLine(sst_image_rgb, (x, y), (x, y + arrow_length), (0, 255, 0), 2)
    else:
        cv2.arrowedLine(sst_image_rgb, (x, y), (x + arrow_length, y), (0, 255, 0), 2)

# Display the SST image with wind directions at cloud regions
plt.imshow(cv2.cvtColor(sst_image_rgb, cv2.COLOR_BGR2RGB))
plt.title('SST Image with Wind Directions at Cloud Regions')
plt.axis('off')
plt.show()