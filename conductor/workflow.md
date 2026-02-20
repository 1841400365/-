# Development Workflow

## Build & Deploy
1.  **Build:** `./build.sh` (Compiles the project).
2.  **Transfer:** Use `scp` or USB drive to move `output/main` to the 2K0301 board.
3.  **Run:** Execute `./main` on the board (ensure permissions: `chmod +x main`).

## Debugging Strategy
-   **Visual Debugging:** Draw detection results (bounding boxes, centerlines) on the LCD screen.
-   **Log Debugging:** Use `printf` or a logging library to output PID values and State info to UART.
-   **Image Logging:** Save failed recognition frames to SD card for offline analysis.

## Git Workflow
-   Commit specifically for each algorithm implementation (e.g., "feat: add PID controller", "feat: add YOLO inference").
