![image with grid of buttons](https://github.com/LazerGerraldo/MicroscopeGUI-JanSci/blob/master/basicui.jpg?raw=true) -->

<p float="left">
	<img src="https://github.com/LazerGerraldo/MicroscopeGUI-JanSci/blob/master/assets/basicui.jpg" width="313" height="343"/>
</p>

# Created for the testing and setup of Jan Scientific Microscopes

Designed a basic operating GUI for the Jan Scientific microscope for internal testing and root cause analysis in the office. The program used pySerial for serial communication with the microscope.

Internal axis information is stored to ensure that motors are not burnt out while operating. 

### Future Update
Make sure the baud rate and port selectors are available and working

In a upcoming update it would be handy to have a program that programs motor controllers when specified a port and motor axis to program. 

## File Descriptions and Explanations

UImicroscope.py integrates all other methods with a GUI format for the user. 

microscope.py sends movements to the microscope. Additionally manages the serial commands sent to the microscope and determines if requested movement is within the stored parameters for a specified axis. 

serialscan.py scans all computers serial ports and returns a list of available serial ports for user determining what serial port the microscope is located on. 


## Installation
need to run the following command to install pySerial. 
```
python -m pip install pyserial
```
full documentation website for [pySerial](https://pyserial.readthedocs.io/en/latest/index.html)

serial communicating basics with examples from [here](https://firmlyembedded.co.za/useful-python-script-to-send-and-receive-serial-data/).

install PyQt5 and PyQt-builder 1/12/2022

look for designer.exe in C:\Users\<user>\AppData\Local\Programs\Python\Python37\Lib\site-packages\PyQt5 folder. 

Followed some of the steps here for finding [designer](https://gist.github.com/marcoandre1/a77460d7b88de7e9608335b9c518b752)
