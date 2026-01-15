import serial
import keyboard  # pip install keyboard

arduino = serial.Serial('/dev/tty.usbmodem14201', 9600)  # Change '/dev/tty.usbmodem14201' to your Arduino port

'''run this line in terminal to get sudo access
sudo chmod 666 /dev/tty.usbmodem14201'''

print("Press 'm' to move motor, 's' to stop. Press 'q' to quit.")

while True:
    if keyboard.is_pressed('m'):
        arduino.write(b'm')
    elif keyboard.is_pressed('s'):
        arduino.write(b's')
    elif keyboard.is_pressed('q'):
        break