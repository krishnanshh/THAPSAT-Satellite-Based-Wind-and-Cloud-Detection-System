import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the SST data
sst_image = cv2.imread('s3.jpg', cv2.IMREAD_GRAYSCALE)

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

# Visualize the wind directions on the SST image
# Convert the SST image to RGB for visualization
sst_image_rgb = cv2.cvtColor(sst_image, cv2.COLOR_GRAY2RGB)

# Draw arrows indicating wind directions on the SST image
arrow_length = 30
for y in range(0, sst_image.shape[0], 25):
    for x in range(0, sst_image.shape[1], 25):
        direction = wind_directions[y//10][x//10]
        if direction == "North":
            cv2.arrowedLine(sst_image_rgb, (x, y), (x, y - arrow_length), (0, 255, 0), 2, tipLength = 0.3)
        elif direction == "West":
            cv2.arrowedLine(sst_image_rgb, (x, y), (x - arrow_length, y), (0, 255, 0), 2, tipLength = 0.3)
        elif direction == "South":
            cv2.arrowedLine(sst_image_rgb, (x, y), (x, y + arrow_length), (0, 255, 0), 2, tipLength = 0.3)
        else:
            cv2.arrowedLine(sst_image_rgb, (x, y), (x + arrow_length, y), (0, 255, 0), 2, tipLength = 0.3)

# Display the original SST image
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.imshow(sst_image, cmap='gray')
plt.title('SST Image')
plt.axis('off')

# Display the SST image with wind directions
plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(sst_image_rgb, cv2.COLOR_BGR2RGB))
plt.title('SST Image with Wind Directions')
plt.axis('off')

plt.tight_layout()
plt.show()