# PID Controlled Sinusoidal Velocity Regulation 

## Objetives
- Practice **P**roportional **I**ntegral **D**erivative control policy to regulate a motor's velocity.
- Collect wheel's motion data.
- Evaluate controller's performance.

## Requirements
Find the sections wrapped by the following comments. 
```python
### START CODING HERE ###

### END CODING HERE ###
```
Finish the provided python scripts to achieve the following goals. 

### 1. (60%) Collect PID Control Data
Complete [pid_sine_test.py](pid_sine_test.py) to achieve following requests.
1. (50%) Tune PID gains so that the actual velocity can approach to the target as quickly and closely as possible.
2. (10%) Upload the data from the best performed controller by uncommenting the last 3 lines in [pid_sine_test.py](pid_sine_test.py).

#### Hints
- [Matplotlib](https://matplotlib.org/) installation
```console
# Run following line in terminal
pip install matplotlib --break-system-packages
```

### 2. (40%) Mean Squared Error Evaluation 
Mean squared error (MSE) is a metric used to measure the average squared difference between two variables.
We can employ such a metric to measure the difference between the wheel's target velocity and actual velocity.
And such a metric can serve as an indicator of the PID controller's performance.

During the data collection process, $T$ measurements are taken to probe/sample the wheel's actual velocity.
Each measurement is taken at a certian moment $t_i$, where $i \in {0, 1, 2, \dots, T}$.
Let velocity of the wheel at moment $t_i$ be $v_i$ and the actual velocity at the same moment to be $\hat{v}_i$.
The MSE between the target and the actual wheel velocity in this control process can be written as,

$$e_{MSE} = \frac{1}{T} \sum_{i=0}^T (v_i - \hat{v}_i)^2$$

1. (30%) Complete the code in [evaluation.py](evaluation.py) to compute the MSE of your PID controller. You'll need to figure out the correct values for $T$, $v_i$, and $\hat{v}_i$
2. (10%) Upload the velocity comparison figure to this repository.

## AI Policies
Please acknowledge AI's contributions follow the policies in the syllabus.
