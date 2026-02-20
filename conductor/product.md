# Product Definition: 走马观碑 (Walking Horse & Watching Monument)

## Overview
**Project Name:** LQ_2K0301_Zoumabei
**Competition:** 21st National University Smart Car Race (21届全国大学生智能汽车竞赛)
**Category:** Walking Horse and Watching Monument (走马观碑)
**Platform:** Loongson 2K0301 (龙芯2K0301)

## Competition Context
The "Walking Horse and Watching Monument" category challenges the smart car to navigate a track autonomously while identifying specific targets ("monuments") along the way.

### Core Objectives
1.  **High-Speed Navigation:** Rapidly traverse the designated track (likely involving visual line following or electromagnetic guidance).
2.  **Accurate Recognition:** Correctly identify and classify targets (Images, AprilTags, or Objects) placed alongside the track.
3.  **Precise Control:** Maintain stability during high-speed turns and precise stops/actions upon target detection.

## Key Features

### Vision System
-   **Track Recognition:** Identify track boundaries, centerlines, and special elements (crossroads, turns) using Computer Vision.
-   **Target Detection:** Real-time detection of "monuments" using Deep Learning (YOLO family) or Classical CV.
-   **Color Recognition:** Distinguish specific color markers or zones.

### Motion Control
-   **Dual-Loop Control:**
    -   **Speed Loop:** PID control for motor speed stability.
    -   **Steering Loop:** PD/Fuzzy PID control for steering servo based on error signals (visual/EM).
-   **Dynamic Obstacle Avoidance:** (If applicable) Real-time path replanning using ultrasonic/ToF sensors.

### System Architecture
-   **Processor:** Loongson 2K0301 (Main Controller & Vision Processing).
-   **Sensor Fusion:** Combining Camera data (Vision) with IMU (Posture) and Encoders (Speed).

## Performance Goals
-   **Frame Rate:** Vision processing > 30 FPS.
-   **Latency:** Control loop < 10ms.
-   **Recognition Accuracy:** > 95%.
