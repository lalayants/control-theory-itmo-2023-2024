import numpy as np
from scipy.optimize import least_squares
import matplotlib.pyplot as plt

path_to_file = "./task2.1"

battery_power = 6.8424

K_p = [0.0025, 0.005, 0.01]
targets = [(600, 0), (600, 600)]

cnt = 0
for target in targets:
    for k_p in K_p:

        data =  np.loadtxt(path_to_file + f"/data_{str(target)}_{str(k_p)}", dtype=float) 

        time = data[:, 0]
        angle = data[:, 1]*np.pi/180
        speed = data[:, 2]*np.pi/180 

        target_angle = target[0] + target[1] * time

        plt.plot(time, target_angle, color="r")
        plt.plot(time, angle, color="b")
        plt.show()