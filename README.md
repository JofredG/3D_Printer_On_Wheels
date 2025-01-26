# 3D_Printer_On_Wheels

[3D_Printer_On_Wheels GitHub](https://github.com/JofredG/3D_Printer_On_Wheels)
[Dexarm_GitHub](https://github.com/Rotrics-Dev)
[Rotrics_Dexarm_Manual](https://manual.rotrics.com/)

### 1/24/24 Meeting w Fonseca (Senior Project Advisor)
- Need to ensure we choose a viable final deliverable.
- Given a fully functioning 3D Printing Robot on Wheel's may not be viable, Fonseca suggested creating an interface to communicate with the robot.
### 1/25/24 Understanding 2D Printing (CNC with Pen and Paper)
##### Notes:
- When booting up the Dexarm, it moves to *Home* and the default *Work Height*.
- One can create a python script that parses a .g-code file and sends it to Dexarm.
- To print 2D .svg images, the images need to be converted to .g-code files.

Question:
How does one set the work height during g-code generation?
Which open source .svg to .g-code generator works best?
	I generated a g-code file for a 2D pen print using rotrics studio and exported it. I then created a python script that ran through the g-code and sent it to the Dexarm robot using pyserial. Looking at the print, I realize that the robot tends to not follow commands that require drawing a curve between two points. Along with that the robot doesn't pick up the pen, or rather take into account needing to move the pen off the paper by increasing the z-value. Chat GPT replied with the following possible causes:
		1. Curve Commands Not Executed Properly:
			-  Unsupported G-code Commands: The Dexarm firmware might not fully support G2/G3 commands. Some CNC devices and 3D printers only support straight-line moves (G1). If this is the case, you can:
		    - Reconfigure g-code generation: In Rotrics Studio or your CAD/CAM software, look for an option to approximate curves using a series of short straight-line moves instead of G2/G3 commands.
		    - Preprocess the g-code: Write a Python script to interpolate G2/G3 commands into small G1 segments.
		2. Pen Not Lifting
			This issue suggests that the Z-axis movement commands (like G1 Zxxx) are either missing, ignored, or not configured correctly.
		3. Communication/Timing Issues with pyserial
			If commands are being skipped or ignored, it could be a problem with how you're sending the commands to the robot.
			- Buffering Issues: The Dexarm may be receiving commands too quickly, causing it to drop some of them. Add a delay after sending each command to allow the robot to process it.
			- Command Termination: Ensure each g-code command is properly terminated with a newline character (`\n`)
		4. Calibration and Z-Axis Configuration
			- Ensure the Dexarm is calibrated correctly, especially for the Z-axis. Improper calibration can cause the robot to not lift the pen or apply the wrong height during drawing.
			- Double-check the workspace and ensure the Z-axis "pen down" and "pen up" heights are defined correctly in the robot's settings.

##### Future notes:
- 3D Printing bed should be 15 cm from the base of Dexarm for maximum working area.
- E-Axis replaces x-axis movement (When on top of moving platform, the entire Dexarm moves instead of just the head.)
- Movement speed units are mm/sec

##### Thoughts for the future:
[Rotrics Studio has an option to integrate a sliding rail which uses the E-Axis feature.](https://manual.rotrics.com/get-start/sliding-rail-kit) Given there is an E-Axis, we may attempt to have that axis movement translate to wheels of the AVG Robot that is set to be used as the moving platform by *x* mm. **Must figure out if we can take advantage of the feature.**


