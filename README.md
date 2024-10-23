# Machine Vision Mask Detection 

This project implements a real-time mask color detection system using computer vision techniques with OpenCV. It detects the presence of different colored masks, including **blue (surgical mask)**, **white (KN95 mask)**, and **black (surgical mask)**, by analyzing frames captured from a webcam or video input. The project processes video frames to highlight and label detected masks based on their color.

## Features
- **Real-Time Detection**: Processes live video from a webcam or video file input.
- **Mask Color Detection**: Identifies blue, white, and black colored masks using color filtering in the HSV space.
- **Contours and Boundaries**: Draws rectangles around the detected masks and displays text labels.
- **Adjustable Parameters**: Provides trackbars to adjust thresholds for Canny edge detection.

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

Clone
To get started, clone the repository to your local machine:

git clone https://github.com/your-username/mask-detection-project.git
cd mask-detection-project

Usage
Webcam Mode
To run the mask detection via webcam, execute the following command:
