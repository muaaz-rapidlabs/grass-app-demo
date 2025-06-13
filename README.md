# 🥬 Grass Detection in Beetroot Truckloads

This desktop tool helps detect **green grass/weeds** in a truckload of **beetroot** using image analysis. It highlights grass patches and calculates the percentage of grass coverage in an uploaded image.

---

## 📸 Example Output

- Green areas (potential grass/weeds) are highlighted
- Bounding boxes show detected patches
- A % estimate of green coverage is calculated
- Option to download the highlighted image

---

## 🧠 Methodology

The tool uses a computer vision pipeline based on **OpenCV + HSV color thresholding**:

### 1. **Image Preprocessing**
- Image is converted to HSV color space (good for color filtering).
- HSV is more robust than RGB for lighting variations.

### 2. **Green Mask Detection**
- A range of green HSV values is defined:
  ```python
  lower_green = np.array([35, 40, 40])
  upper_green = np.array([85, 255, 255])

* Pixels in this range are considered potential grass.

### 3. **Highlighting**

* Detected green pixels are highlighted with a bright green overlay.
* Optional: Bounding boxes are drawn around large green patches using contours.

### 4. **Green Coverage Calculation**

* Total green pixels / total pixels gives the grass coverage percentage.

---

## 📁 Code Structure

```bash
project/
│
├── app.py         # Streamlit UI for running the detection
├── gui.py         # Desktop launcher using pywebview
├── dist/
│   └── gui.exe    # Compiled standalone app for Windows
│   └── app.py     # Streamlit UI for running the detection
```

---

## 🚀 How to Use (End User - No Python Required)

### ✅ Prerequisites

* Windows 10 or 11 (64-bit)

### 📦 Installation

1. Download the `dist/` folder or ZIP from release
2. Make sure `gui.exe` and `app.py` are in the **same folder**
3. Double-click `gui.exe`
4. The app will open in a small desktop window
5. Upload a beetroot image and view the analysis

> ℹ️ Internet is **not required** to run.

---

## ⚙️ Developer Setup (With Python)

### 🐍 Python Environment Setup

1. Create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install streamlit opencv-python-headless pillow numpy pywebview
   ```

3. Run locally:

   ```bash
   streamlit run app.py
   ```

---

## 🖥️ Convert to Desktop App (EXE) with PyInstaller

1. Install pyinstaller:

   ```bash
   pip install pyinstaller
   ```

2. Compile:

   ```bash
   pyinstaller --onefile --windowed gui.py
   ```

3. Find the output `.exe` in the `dist/` folder

> 📦 Make sure `app.py` is in the same folder as the `.exe` when you run it.

---

## 🛠 `gui.py` - How It Works

```python
import os
import webview

# Launch the Streamlit app in a hidden terminal
os.system("start /B streamlit run app.py --server.port 8501")

# Launch pywebview in a desktop window
webview.create_window("Grass Detection", "http://localhost:8501")
webview.start()
```

* Starts Streamlit server in background
* Opens a small native window using `pywebview`

---

## 📦 Future Improvements

* Use ML model for more accurate segmentation
* Add support for multiple image uploads
* Export PDF reports or Excel summaries

---

## 📧 Contact

Feel free to contact \[Muaaz Ahmad] at \[[muaaz.ahmad@rapidlabs.ai](mailto:muaaz.ahmad@rapidlabs.ai)] for collaboration, bug reports, or feature requests.

---
