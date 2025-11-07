"""
Run this script with local Python
"""

import csv
from pathlib import Path

# ======================= #
# --- 0. Prepare Data --- #
# ======================= #
### CHANGE FILE NAME BELOW ###
filename = "example_data.csv"  # data file name

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

# =============================================== #
# --- 4. Visualization (Uncomment Code Below) --- #
# =============================================== #
# import matplotlib.pyplot as plt
# plt.plot(
#     ts[24:175],
#     ref_vels[24:175],
#     ts[24:175],
#     meas_vels[24:175],
# )
# plt.legend(["Reference", "Measured"])
# plt.xlabel("Time (s)")
# plt.xlim(0.25, 1.75)
# plt.xticks([0.1 * i for i in range(3, 18)])
# plt.ylabel("Linear Velocity (m/s)")
# plt.ylim(0.0, 0.5)
# plt.yticks([0.025 * i for i in range(20)])
# plt.grid(True)
# plt.show()
