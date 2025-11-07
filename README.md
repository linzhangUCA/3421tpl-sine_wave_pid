# Evaluate PID Controller

Let's build and tune a PID controller to regulate wheel's velocity.
Experiment with different combinations of **P**roportional **I**ntegral **D**erivative gains.
And find the best PID parameters.

## Get Started

### 1. Hardware Setup

Have one of your robot's motor and its encoder wired to appropriate components.

> [!TIP]
>
> You can refer to the [example](https://github.com/linzhangUCA/3421example-motor_control/blob/main/images/encoder_motor_pico.jpg).

### 2. Get PID Controlled Wheel Ready

1. Upload [motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/motor_driver.py),
[encoded_motor_driver.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/encoded_motor_driver.py),
[wheel_controller.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/wheel_controller.py)
to your Pico board.
2. Run [wheel_controller.py](https://github.com/linzhangUCA/3421example-motor_control/blob/main/wheel_controller.py) to verify if you can sense and control the motor velocity.

> [!TIP]
> Feel free to use your own code.

### 3. Collect Data

1. Change `REF_VEL`, `K_P`, `K_I`, `K_D` values in [collect_data.py](collect_data.py), and run the script with **MicroPython**.
2. Observe controller's performance.
If satisfied, download the [csv](https://en.wikipedia.org/wiki/Comma-separated_values) file to [data](data/) directory on your computer/laptop.
3. Remove the `.csv` file from the Pico board.

> [!IMPORTANT]
>
> [collect_data.py](collect_data.py) is only for good for MicroPython running on your Pico.

> [!TIP]
>
> - Thonny's "Plotter" panel (under the "View" menu) is very handy.
> - An example of the saved csv file name: `ref_0.4-pid_0.50_0.00_0.00.csv`
> - You can save multiple files on the Pico board, but it is highly recommended to clean up Pico's storage regularly.

### 4. Evaluate controller

1. Change `filename` to the downloaded csv file (e.g. `"ref_0.4-pid_0.50_0.00_0.00.csv"`) on line 11 in [evaluate.py](evaluate.py).
2. Run [evaluate.py](evaluate.py) with **Local Python** to log the metrics of your controller.

> [!IMPORTANT]
>
> [evaluate.py](evaluate.py) is only for good for Local Python running on your Laptop(computer).

> [!TIP]
> Install [matplotlib](https://matplotlib.org/), then uncomment specified sections in code to visualize measured velocity vs reference velocity.

## Requirements

### 1. (20%) Log baseline controller's performance using the tables below

> [!NOTE]
>
> - The baseline PID controller parameters: `P=0.50`, `I=0.00`, `D=0.00`.
> - Log "Steady State Velocity" with `mean(standard deviation)`, for example: `0.4012(0.0013)`.

### 2. (54%) Log improved controller's performance using the tables below

> [!NOTE]
>
> - Highlight the better performed controller's metrics using **bold** font.
> - Use the overall best performed PID parameters. You cannot change PID parameters for different reference velocities.
> - 2% will be taken off if the baseline controller outperformed the tuned controller on a metric.
You can lose up to 32% if the baseline outperformed tuned controller on every metric.

### 3. (10%) Write down the best PID parameters you've found. :point_down:

### 4. (16%) Upload your data to [data](data/) directory

> [!WARNING]
>
> Or, your logs will not be graded.

Tuned PID controller parameters: `P=?`, `I=?`, `D=?`.

| **Reference: 0.1 m/s** | **Baseline** | **Tuned** |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

| **Reference: 0.2 m/s** | **Baseline** | **Tuned** |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

| **Reference: 0.3 m/s** | **Baseline** | **Tuned** |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

| **Reference: 0.4 m/s** | **Baseline** | **Tuned** |
| :--- | ---: | ---: |
| Rise Time (seconds) | ?  | ? |
| Overshoot (%) | ?  | ? |
| Steady State Velocity (m/s) | ?  | ? |

## AI Policies

Please acknowledge AI's contributions follow the policies in the syllabus.
