from guizero import App, Text, PushButton

def change_message():
    message.value = "Homing Axis"

app = App(title="Hello world")

message = Text(app, text="Press Button to Home")

button = PushButton(app, text="Home Axis", command=change_message)
button2 = PushButton(app, text="Button 2", command=change_message)

app.display()