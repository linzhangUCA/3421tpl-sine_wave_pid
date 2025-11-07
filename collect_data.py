"""
Run this script with MicroPython(Raspberry Pi Pico)
"""

from time import sleep
from wheel_controller import WheelController
from machine import Pin


### TUNE PID GAINS BELOW ###
REF_VEL = 0.1
K_P = 0.5
K_I = 0.0
K_D = 0.0
### TUNE PID GAINS ABOVE ###

# SETUP
pid_controller = WheelController(
    driver_ids=(15, 13, 14),
    encoder_ids=(11, 10),
)
pid_controller.k_p = K_P
pid_controller.k_i = K_I
pid_controller.k_d = K_D
STBY = Pin(12, Pin.OUT)
STBY.on()
vel_data = []


# LOOP
for i in range(200):
    if i == 49:  # step up @ t=0.5 s
        pid_controller.set_wheel_velocity(REF_VEL)
    elif i == 149:  # step down @ t=1.5 s
        pid_controller.set_wheel_velocity(0.0)
    print(
        f"Reference velocity={pid_controller.ref_lin_vel} m/s, Measured velocity={pid_controller.meas_lin_vel} m/s"
    )
    vel_data.append((pid_controller.ref_lin_vel, pid_controller.meas_lin_vel))
    sleep(0.01)
# Terminate
pid_controller.set_wheel_velocity(0.0)
sleep(0.5)
STBY.off()

### UNCOMMENT FOLLOWING 3 LINES WHEN SATISFIED WITH PID GAINS ###
with open(f"ref_{REF_VEL:.1f}-pid_{K_P:.2f}_{K_I:.2f}_{K_D:.2f}.csv", "w") as file:
    for item in vel_data:
        file.write(f"{item[0]},{item[1]}\n")
