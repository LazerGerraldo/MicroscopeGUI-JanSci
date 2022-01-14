# communicating with the microscope from this link https://firmlyembedded.co.za/useful-python-script-to-send-and-receive-serial-data/

import time
import serial

baud = 38400        # baud rate, default 38400 for microscope
ser = 0             # serial connection assigned during startup()
waittime = 12       # loop time for movement of motors, based on Z axis homing from max

axisinfo = [['X', 77000],['Y',40000],['Z',30000], # array of all acceptable axis IDs and the axis max step values
['O', 400000],['L',500],['P',500]]           # TODO update for L, P

# opens serial connection at the input port using global baudrate
def startup(port):
    global ser
    global baud
    ser = serial.Serial(port, baud, timeout=1) # initialize the serial port

    if ser.isOpen():    # verify serial port is open
        print(ser.name + ' is open...')
    else:
        print('unable co open serial port, verify the correct serial port and run again')
    return ser

# uses global ser value and closes serial connection
def closedown():
    global ser
    ser.close() # close the serial port

# check the axis ID with the axis info array before sending the serial command
def axisidcheck(id):
    global axisinfo
    for x in axisinfo:
        if x[0] == id:
            print('the axis info array contains the ID ' + id)
            return True
    print('the axis info array does NOT contain the ID ' + id) 
    return False

def axisstepcheck(id, stepcount):
    global axisinfo
    for x in axisinfo:
        if x[0] == id: # find correct ID
            if x[1] >= stepcount: # verify axis can move requested step ammount
                # print('requested movement within bounds')
                return True
            else:
                print(id + ' unable to move, requested movement of ' + str(stepcount) + ' exceeds max step count of ' + str(x[1]) + ' steps for axis ' + id)
                return False
    print('requested axis ID of ' + id + ' not found')
    return False

# move axis with axis ID should be single letter X, Y, Z, O, L, P and step distance less thatn 35,000
def moveAxis(id, step):
    global waittime
    if axisstepcheck(id, step): # if the axis ID exists move the axis step steps
        # print(id + ' moving ' + str(step) + ' steps')
        movestr = id + 'MA ' + str(step) + '\n'  # combines to ex. XMA 140\n
        movestr = movestr.encode('utf-8')   # encoded move string for serial communication
        ser.write(movestr)
        time.sleep(4)

        if '' in ser.read_all().decode("utf-8"):# check if the movement was completed successfully
            print('completed movement')

        else:
            print('movement was unable to complete')

    else:
        print('incorrect ID or step movement, requested to move ' + id + ' ' + str(step)+ ' steps ')

# home axis with input 
def homeAxis(id):
    global waittime
    if axisidcheck(id):
        homestr = id + 'EX 1\n'
        homestr = homestr.encode('utf-8')

        print('homing ' + id + ' axis')
        ser.write(homestr)
        
    else:
        print('incorrect ID for homing\nrequested to move ' + id)
    
    x = 0 # keep track of loops through
    while x <= waittime:
        if 'DONE' in ser.read_all().decode("utf-8"):
            print('completed homing')
            break
        time.sleep(1)
        x = x + 1
    else:
        print('movement was unable to complete or did not have enough time to record Done')

def internalTest():
    # ------------------------------ testing microscope class --------------------------------
    ser = startup('COM5') # needed for using any serial connections

    # test axisidcheck()
    # axisidcheck('Bill')
    axisidcheck('X')

    # test axisstepcheck()
    # axisstepcheck('Y', 500)
    # axisstepcheck('O', 1000000000)
    # axisstepcheck('Y', 500)


    # moveAxis('Z', 3000)
    # moveAxis('Z', 6000)
    # moveAxis('Z', 3000)
    # homeAxis('Z')

    closedown() # closing serial connection

def bobLoop():
    ser = startup('COM6')
    x = 1
    while(1):
        homeAxis('Z')
        # print('reading serial: ' + ser.read_all().decode("utf-8"))
        time.sleep(3)
        # moveAxis('Z', 15000)
        # print('reading serial: ' + ser.read_all().decode("utf-8"))
        print('completed ' + str(x) + ' loops')
        x = x + 1

    closedown()

# bobLoop()
# internalTest()