# Optional for Colab only
# !pip install easyocr
# !pip install imutils

import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as plt

# Load the image (adjust path if needed)
img = cv2.imread('sample_images/kerala_car.jpeg')  # Make sure the file exists
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Preprocessing
bfilter = cv2.bilateralFilter(gray, 11, 17, 17)
edged = cv2.Canny(bfilter, 30, 200)

# Find contours
keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(keypoints)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

# Approximate number plate region
location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour, 10, True)
    if len(approx) == 4:
        location = approx
        break

if location is not None:
    # Create mask and crop
    mask = np.zeros(gray.shape, np.uint8)
    cv2.drawContours(mask, [location], 0, 255, -1)
    x, y = np.where(mask == 255)
    x1, y1 = np.min(x), np.min(y)
    x2, y2 = np.max(x), np.max(y)
    cropped_image = gray[x1:x2+1, y1:y2+1]

    # OCR
    reader = easyocr.Reader(['en'])
    result = reader.readtext(cropped_image)
    text = result[0][-2] if result else "No text found"

    # Draw result
    font = cv2.FONT_HERSHEY_SIMPLEX
    annotated = cv2.putText(img, text, (location[0][0][0], location[1][0][1]+60),
                            font, 1, (0,255,0), 2, cv2.LINE_AA)
    annotated = cv2.rectangle(img, tuple(location[0][0]), tuple(location[2][0]), (0,255,0), 3)

    # Display
    plt.imshow(cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB))
    plt.title("Detected Number Plate")
    plt.axis("off")
    plt.show()
else:
    print("Number plate not found!")


