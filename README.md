#  Automatic Number Plate Detection

This project detects vehicle license plates in images using OpenCV for image processing and EasyOCR for text recognition. It's designed for Indian number plate formats and uses contour detection to localize the plate region.

## 🔧 How It Works

1. Load the input image
2. Apply bilateral filtering and Canny edge detection
3. Detect contours to locate the number plate
4. Crop and extract the plate region
5. Use EasyOCR to read the text from the cropped plate
6. Display the annotated result

## ▶How to Run

1. Place your test image in a folder called `sample_images/`
2. Run the script:

```bash
python number_plate_detection.py
