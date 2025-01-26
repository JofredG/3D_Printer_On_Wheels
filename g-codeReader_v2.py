from pydexarm import Dexarm

dexarm = Dexarm(port="COM3")  # Replace with your serial port
dexarm.go_home()

# Path to your g-code file
gcode_file_path = "./ROTRICS.gcode"

# Execute the g-code file
dexarm.execute_gcode_file(gcode_file_path)

dexarm.close()
