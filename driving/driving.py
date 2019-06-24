import explorerhat
from time import sleep
from guizero import App, PushButton, Slider, Text

def forward(value):
	explorerhat.motor.forward(int(value))

def backward(value):
        explorerhat.motor.backward(int(value))
	
def stop():	
	explorerhat.motor.stop()
	forwardSider.value = "0"
	backwardSlider.value = "0"
	leftSider.value = "0"
	rightSlider.value = "0"

def turnLeft(value):
        explorerhat.motor.one.forward(int(value))
        explorerhat.motor.two.backward(int(value))
        
def turnRight(value):
        explorerhat.motor.two.forward(int(value))
        explorerhat.motor.one.backward(int(value))

app = App("Controller", height=300, width=300)
stopButton = PushButton(app, stop, text="Stop")

forwardTxt = Text(app, "Move forward")
forwardSider = Slider(app, start=0, end=100, command=forward)

backwardTxt = Text(app, "Move backward")
backwardSlider = Slider(app, start=0, end=100, command=backward)

leftTxt = Text(app, "Turn left")
leftSider = Slider(app, start=0, end=100, command=turnLeft)

rightTxt = Text(app, "Turn right")
rightSlider = Slider(app, start=0, end=100, command=turnRight)

app.display()
