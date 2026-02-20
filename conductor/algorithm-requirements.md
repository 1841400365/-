# Algorithm Requirements Checklist

This document lists the specific algorithms that need to be implemented for the project.

## 1. Image Processing (Visual Perception)
- [ ] **Preprocessing:**
    -   Gaussian Blur / Median Filtering (Noise Reduction).
    -   Inverse Perspective Mapping (IPM) (Bird's Eye View - Optional but recommended).
    -   Lens Distortion Correction.
- [ ] **Feature Extraction:**
    -   Sobel / Canny Edge Detection.
    -   Hough Transform (Line Detection).
    -   Blob Detection (for color markers).
    -   ORB / FAST (Feature points, if needed for SLAM/Matching).

## 2. Target Recognition (AI/DL)
- [ ] **Object Detection:**
    -   Implement YOLOv5/v7 inference using OpenCV DNN module.
    -   Post-processing: Non-Maximum Suppression (NMS).
- [ ] **Target Tracking (Optional):**
    -   KCF (Kernelized Correlation Filters) or MOSSE for single object tracking.
    -   DeepSORT for multi-object tracking (Performance heavy).

## 3. Motion Control
- [ ] **Motor Control:**
    -   Incremental PID Controller (Speed Loop).
- [ ] **Steering Control:**
    -   Positional PD Controller (Steering Loop).
    -   Fuzzy PID (Adaptive gains based on error magnitude).
- [ ] **Sensor Fusion:**
    -   Complementary Filter / Kalman Filter (IMU Data Fusion for Angle estimation).

## 4. Path Planning & Strategy
- [ ] **Line Following:**
    -   Least Squares Fitting (Linear Regression) for path centerline.
- [ ] **Obstacle Avoidance:**
    -   Artificial Potential Field (APF) or Dynamic Window Approach (DWA).
    -   A* Algorithm (if map is known/built).

## 5. System Optimization
- [ ] **Memory Management:** Object pooling for images to reduce allocation overhead.
- [ ] **Concurrency:** Multi-threading (Vision Thread, Control Thread, Comm Thread).
