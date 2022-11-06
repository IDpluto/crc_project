
from itertools import count
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from pandas.core.indexes import interval

fig, (gx, gy, gz, ax, ay, az) = plt.subplots(6,1)

fig.set_size_inches((10, 5))
fig.subplots_adjust(wspace = 0.9, hspace = 0.9)

line1, = gx.plot([], [], lw =2)
line2, = gy.plot([], [], lw =2) 
line3, = gz.plot([], [], lw =2) 
line4, = ax.plot([], [], lw =2) 
line5, = ay.plot([], [], lw =2) 
line6, = az.plot([], [], lw =2)
line = [line1, line2, line3, line4, line5, line6]

def animate(i):
    # axis limits checking. Same as before, just for both axes
    data =pd.read_csv('/home/dohlee/crc_project/data/data1.csv')
    x_value = data['x_value']
    gyro_x = data['gyro_x']
    gyro_y = data['gyro_y']
    gyro_z = data['gyro_z']
    acc_x = data['acc_x']
    acc_y = data['acc_y']
    acc_z = data['acc_z']

    for ax in [gx, gy]:
        xmin, xmax = ax.get_xlim()
        if t >= xmax:
            ax.set_xlim(xmin, 2*xmax)
            ax.figure.canvas.draw()
    gx.plot(x_value, gyro_x, lw =2)
    gy.plot(x_value, gyro_y, lw =2) 
    gz.plot(x_value, gyro_z, lw =2) 
    ax.plot(x_value, acc_x, lw =2) 
    ay.plot(x_value, acc_y, lw =2) 
    az.plot(x_value, acc_z, lw =2)
    print(x_value)
    
    #line[0].set_data(x_value, gyro_x)
    #line[1].set_data(x_value, gyro_y)
    #line[2].set_data(x_value, gyro_z)
    #line[3].set_data(x_value, acc_x)
    #line[4].set_data(x_value, acc_y)
    #line[5].set_data(x_value, acc_z)
    
    return line


ani = FuncAnimation(fig , animate, blit=False, frames= 200, interval = 10, repeat=False)
 
#plt.tight_layout()
plt.show()
