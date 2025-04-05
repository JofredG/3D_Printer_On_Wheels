from pydexarm import Dexarm
import time
import serial

'''windows'''
# dexarm = Dexarm(port="COM67")
'''mac & linux'''
# this is for the top right USB port on raspberry pi 5, use >>ls /dev/tty*<< to find port otherwise
dexarm = Dexarm(port="/dev/ttyACM1")

# Open serial connection to arduino, this is for the top left USB port on rasp 5
arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(2)
dexarm.go_home()
time.sleep(2)

for _ in range(3):
    dexarm.move_to(0, 300, -125)
    time.sleep(1)
    dexarm.move_to(0, 250, -125)
    time.sleep(1)
    arduino.write(b'1')
    time.sleep(0.5)
    arduino.write(b'0')
    time.sleep(1)

arduino.close() # close serial comm
dexarm.close()