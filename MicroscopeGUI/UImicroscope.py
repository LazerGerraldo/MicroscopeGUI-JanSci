from guizero import App, Text, PushButton, MenuBar
import time
import microscope
import serialscan

port = 'COM5'   # may need to manualy assign a COM port after looking in device manager
baud = 38400    # baud rate, default 38400 for microscope
count = 0       # keep track of number of loops

microscope.startup(port)
# microscope.homeAxis('Z')

def moveAxis(id, step):
    microscope.moveAxis(id, step)
    # microscope.moveAxis('Z', 15000)

def homeAxis(id):
    microscope.homeAxis(id)
    # microscope.homeAxis('Z')

# home button commmands
def homeX():
    homeAxis('X')
def homeY():
    homeAxis('Y')
def homeZ():
    homeAxis('Z')
def homeO():
    homeAxis('O')
def homeL():
    homeAxis('L')
def homeP():
    homeAxis('P')

# up button commands
def upX():
    moveAxis('X', 50000)
def upY():
    moveAxis('Y', 35000)
def upZ():
    moveAxis('Z', 15000)
def upO():
    moveAxis('O', 150000)
def upL():
    moveAxis('L', 1000)
def upP():
    moveAxis('P', 1000)

# down button commands
def downX():
    moveAxis('X', 10000)
def downY():
    moveAxis('Y', 5000)
def downZ():
    moveAxis('Z', 5000)
def downO():
    moveAxis('O', 50000)
def downL():
    moveAxis('L', 1000)
def downP():
    moveAxis('P', 1000)


defmes = 'Press Button to Move'

app = App(title='Microscope Control V1', layout='grid')



def com_port_function():
    print("COM port menu button pressed")
    
def edit_function():
    print("******************Baud Rate (Changing)********************************")
 

menubar = MenuBar(app,
                  toplevel=["Serial Port", "Baud Rate"],
                  options=[
                      [ ["COM3", com_port_function], ["COM5", com_port_function], ["Re Scan Serial Ports", com_port_function] ],
                      [ ["Does not work", edit_function], ["9600", edit_function], ["86400", edit_function] ]
                  ])

#axis identifiers
xcol = Text(app, text="x", grid=[0,0])
ycol = Text(app, text="y", grid=[1,0])
zcol = Text(app, text="z", grid=[2,0])
ocol = Text(app, text="o", grid=[0,4])
lcol = Text(app, text="l", grid=[1,4])
pcol = Text(app, text="p", grid=[2,4])

# homing buttons
buttonhx = PushButton(app, text="home x axis", grid=[0,2], command=homeX)
buttonhy = PushButton(app, text="home y axis", grid=[1,2], command=homeY)
buttonhz = PushButton(app, text="home z axis", grid=[2,2], command=homeZ)
buttonho = PushButton(app, text="home o axis", grid=[0,7], command=homeO)
buttonhl = PushButton(app, text="home l axis", grid=[1,7], command=homeL)
buttonhp = PushButton(app, text="home p axis", grid=[2,7], command=homeP)

# movement buttons
buttonupx = PushButton(app, text="up x axis", grid=[0,1], command=upX)
buttonupy = PushButton(app, text="up y axis", grid=[1,1], command=upY)
buttonupz = PushButton(app, text="up z axis", grid=[2,1], command=upZ)
buttondwnx = PushButton(app, text="down x axis", grid=[0,3], command=downX)
buttondwny = PushButton(app, text="down y axis", grid=[1,3], command=downY)
buttondwnz = PushButton(app, text="down z axis", grid=[2,3], command=downZ)

buttonupo = PushButton(app, text="up o axis", grid=[0,6], command=upO)
buttonupl = PushButton(app, text="up l axis", grid=[1,6], command=upL)
buttonupp = PushButton(app, text="up p axis", grid=[2,6], command=upP)
buttondwno = PushButton(app, text="down o axis", grid=[0,8], command=downO)
buttondwnl = PushButton(app, text="down l axis", grid=[1,8], command=downL)
buttondwnp = PushButton(app, text="down p axis", grid=[2,8], command=downP)

app.display()

microscope.closedown()