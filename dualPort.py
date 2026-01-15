import serial
import time
import re

class DualPortDexarmController:
    def __init__(self, port1, port2):
        self.ser_y = serial.Serial(port1, 115200, timeout=1)
        self.ser_xz = serial.Serial(port2, 115200, timeout=1)
        time.sleep(2)  # Allow time for both connections to initialize

    def execute_gcode_file(self, gcode_file):
        with open(gcode_file, 'r') as f:
            for line in f:
                command = line.strip()
                if not command or command.startswith(';'):
                    continue  # Skip comments and blank lines

                # Check which axes are mentioned
                has_x = 'X' in command
                has_y = 'Y' in command
                has_z = 'Z' in command

                # If Y is present, send to port 1 (Y-axis device)
                if has_y:
                    print(f"Sending to Y-axis (port1): {command}")
                    self.ser_y.write((command + '\n').encode())
                    time.sleep(0.1)
                
                # If X or Z present (but not Y), send to port 2 (XZ-axis device)
                if (has_x or has_z) and not has_y:
                    print(f"Sending to X/Z-axis (port2): {command}")
                    self.ser_xz.write((command + '\n').encode())
                    time.sleep(0.1)

    def close(self):
        self.ser_y.close()
        self.ser_xz.close()


controller = DualPortDexarmController(port1="/dev/cu.usbmodemY", port2="/dev/cu.usbmodemXZ")
controller.execute_gcode_file("./ROTRICS.gcode")
controller.close()

