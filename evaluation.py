"""
Run this script with local Python (on RPi).
"""

import csv
import matplotlib.pyplot as plt
from pathlib import Path

# ======================= #
# --- 0. Prepare Data --- #
# ======================= #
### CHANGE FILE NAME BELOW ###
filename = "ref_0.4-pid_1.20_0.00_1.50.csv"  # data file name

data_path = Path(__file__).parent / "data" / filename
with open(data_path, newline="") as f:
    reader = csv.reader(f)
    data = tuple(reader)
ref_vels = []
meas_vels = []
errors = []
ts = []
for ind, val in enumerate(data):
    ref_vels.append(float(val[0]))
    meas_vels.append(float(val[1]))
    errors.append(float(val[0]) - float(val[1]))
    ts.append(ind * 0.01)

# ============================== #
# --- 1. Calculate Rise Time --- #
# ============================== #
refv = ref_vels[99]  # ref=0 in [0:50] and [149:200]
t_10 = None
t_90 = None
for i, mv in enumerate(meas_vels):
    if t_10 is None and mv >= refv * 0.1:
        t_10 = ts[i]
    if t_90 is None and mv >= refv * 0.9:
        t_90 = ts[i]
    if t_10 and t_90:
        break
rise_time = "N/A"
if t_10 and t_90:
    rise_time = t_90 - t_10
    print(f"Rise time (10%-90%): {rise_time:.2f} s")
else:
    print("Rise time (10%-90%): N/A (Did not reach 90% of reference)")

# ========================================= #
# --- 2. Calculate Overshoot Percentage --- #
# ========================================= #
maxv = max(meas_vels)
overshoot = maxv - refv
if overshoot > 0 and refv:
    overshoot_percent = (overshoot / refv) * 100
else:
    overshoot_percent = 0.0

print(f"Peak velocity: {maxv:.4f} m/s, overshoot percentage: {overshoot_percent:.2f}%")

# ============================================================= #
# --- 3. Calculate Steady State Mean and Standard Diviation --- #
# ============================================================= #
stabv = meas_vels[149:119:-1]  # consider last 30% as steady state
steady_mean = sum(stabv) / len(stabv)
steady_var = (sum((x - steady_mean) ** 2 for x in stabv) / len(stabv)) ** 0.5
print(
    f"Steady state average: {steady_mean:.4f} m/s, standard deviation: {steady_var:.4f} m/s"
)

# Visualize data
plt.plot(
    ts,
    ref_vels,
    "#7C878E",
    ts,
    meas_vels,
    "#582c83",
)
plt.legend(["Reference", "Measured"])
plt.xlabel("Time Stamps (x 0.01 seconds)")
plt.ylabel("Linear Velocity of Wheel (m/s)")
plt.grid(True)
plt.show()


#
# ### START CODING HERE ### ~ 4 lines
# mse = None
# ### END CODING HERE ###
# print(f"PID Controller's Mean Squared Error: {mse}")
#
# # Plot data
# ts = list(range(len(data)))  # create timestamps for x axis
# for i in range(len(data)):
#     ts[i] = 0.05 * i
# xticks = [0] * 21
# for i in range(21):
#     xticks[i] = i
# yticks = [0] * 20
# for i in range(20):
#     yticks[i] = i * 0.1 - 1
# fig, ax = plt.subplots(2, 1, sharex=True, figsize=(12, 8))
# ax[0].plot(ts, targ_v, "#7C878E", linewidth=2)
# ax[0].plot(ts, real_v, "#582C83", linewidth=1.5)
# ax[0].set_ylabel("Velocity (m/s)")
# ax[0].set_xlim([0, 20.5])
# ax[0].set_ylim([-0.95, 0.95])
# ax[0].set_xticks(xticks)
# ax[0].set_yticks(yticks)
# ax[0].grid()
# ax[0].legend(["target", "actual"])
# ax[1].plot(ts, err, "r")
# ax[1].set_xlabel("Time Stamps (s)")
# ax[1].set_ylabel("Error (m/s)")
# ax[1].set_ylim([-0.4, 0.4])
# plt.grid()
# plt.show()
# ### UNCOMMENT FOLLOWING LINE WHEN SATISFIED WITH PID GAINS AND MSE VALUE ###
# # plt.savefig('pid_eval.png'))
