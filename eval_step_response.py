from time import sleep
from wheel_controller import WheelController
from machine import Pin

# SETUP
velocity_controller = WheelController(
    driver_ids=(15, 13, 14),
    encoder_ids=(18, 19),
)
# START TUNING PID GAINS below
velocity_controller.k_p = None
velocity_controller.k_i = None
velocity_controller.k_d = None
# END TUNING

STBY = Pin(12, Pin.OUT)
STBY.on()

# LOOP

for i in range(200):
    if i == 50:  # step up @ t=0.5 s
        velocity_controller.set_wheel_velocity(0.4)
    elif i == 140:  # step down @ t=1.25 s
        velocity_controller.set_wheel_velocity(0.0)
    print(
        f"Reference velocity={velocity_controller.ref_lin_vel} m/s, Measured velocity={velocity_controller.meas_lin_vel} m/s"
    )
    sleep(0.02)
# Terminate
velocity_controller.set_wheel_velocity(0.0)
sleep(0.5)
STBY.off()

### UNCOMMENT FOLLOWING 3 LINES WHEN SATISFIED WITH PID GAINS ###
# with open(f'data-{K_P}_{K_I}_{K_D}.csv', 'w') as file:
#     for item in data:
#         file.write(f'{item[0]},{item[1]}\n')
