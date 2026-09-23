# 🌱 Plant Doctor — Color-Based Plant Health Analysis

> **An Image Processing project that analyzes plant leaves using RGB and HSV color spaces to detect visible discoloration and provide a simple plant health indication.**

---

## 🌿 About the Project

**Plant Doctor** is a color image processing system designed to analyze the visual appearance of plant leaves.

The system takes a leaf image as input and processes its colors to identify **green, yellow, and brown regions**. By calculating the percentage of each color present on the leaf, the system can highlight areas of visible discoloration and provide a simple observation about the leaf's condition.

### 🎯 Main Idea

```text
📷 Leaf Image
      ↓
🎨 Color Processing
      ↓
🔍 Color Segmentation
      ↓
📊 Percentage Analysis
      ↓
🩺 Plant Health Indication
```

---

## ✨ Features

* 📸 Upload a plant leaf image
* 🎨 Convert images between RGB and HSV
* 🔴🟢🔵 Separate RGB channels
* 🌈 Analyze leaf colors using HSV
* 🟢 Detect green regions
* 🟡 Detect yellow regions
* 🟤 Detect brown regions
* 📊 Calculate color percentages
* 🔍 Identify visible discoloration
* 🖼️ Highlight detected problem areas
* 🩺 Generate a simple plant health observation
* ✨ Apply image enhancement
* 🎨 Demonstrate RGB, HSV and CMYK color representations
* 💻 Interactive Streamlit interface

---

# 🧠 How It Works

The project is divided into four major stages.

### 1️⃣ Image Processing

**Module:** `image_processing.py`

The input leaf image is processed using basic color image processing techniques.

```text
Input Leaf
    ↓
BGR → RGB
    ↓
RGB Channel Separation
    ↓
RGB → HSV
    ↓
Processed Image
```

The module provides:

* RGB image
* Red channel
* Green channel
* Blue channel
* HSV image

---

### 2️⃣ Color Segmentation

**Module:** `segmentation.py`

The HSV image is analyzed to identify different color regions.

The system creates separate masks for:

🟢 **Green**

🟡 **Yellow**

🟤 **Brown**

```text
HSV Image
    │
    ├── 🟢 Green Mask
    ├── 🟡 Yellow Mask
    └── 🟤 Brown Mask
```

Noise can also be removed from the masks using basic image processing techniques.

---

### 3️⃣ Analysis & Problem Detection

**Module:** `analysis.py`

This is the **analysis layer** of the project.

The three color masks are used to calculate the percentage of each color present in the leaf.

For example:

```text
🟢 Green   → 78%
🟡 Yellow  → 15%
🟤 Brown   → 7%
```

The yellow and brown regions are then combined to identify areas of visible discoloration.

```text
Yellow Mask
     +
Brown Mask
     ↓
Problem Mask
     ↓
Highlighted Leaf
```

The system then generates a simple observation based on the detected discoloration.

Example:

> **"Noticeable discoloration detected."**

⚠️ The result is a **visual image-processing indication**, not a medical or scientific diagnosis of plant disease.

---

### 4️⃣ User Interface

**Module:** `app.py`

The Streamlit application connects all the modules into a single interface.

The user can:

1. Upload a leaf image
2. View the original image
3. View processed images
4. View detected color regions
5. See color percentages
6. View highlighted problem areas
7. Read the generated observation

---

# 🏗️ Project Structure

```text
Plant-Doctor/
│
├── 📄 app.py
├── 📄 image_processing.py
├── 📄 segmentation.py
├── 📄 analysis.py
├── 📄 requirements.txt
├── 📄 README.md
│
├── 📁 images/
│   ├── healthy_leaf.jpg
│   ├── yellow_leaf.jpg
│   └── brown_leaf.jpg
│
└── 📁 outputs/
    ├── masks/
    └── highlighted/
```

---

# 🔬 Color Models Used

## 🔴 RGB

RGB represents an image using three color channels:

* **R — Red**
* **G — Green**
* **B — Blue**

It is useful for displaying and manipulating digital images.

---

## 🌈 HSV

HSV represents color using:

* **H — Hue**
* **S — Saturation**
* **V — Value**

HSV is particularly useful for this project because colors such as green, yellow, and brown can be separated using ranges of hue and saturation.

```text
RGB Image
    ↓
   HSV
    ↓
Color Range Selection
    ↓
Color Masks
```

---

## 🖨️ CMYK

CMYK represents colors using:

* **C — Cyan**
* **M — Magenta**
* **Y — Yellow**
* **K — Black**

CMYK is mainly associated with printing.

In Plant Doctor, CMYK can be demonstrated as another representation of the same leaf colors while HSV is used for practical color segmentation.

---

# 📊 Example Analysis

A sample analysis could produce:

| Color     | Percentage |
| --------- | ---------: |
| 🟢 Green  |        78% |
| 🟡 Yellow |        15% |
| 🟤 Brown  |         7% |

### 🩺 Observation

**Possible visible signs of plant stress due to noticeable discoloration.**

The highlighted image shows the regions detected as yellow or brown.

---

# 🛠️ Technologies Used

| Technology    | Purpose                      |
| ------------- | ---------------------------- |
| 🐍 Python     | Core programming             |
| 👁️ OpenCV    | Image processing             |
| 🔢 NumPy      | Pixel and array calculations |
| 📊 Matplotlib | Image visualization          |
| 💻 Streamlit  | Web interface                |

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Plant-Doctor.git
```

### 2. Open the project

```bash
cd Plant-Doctor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

---

# 📦 Requirements

Example `requirements.txt`:

```text
opencv-python
numpy
matplotlib
streamlit
Pillow
```

---

# 🚀 Future Improvements

The project can be extended with:

* 🌱 Plant disease classification
* 🤖 Machine Learning-based disease detection
* 📷 Real-time camera analysis
* 🌿 Support for different plant species
* 📈 Historical health tracking
* 🔬 More detailed leaf feature extraction
* ✨ Advanced brightness and contrast enhancement
* 🎨 Interactive RGB/HSV/CMYK color inspector
* 📊 Health analysis dashboard
* 📱 Mobile-friendly interface

---

# ⚠️ Limitations

The current system is based primarily on **color analysis**.

Yellow or brown regions may occur because of several different factors such as:

* Natural aging
* Lighting conditions
* Nutrient deficiency
* Environmental stress
* Physical damage
* Disease

Therefore, the system should be considered a **visual screening and image-processing tool**, rather than a definitive plant disease diagnosis.

---

# 👩‍💻 Team Contributions

| Member           | Responsibility               |
| ---------------- | ---------------------------- |
| **Debasmita** 🧠 | Core Image Processing        |
| **Adrija** 🎨    | Color Segmentation           |
| **Rishika** 🔍   | Analysis & Problem Detection |
| **Tanisha** 💻   | UI & Integration             |

### 🔗 Pipeline

```text
Debasmita
Image → HSV
    ↓
Adrija
HSV → Color Masks
    ↓
Rishika
Masks → Analysis
    ↓
Tanisha
Everything → Streamlit App
```

---

# 🎯 Project Goal

The goal of **Plant Doctor** is to demonstrate how fundamental **Color Image Processing techniques** can be applied to a practical real-world problem.

Instead of immediately relying on complex AI models, the project focuses on understanding how image representation, color segmentation, pixel analysis, and visualization can be combined to extract useful information from a plant leaf.

---

## 🌱 Plant Doctor

### *See the color. Detect the change. Understand the leaf.*

---

⭐ **If you find this project interesting, consider giving the repository a star!**
