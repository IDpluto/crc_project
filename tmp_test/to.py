import serial
from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np

arduino = serial.Serial('/dev/ttyUSB0', 921600)

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim=(-10, 10))
line, = ax.plot([], [], lw=2)

max_points = 10
line, = ax.plot(np.arange(max_points), 
                np.ones(max_points, dtype=np.float)*np.nan, lw=2)

def init():
    return line,

def animate(i):
    y = arduino.readline()
    y = y.decode("ISO-8859-1")#.encode("utf-8")
    y = y.split(',')
    y = y[1]
    y = float(y)

    old_y = line.get_ydata()
    new_y = np.r_[old_y[1:], y]
    line.set_ydata(new_y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=200, interval=10, blit=False)

plt.show()