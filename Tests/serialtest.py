# communicating with the microscope from this link https://firmlyembedded.co.za/useful-python-script-to-send-and-receive-serial-data/

import time
import serial

port = 'COM6'   # may need to manualy assign a COM port after looking in device manager
baud = 38400    # baud rate, default 38400 for microscope
count = 0       # keep track of number of loops

ser = serial.Serial(port, baud, timeout=1) # initialize the serial port

if ser.isOpen():    # verify serial port is open
     print(ser.name + ' is open...')
else:
    print('unable co open serial port, verify the correct serial port and run again')


while 1:
    print('sending command '+ str(count))
    ser.write(b'ZEX 1\n')
    time.sleep(8)
    count += 1
    if count == 4:
        break

ser.close() # close the serial port
    