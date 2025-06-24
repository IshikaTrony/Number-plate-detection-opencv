#  Automatic Number Plate Detection using OpenCV & EasyOCR

This project detects vehicle number plates from images using OpenCV for image processing and EasyOCR for character recognition. It is designed with Indian plate formats in mind and can be extended for traffic surveillance, law enforcement, or parking automation.

---

##  Features

- Detects number plate area using edge detection and contour analysis
- Extracts characters using EasyOCR
- Works on Indian white and yellow plates
- End-to-end visualization with Matplotlib

---

## 🛠 Tech Stack

- **Language**: Python
- **Libraries**:
  - OpenCV (image processing)
  - EasyOCR (text extraction)
  - imutils (contour processing)
  - NumPy (array manipulation)
  - Matplotlib (image display)

---

## 📁 Project Structure

```
number-plate-detection-opencv/
├── README.md
├── requirements.txt
├── number_plate_detection.py
└── sample_images/
    └── kerala_car.jpeg
```

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/IshikaTrony/number-plate-detection-opencv.git
   cd number-plate-detection-opencv
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make sure your image is placed inside the `sample_images/` folder.

4. Run the script:
   ```bash
   python number_plate_detection.py
   ```

---

## 📷 Sample Output
_

---
---

## 📚 References

- Sulaiman, N. (2013). *Development of automatic vehicle plate detection system.*
- Prabhakar, P. (2014). *Automatic vehicle number plate detection and recognition.*

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
