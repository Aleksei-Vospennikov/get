import matplotlib.pyplot as plt
import numpy as np
import math

with open("./settings.txt", "r") as settings_file:
    settings_data = [float(num) for num in settings_file.read().split("\n")]

data = np.loadtxt("./data.txt", dtype=int)

sampl_freq = settings_data[0]           # sampling frequency = time step
quant_step = settings_data[1]           # quantization step  = voltage step

volt_data = data * quant_step
time_data = np.arange(0, len(data)) * sampl_freq

max_volt = max(volt_data)
max_time = max(time_data)

charge_data = [time_data[0:argmax(volt_data):], volt_data[0:argmax(volt_data):]]
discharge_data = [time_data[arqmax(volt_data)::], volt_data[arqmax(volt_data)::]]

fig, axs = plt.subplots(nrows=, ncols=, figsize=(), dpi=)
