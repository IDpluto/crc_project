
import serial
import math
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
from pandas.core.indexes import interval

def init():
    l_roll1.set_data([], [])
    l_pitch1.set_data([], [])
    l_yaw1.set_data([], [])
    l_acc_x1.set_data([], [])
    l_acc_y1.set_data([], [])
    l_acc_z1.set_data([], [])
    return l_roll1, l_pitch1, l_yaw1, l_acc_x1, l_acc_y1, l_acc_z1,

def data_gen():
    while 1:
        data =pd.read_csv('/home/dohlee/crc_project/data/data1.csv')

        xnum = data['x_num']
        roll1 = data['roll']
        pitch1 = data['pitch']
        yaw1 = data['yaw']
        acc_x1 = data['acc_x']
        acc_y1 = data['acc_y']
        acc_z1 = data['acc_z']
        yield xnum, roll1, pitch1, yaw1, acc_x1, acc_y1, acc_z1,

def animate(data):
    xnum, roll1, pitch1, yaw1, acc_x1, acc_y1, acc_z1 = data
    
    #ax1.clear()
    #ax2.clear()
    #ax3.clear()
    #ax4.clear()
    l_roll1.set_data(xnum, roll1)
    l_pitch1.set_data(xnum, pitch1)
    l_yaw1.set_data(xnum, yaw1)
    l_acc_x1.set_data(xnum, acc_x1)
    l_acc_y1.set_data(xnum, acc_y1)
    l_acc_z1.set_data(xnum, acc_z1)
    #ax3.plot(xnum, roll2, lw=2, color = 'red')
    #ax3.plot(xnum, pitch2, lw=2, color = 'blue')
    #ax3.plot(xnum, yaw2, lw=2, color = 'orange')
    #ax4.plot(xnum, acc_x2, lw=2, color = 'red')
    #ax4.plot(xnum, acc_y2, lw=2, color = 'blue')
    #ax4.plot(xnum, acc_z2, lw=2, color = 'orange')
    return l_roll1, l_pitch1, l_yaw1, l_acc_x1, l_acc_y1, l_acc_z1,


if __name__ == '__main__':
    
    grad2rad = 3.141592/180.0
    rad2grad = 180.0/3.141592
    cos = math.cos
    ser = serial.Serial('/dev/ttyUSB0', 921600)
    fig, (ax1, ax2) =  plt.subplots(2,1)
    l_roll1, = ax1.plot([], [], lw=2, color = 'red')
    l_pitch1, = ax1.plot([], [], lw=2, color = 'blue')
    l_yaw1, = ax1.plot([], [], lw=2, color = 'orange')
    l_acc_x1, = ax2.plot([], [], lw=2, color = 'red')
    l_acc_y1, = ax2.plot([], [], lw=2, color = 'blue')
    l_acc_z1, = ax2.plot([], [], lw=2, color = 'orange')


    
    ax1.set_ylim(-300, 300)
    ax1.grid()
    ax2.set_ylim(-3, 3)
    ax2.grid()

    ani = animation.FuncAnimation(fig, animate, data_gen, blit=True, interval=10,
        init_func=init, repeat=False)
    #ani = animation.FuncAnimation(fig, animate, data_gen,
    #                          interval=25, blit=True)

    plt.show()

    
 

