# Signature Verification System 🖋️

This project is a Signature Verification System developed using Python, OpenCV, and Streamlit. It uses keypoint detection and feature matching techniques to determine whether a test signature matches a reference signature.

---

## 📌 Aim

To build an intelligent system capable of verifying handwritten signatures by comparing structural features extracted from images using keypoints and descriptors. This can be applied in secure identity verification scenarios like banking, official documentation, and form validation.

---

## 🧠 How It Works

The system uses the ORB (Oriented FAST and Rotated BRIEF) algorithm to extract features from both reference and test signatures and compares them using a Brute Force Matcher. The similarity score is based on how well the keypoints match.

---

## ✅ Procedure

### 1. Preprocessing the Signatures
- Images are converted to grayscale and thresholded using binary thresholding to focus on the signature's shape and eliminate background noise.

### 2. Keypoint Detection & Feature Extraction
- **Keypoints** are specific, unique points like corners or stroke intersections.
- **ORB Algorithm** is used to detect these keypoints and compute **descriptors** — vectors representing the local neighborhood of each keypoint.

### 3. Signature Matching
- Descriptors are compared using **Brute Force Matcher** with Hamming distance.
- The number of matches and their ratio with the total keypoints is calculated.

### 4. Decision Making
- If the match ratio > 0.7 (can be adjusted), the system infers that the signatures match.
- Otherwise, they are considered significantly different.

### 5. Visualization
- Optionally, the user can view matched keypoints to understand how well the signatures align.

---

## 🔍 Key Concepts

### 🔹 Keypoints
Distinctive points in an image (e.g., edges, corners). They help in understanding structural patterns in signatures.

### 🔹 Descriptors
Numerical vectors that describe the area around each keypoint for easy comparison.

### 🔹 ORB (Oriented FAST and Rotated BRIEF)
A fast and efficient algorithm that detects keypoints and computes binary descriptors, suitable for real-time applications.

### 🔹 Brute Force Matcher
Compares each descriptor from one image with all descriptors in another to find the best matches.

---

## 📊 Inference

- A **high match ratio** (e.g., > 0.7) indicates a strong similarity between the reference and test signatures.
- A **low match ratio** suggests structural dissimilarity, likely indicating a forgery.

### Example Output:
- Reference Keypoints: 120  
- Test Keypoints: 115  
- Matches Found: 100  
- **Match Ratio:** 0.83  
- **Conclusion:** The signatures match well.

---

## 🛠️ Tech Stack

- **Python**
- **OpenCV**
- **Streamlit**
- **PIL (Pillow)**
- **NumPy**

---

## ▶️ How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
