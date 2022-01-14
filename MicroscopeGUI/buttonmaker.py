# outline of buttons for microscope control

from guizero import App, Text, TextBox, PushButton


app = App(title='Microscope Movement' , layout='grid')

#axis identifiers
xcol = Text(app, text="x", grid=[0,0])
ycol = Text(app, text="y", grid=[1,0])
zcol = Text(app, text="z", grid=[2,0])
ocol = Text(app, text="o", grid=[0,4])
lcol = Text(app, text="l", grid=[1,4])
pcol = Text(app, text="p", grid=[2,4])

# homing buttons
buttonhx = PushButton(app, text="home x axis", grid=[0,2])
buttonhy = PushButton(app, text="home y axis", grid=[1,2])
buttonhz = PushButton(app, text="home z axis", grid=[2,2])
buttonho = PushButton(app, text="home o axis", grid=[0,7])
buttonhl = PushButton(app, text="home l axis", grid=[1,7])
buttonhp = PushButton(app, text="home p axis", grid=[2,7])

# movement buttons
buttonupx = PushButton(app, text="up x axis", grid=[0,1])
buttonupy = PushButton(app, text="up y axis", grid=[1,1])
buttonupz = PushButton(app, text="up z axis", grid=[2,1])
buttondwnx = PushButton(app, text="down x axis", grid=[0,3])
buttondwny = PushButton(app, text="down y axis", grid=[1,3])
buttondwnz = PushButton(app, text="down z axis", grid=[2,3])

buttonupo = PushButton(app, text="up o axis", grid=[0,6])
buttonupl = PushButton(app, text="up l axis", grid=[1,6])
buttonupp = PushButton(app, text="up p axis", grid=[2,6])
buttondwno = PushButton(app, text="down o axis", grid=[0,8])
buttondwnl = PushButton(app, text="down l axis", grid=[1,8])
buttondwnp = PushButton(app, text="down p axis", grid=[2,8])

app.display()