"""
Run this script with local Python.
"""
import csv
import matplotlib.pyplot as plt

# Extract data
with open('example_data.csv', newline='') as f:
    reader = csv.reader(f)
    data = tuple(reader)
targ_v = []
real_v = []
err = []
for item in data:
    targ_v.append(float(item[0]))
    real_v.append(float(item[1]))
    err.append(targ_v[-1] - real_v[-1])

# START CODING HERE
mse = None
# END CODING HERE
print(f"PID Controller's Mean Squared Error: {mse}")

# Plot data
ts = list(range(len(data)))  # create timestamps for x axis
for i in range(len(data)):
    ts[i] = 0.05 * i
xticks = [0] * 21
for i in range(21):
    xticks[i] = i
yticks = [0] * 20
for i in range(20):
    yticks[i] = i * 0.1 - 1
fig, ax = plt.subplots(2, 1, sharex=True, figsize=(12, 8))
ax[0].plot(ts, targ_v, '#7C878E', ts, real_v, '#582C83') 
ax[0].set_xlim([0, 20.5])
ax[0].set_ylim([-0.95, 0.95])
ax[0].set_xticks(xticks)
ax[0].set_yticks(yticks)
ax[0].grid()
ax[1].plot(ts, err, 'r')
ax[1].set_ylim([-0.5, 0.5])
plt.grid()
plt.show()
