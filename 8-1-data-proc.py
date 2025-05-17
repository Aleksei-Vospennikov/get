import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

with open("./settings.txt", "r") as settings_file:
    settings_data = [float(num) for num in settings_file.read().split("\n")]

data = np.loadtxt("data.txt", dtype=int)

# Get samplting rate (= time step) and quantization step (= voltage step)
sampl_rate = settings_data[0]
quant_step = settings_data[1]

# Calculate real voltage and time values
volt_data = data * quant_step
time_data = np.arange(0, len(data)) * sampl_rate

# Determine maximums of voltage and time
max_volt = max(volt_data)
max_time = max(time_data)

# Calculate charging and discharging time
idx, item = max(enumerate(volt_data), key=lambda pair: (pair[1], pair[0]))
charge_time = time_data[idx]
discharge_time = time_data[-1] - charge_time

# Build figure and axes
fig, axs = plt.subplots(figsize=(16, 10), dpi=500)

# Build graph
axs.plot(time_data, volt_data, color="blue", linewidth=2, label='Напряжение на конденсаторе')
axs.scatter(time_data[::20], volt_data[::20], color='darkblue', s=50, label='Экспериментальные точки')

# Axes setting
axs.set_xlim(np.min(time_data), np.max(time_data))
axs.set_ylim(np.min(volt_data) * 0.9, np.max(volt_data) * 1.1)
axs.set_xlabel("Время, с", fontsize=12)
axs.set_ylabel("Напряжение, В", fontsize=12)
axs.set_title("Зависимость напряжения на конденсаторе от времени в процессе его зарядки и рязрядки", fontsize=14, wrap="True")

# Grid setting
axs.grid(which='major', linestyle='-', linewidth=0.7, alpha=0.7)
axs.grid(which='minor', linestyle=':', linewidth=0.5, alpha=0.5)
axs.xaxis.set_minor_locator(AutoMinorLocator())
axs.yaxis.set_minor_locator(AutoMinorLocator())

# Add text
axs.text(charge_time + discharge_time/2, np.max(volt_data)*0.5,
         "Время зарядки: {:.2f} с\n\nВремя разрядки: {:.2f} с".format(charge_time, discharge_time),
         fontsize=12, ha='left', color='black')

# Legend
axs.legend(loc='best', fontsize=10)

# Show and save figure
fig.savefig("graph.svg")
plt.show()
