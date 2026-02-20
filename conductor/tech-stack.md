# Technology Stack

## Core Platform
-   **SoC:** Loongson 2K0301 (LoongArch64)
-   **OS:** Linux (Embedded)
-   **Toolchain:** Loongson GNU Toolchain 8.3 (`/opt/loongsonToolchain`)

## Software Frameworks

### Computer Vision & AI
-   **OpenCV 4.10.0:**
    -   `Core`: Basic image structures.
    -   `ImgProc`: Color conversion (RGB->HSV), Thresholding, Canny Edge, Morphology.
    -   `DNN`: Running inference for YOLO models.
-   **Deep Learning Models:**
    -   **Detection:** YOLOv5-Nano or YOLO-Fastest (optimized for embedded CPU).
    -   **Tracking:** DeepSORT or MOSSE (if multi-object tracking is needed).

### Control & Navigation
-   **Control Algorithms:**
    -   **PID:** Incremental & Positional PID.
    -   **Fuzzy Logic:** For adaptive steering control.
-   **Path Planning:**
    -   **A* (A-Star):** For obstacle avoidance / pathfinding.
    -   **Pure Pursuit:** For geometric path tracking.

## Hardware Drivers
-   **Camera:** V4L2 Driver / Custom `WW_CAMERA` module.
-   **Sensors:**
    -   **IMU:** MPU6050 / ICM42605 (I2C).
    -   **ToF:** VL53L0X (Distance measurement).
-   **Actuators:**
    -   **Motors:** PWM controlled DC Motors.
    -   **Servo:** PWM controlled Steering Servo.

## Development Tools
-   **Build System:** CMake.
-   **Debugging:** GDB (gdb-multiarch), Serial Logs.
-   **Visualization:** Python/Matplotlib (offline analysis), LCD Display (real-time).
