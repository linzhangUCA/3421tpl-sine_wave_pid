# Evaluate PID Controller

Experiment with different **P**roportional **I**ntegral **D**erivative parameters.
Test varied combinations of these parameters and evaluate each controller's performance.

## Workflow

### 1. Hardware Setup

Have one of your robot's motor and its encoder wired to appropriate components.
You can refer to the [example](https://github.com/linzhangUCA/3421example-motor_control/blob/main/images/encoder_motor_pico.jpg).

### 2. Set PID Controller Ready

1. Upload [motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/motor_driver.py),
[encoded_motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/encoded_motor_driver.py),
[wheel_controller.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/wheel_controller.py)
to your Pico board.
2. Run [wheel_controller.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/wheel_controller.py) to verify if you can sense and control the motor velocity.

> [!TIP]
>
> Feel free to use your own code.

### 3. Collect Data

1. Change `REF_VEL`, `K_P`, `K_I`, `K_D` values in [collect_data.py](collect_data.py), and run the script with **MicroPython**.
2. Download the [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file to the [data](data/) directory on your computer.
3. Remove the `.csv` file from the Pico board.

> [!IMPORTANT]
>
> [collect_data.py](collect_data.py) is only for good for MicroPython running on your Pico.

> [!TIP]
>
> - An example of the saved csv file name: `ref_0.4-pid_0.50_0.00_0.00.csv`
> - You can save multiple files on the Pico board, but it is highly recommended to clean up Pico's storage regularly.
> - The "Plotter" under the "View" menu in Thonny is very handy.

### 4. Evaluate controller

1. Change `filename` to the downloaded csv file (e.g. `"ref_0.4-pid_0.50_0.00_0.00.csv"`) on line 11 in [evaluate.py](evaluate.py).

> [!IMPORTANT]
>
> [evaluate.py](evaluate.py) is only for good for Local Python running on your Laptop(computer).

## Requirements

### 1. (100%) State the best PID parameters you've found. :point_down:

> The baseline controller PID parameters: `P=0.50`, `I=0.00`, `D=0.00`.

- Improved controller PID parameters: `P=?`, `I=?`, `D=?`.

| **Reference: 0.1 m/s** | **Baseline** | **Improved** |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

| **Reference: -0.2 m/s** | **(Baseline)** P=0.50, I=0.00, D=0.00  | **(Improved)** P=?, I=?, D=? |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

| **Reference: -0.3 m/s** | **(Baseline)** P=0.50, I=0.00, D=0.00  | **(Improved)** P=?, I=?, D=? |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

| **Reference: 0.4 m/s** | **(Baseline)** P=0.50, I=0.00, D=0.00  | **(Improved)** P=?, I=?, D=? |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

## AI Policies

Please acknowledge AI's contributions follow the policies in the syllabus.
