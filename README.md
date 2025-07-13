# Hematological Image Segmentation using Connected Component Labeling

## Overview

This project implements a full pipeline for segmenting **White Blood Cells (WBCs)** from hematological images using **8-connected Component Labeling (CCA)**. The system isolates the WBCs from the background and further separates the **cytoplasm** and **nucleus**. Segmentation accuracy is evaluated using the **Dice Coefficient** metric.

The code is written in python and organized into modular scripts for preprocessing, segmentation, and evaluation. Since this was done for an image processing course, there was a requirement to make all functions from scratch where possible instead of using their built-in counterparts. Replacing the built-in functions would make the program more efficient. 

---

## Features implemented

- 1. WBC Isolation using CCA (8-connectivity)
- 2. Segmentation of WBC into Cytoplasm and Nucleus using:
  - Power-law contrast enhancement
  - Averaging blur filter
  - Thresholding based on pixel intensity analysis
- 3. Dice Coefficient computation for:
  - Background
  - Cytoplasm
  - Nucleus

---

## Project Structure
```plaintext
hematological-segmentation-using-cca/
│
├── src/
│ ├── preprocessing.py # Image enhancement and blurring
│ ├── cca.py # Connected component labeling
│ ├── segmentation.py # Thresholding and Detecting the Largest Object
│ └── metrics.py # Dice coefficient computation
│
├── main.py # Main pipeline 
├── README.md # This file
├── .gitignore
└── LICENSE #( MIT License)
```

## File Descriptions

### `main.py`
Runs the full segmentation pipeline:
1. Loads image and ground truth
2. Applies preprocessing
3. Runs CCA and thresholding
4. Evaluates segmentation

### `src/preprocessing.py`
- `conv(img, mask_size, mask_val)`: Applies an averaging blur, can be replaced by cv2.blur
- `power_law(img, gamma)`: Applies gamma correction for contrast enhancement

### `src/cca.py`
- `ccn8(img)`: Labels connected components using 8-connectivity

### `src/segmentation.py`
- `thresh(img, value)`: Binary thresholding
- `largest_object(img, value)`: Keeps only the largest object and assigns a specific label

### `src/metrics.py`
- `dice_coefficient(img, mask, val)`: Computes Dice score for a specific label

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/yourusername/hematology-segmentation-cca.git
cd hematology-segmentation-cca
```

2. Access datasets: https://drive.google.com/drive/folders/1DUDnYXZQF6zSZDl0RJIsdo8lqiZOJQoV?usp=sharing
##### The dataset consists of paired microscopic images and manually annotated ground truth masks. Each image has a corresponding labeled mask where: 
#### - White region represents the nucleus of the WBC. 
#### - Gray region represents the cytoplasm of the WBC. 
#### - Black region represents the background. 
##### Each image is labeled pixel-wise, enabling precise segmentation.

3. Run main.py.

## Dependencies

This project requires the following Python packages:
- numpy
- opencv-python
- matplotlib

```bash
pip install numpy opencv-python matplotlib
```

##### License
This project is licensed under the MIT License.

##### Hit me up at rijaakhalid@gmail.com for any queries!




