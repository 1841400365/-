# Development Tracks

## Active Tracks

### 🚀 System Initialization
- [x] **Environment Setup:** Fix Cross-Compiler paths (Done).
- [ ] **Hardware Verification:** Test all drivers (Screen, Camera, IMU, Motors) on the 2K0301.
    - *Action:* Compile and run basic "Hello World" tests for each peripheral.

## Planned Tracks

### 👁️ Vision System Development
- [ ] **Image Preprocessing:** Implement Grayscale, Binarization, and Denoising.
- [ ] **Track Recognition:** Implement algorithm to find track centerline and curvature.
- [ ] **Model Deployment:** Convert YOLO model to ONNX and run with OpenCV DNN.

### 🚗 Control System Development
- [ ] **Motor Open-Loop:** Verify PWM output and motor rotation direction.
- [ ] **Speed Closed-Loop:** Implement PID encoder feedback.
- [ ] **Steering Control:** Map vision error to servo angle.

### 🧠 Integration & Strategy
- [ ] **Main Loop Logic:** Combine Vision -> Planning -> Control.
- [ ] **Competition Logic:** Handle Start/Stop signals, Special Elements (Crossroads).

### 🧪 Optimization & Testing
- [ ] **Latency Profiling:** Measure time cost of Vision vs Control.
- [ ] **Parameter Tuning:** PID Tuning, Fuzzy Logic Rules adjustment.
