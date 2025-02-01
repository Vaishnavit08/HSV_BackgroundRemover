# 🖼 Background Removal using OpenCV

## 📌 Overview
This project implements background removal using color-based masking with OpenCV and Python. It processes an image by detecting a region of interest (ROI) and applies a mask to remove the background efficiently.

## 🛠 Features
- 🎨 Converts an image to HSV color space
- 🖼 Extracts a region of interest (ROI) for color-based masking
- 🎭 Generates a histogram for accurate color matching
- 🔍 Applies filtering and thresholding for noise reduction
- ✂️ Removes the background using bitwise operations

## 📂 Installation
```bash
pip install opencv-python numpy
```

## 🚀 Usage
Run the script to process the images and remove the background:
```bash
python main.py
```

## 📸 Output
Include screenshots of your output images here:
![image](https://github.com/user-attachments/assets/0c19323e-b9ce-4b60-98a2-00c880f1d1ed)


## 📜 Explanation
1. **Reading the Image** 🖼
   - Loads and resizes the input image.
2. **Converting to HSV** 🎨
   - Converts the image from BGR to HSV color space.
3. **Extracting ROI** 🔍
   - Reads the second image (ROI) for color reference.
4. **Generating Color Histogram** 📊
   - Computes a histogram to match the ROI color range.
5. **Creating a Mask** 🎭
   - Uses `cv2.calcBackProject` to create a color-based mask.
6. **Filtering Noise** 🧹
   - Applies filtering and thresholding for cleaner results.
7. **Background Removal** ✂️
   - Merges the mask and applies bitwise operations to remove the background.

## 📬 Contact
For any queries or suggestions, feel free to reach out! 😊

