import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval
 
 
 
def animate(i):
    data =pd.read_csv('data1.csv')
    gyro_x = data['gyro_x']
    gyro_y = data['gyro_y']
    gyro_z = data['gyro_z']
    acc_x = data['acc_x']
    acc_y = data['acc_y']
    acc_z = data['acc_z']
 
    plt.cla()
    plt.plot(gyro_x, label='Gyro_x')
    plt.plot(gyro_y, label='Gyro_y')
    plt.plot(gyro_z, label='Gyro_z')
    plt.plot(acc_x, label='acc_x')
    plt.plot(acc_y, label='acc_y')
    plt.plot(acc_z, label='acc_z')
    plt.legend(loc = 'upper left')
    plt.tight_layout()
 
ani = FuncAnimation(plt.gcf(),animate, interval = 1000)
 
plt.tight_layout()
plt.show()