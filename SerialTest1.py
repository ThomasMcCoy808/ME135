import serial
from collections import *
import time

arduino = serial.Serial(port='/dev/cu.SLAB_USBtoUART', baudrate=460800, timeout=.1)

a = deque([0, 4000, 6000, 7000, 3000, 2000, 1000, 240, 260])


def write(x):
    y = char(x)
    arduino.write(bytes(y)

for i in range(0,8):
    write(a[i])


