/*LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL
@编   写：龙邱科技
@使用平台：龙芯2K0301双龙mini派
@功能说明：电机驱动测试 Demo
@引脚配置：
    - 电机 1 (左): 脉冲 GPIO 81 (ATIM CH1), 方向 GPIO 21
    - 电机 2 (右): 脉冲 GPIO 82 (ATIM CH2), 方向 GPIO 22
QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ*/

#include <iostream>
#include <unistd.h>
#include "LQ_ATIM_PWM.hpp"
#include "LQ_HW_GPIO.hpp"

// 引脚定义
#define MOTOR_L_PWM_PIN  81
#define MOTOR_L_DIR_PIN  21
#define MOTOR_R_PWM_PIN  82
#define MOTOR_R_DIR_PIN  22

// PWM 参数
#define PWM_PERIOD       6400    // 周期
#define MAX_SPEED        5000    // 最大占空比限制 (0-10000)

// 全局硬件对象
AtimPwm *motor_l_pwm;
AtimPwm *motor_r_pwm;
HWGpio  *motor_l_dir;
HWGpio  *motor_r_dir;

/**
 * @brief 电机输出控制 (适配原 a240 项目逻辑)
 * @param leftspeed  左电机速度/占空比 (正数前进，负数后退)
 * @param rightspeed 右电机速度/占空比 (正数前进，负数后退)
 */
void motor_out(int leftspeed, int rightspeed)
{
    // 左电机方向逻辑 (GPIO 21)
    if (leftspeed >= 0) {
        motor_l_dir->SetGpioValue(1); // 对应原逻辑 lmotor_ctrl.setValue(1)
        motor_l_pwm->SetDutyCycle(leftspeed);
    } else {
        motor_l_dir->SetGpioValue(0); // 对应原逻辑 lmotor_ctrl.setValue(0)
        motor_l_pwm->SetDutyCycle(abs(leftspeed));
    }

    // 右电机方向逻辑 (GPIO 22)
    if (rightspeed >= 0) {
        motor_r_dir->SetGpioValue(0); // 对应原逻辑 rmotor_ctrl.setValue(0)
        motor_r_pwm->SetDutyCycle(rightspeed);
    } else {
        motor_r_dir->SetGpioValue(1); // 对应原逻辑 rmotor_ctrl.setValue(1)
        motor_r_pwm->SetDutyCycle(abs(rightspeed));
    }
}

int main()
{
    std::cout << "Starting 2K0301 Motor Test Demo..." << std::endl;

    // 1. 初始化方向引脚
    motor_l_dir = new HWGpio(MOTOR_L_DIR_PIN, GPIO_Mode_Out);
    motor_r_dir = new HWGpio(MOTOR_R_DIR_PIN, GPIO_Mode_Out);

    // 2. 初始化 PWM 引脚 (ATIM 控制器)
    // 参数: GPIO, 通道, 极性, 周期, 初始占空比
    motor_l_pwm = new AtimPwm(MOTOR_L_PWM_PIN, 1, LS_ATIM_INVERSED, PWM_PERIOD, 0);
    motor_r_pwm = new AtimPwm(MOTOR_R_PWM_PIN, 2, LS_ATIM_INVERSED, PWM_PERIOD, 0);

    // 3. 使能 PWM
    motor_l_pwm->Enable();
    motor_r_pwm->Enable();

    std::cout << "Motors Initialized. Running test sequence..." << std::endl;

    while (true) {
        // --- 前进 ---
        std::cout << "Moving Forward..." << std::endl;
        motor_out(2000, 2000);
        sleep(2);

        // --- 停止 ---
        std::cout << "Stopping..." << std::endl;
        motor_out(0, 0);
        sleep(1);

        // --- 后退 ---
        std::cout << "Moving Backward..." << std::endl;
        motor_out(-2000, -2000);
        sleep(2);

        // --- 停止 ---
        std::cout << "Stopping..." << std::endl;
        motor_out(0, 0);
        sleep(1);
        
        // --- 原地左转 ---
        std::cout << "Spin Left..." << std::endl;
        motor_out(-1500, 1500);
        sleep(2);
    }

    return 0;
}
