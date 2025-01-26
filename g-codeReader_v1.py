import serial

# Set up the serial connection
ser = serial.Serial('COM3', 115200, timeout=1)  # Replace 'COM3' with your DexArm port

# Send a G-code command
ser.write(b'G1 X100 Y100 F1000\n')  # Move to X=100, Y=100 at speed F=1000

# Close the connection
ser.close()


import serial
import time

# Set up the serial connection
ser = serial.Serial('COM3', 115200, timeout=1)  # Replace 'COM3' with your DexArm's port
time.sleep(2)  # Allow time for the connection to initialize

# Open the G-code file
with open('./ROTRICS.gcode', 'r') as gcode_file:
    for line in gcode_file:
        # Strip any unnecessary whitespace
        command = line.strip()
        
        # Ignore blank lines or comments (lines starting with ';')
        if command and not command.startswith(';'):
            print(f"Sending: {command}")
            ser.write((command + '\n').encode())  # Send the G-code command
            time.sleep(0.1)  # Small delay to avoid overwhelming the device

# Close the serial connection
ser.close()
print("G-code file sent successfully!")
