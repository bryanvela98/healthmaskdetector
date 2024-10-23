# Machine Vision Mask Detection 

This project implements a real-time mask color detection system using computer vision techniques with OpenCV. It detects the presence of different colored masks, including **blue (surgical mask)**, **white (KN95 mask)**, and **black (surgical mask)**, by analyzing frames captured from a webcam or video input. The project processes video frames to highlight and label detected masks based on their color.

## Features
- **Real-Time Detection**: Processes live video from a webcam or video file input.
- **Mask Color Detection**: Identifies blue, white, and black colored masks using color filtering in the HSV space.
- **Contours and Boundaries**: Draws rectangles around the detected masks and displays text labels.
- **Adjustable Parameters**: Provides trackbars to adjust thresholds for canny edge detection.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Make sure you have the following installed:
- Python 3.11
- OpenCV
- Numpy
- Matplotlib (optional for graphing)

You can install the dependencies using pip:

```bash
pip install numpy opencv-python matplotlib

## Clone
To get started, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/mask-detection-project.git
cd mask-detection-project

## Usage

### Webcam Mode

To run the mask detection via webcam, execute the following command:

```bash
python mask_detection_webcam.py

### Video File Mode
To process a sample video for mask detection, use:

```bash
python mask_detection_video.py

### Real-time Color Mask Detection
To process a sample video for mask detection, use:

```bash
python color_mask_detection.py

### Contributing
Feel free to submit issues or pull requests if you would like to improve the project.
