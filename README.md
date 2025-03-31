# Satellite Based Wind and Cloud Pattern Detection System
## Index
1. [Overview](#overview)
2. [Features](#features)
3. [Data Collection Process](#data-collection-process)
4. [Implementation](#implementation)
5. [Results](#results)
6. [Example SST Images](#example-sst-images)
8. [Future Work](#future-work)

## Overview <a name="overview"></a>
This project analyzes Sea Surface Temperature (SST) data to estimate wind directions, particularly focusing on cloud-covered regions. The implementation combines computer vision techniques with meteorological data processing to identify cloud patterns and calculate temperature gradients for wind direction prediction.

## Features<a name="features"></a>
- 🌥️ Cloud detection using adaptive thresholding and morphological operations
- 🌡️ Temperature gradient calculation with Sobel filters
- 🧭 Wind direction approximation based on gradient vectors
- 📊 Visualization of results with directional arrows
- ☁️ Focused analysis on cloud-affected regions

## Data Collection Process<a name="data-collection-process"></a>
To gather relevant satellite imagery and environmental data, the following tools and software were used:

1. **Orbitron** - A satellite tracking software that provides real-time tracking of various satellites to predict their visibility and communication windows.
2. **AirSharp SDR** - A software-defined radio (SDR) tool used to receive raw satellite signals, which are then decoded to obtain useful meteorological data.
3. **WXtoImg** - A widely used software for decoding NOAA APT (Automatic Picture Transmission) signals to generate SST images.
4. **NOAA Weather Satellites** - These satellites provide high-resolution thermal imaging data for SST analysis.
5. **Python with OpenCV and NumPy** - Used for processing and analyzing SST images.

## Implementation<a name="implementation"></a>
The THAPSAT project follows these steps:

1. **Data Acquisition**: SST data is collected using satellite sources and SDR tools.
2. **Preprocessing**: The images are converted to grayscale and enhanced using Gaussian blurring.
3. **Cloud Detection**: Adaptive thresholding and morphological operations are applied to segment cloud regions.
4. **Gradient Computation (Sobel Filter)**:
   - The Sobel filter is used to calculate the temperature gradient in the SST image.
   - It helps to find the edges and contours in the image.
5. **Wind Direction Estimation (Direction Approximation)**:
   - The code calculates the magnitude and angle of the gradient vectors.
   - The angle in radians is converted to degrees and shifted to the range of [0, 360].
   - The adjusted wind direction thresholds are used to approximate the wind directions based on the gradient angles.
6. **Visualization**:
   - **Thresholding**: After calculating the gradient, a threshold is applied to segment the cloud region from the SST image.
   - Thresholding separates image pixels into two classes based on intensity values, helping to identify cloud regions.
   - Finally, the wind directions are visualized on the SST image using arrowed lines, highlighting the wind direction for each pixel in the cloud region.

## Results<a name="results"></a>
The analysis produces SST images with cloud-detected regions and directional arrows indicating wind movement. These results aid in better understanding atmospheric dynamics and weather forecasting.

## Example SST Images<a name="example-sst-images"></a>
<div style="display: flex; justify-content: space-around;">
  <img src="static\sst image with wind direction.jpg" width="40%" height="40%">
  <img src="static\sst image with wind directions in cloud regions.jpg" width="59%" height="59%">
</div>

## Future Work<a name="future-work"></a>
- Enhance cloud detection accuracy using deep learning.
- Improve wind direction estimation using additional meteorological parameters.
- Integrate real-time data collection for live analysis.




