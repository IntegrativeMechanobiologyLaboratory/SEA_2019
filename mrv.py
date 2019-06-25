import explorerhat
from guizero import App, PushButton, Slider, Text, Picture, TextBox, Box
from time import sleep, gmtime, strftime
from picamera import PiCamera

#---------------------------------------------------------
# constants and variables
#---------------------------------------------------------
sweepDelay = 100 # milliseconds
radiationDelay = 100 # milliseconds

Vref = 5.3

xRes = 640
yRes = 480

savingLocation = "/home/ninja/Pictures/image-%d-%m %H:%M:%S.png"

xLoc = 200
yLoc = 200

camera = PiCamera()
camera.resolution = (xRes, yRes)
camera.vflip = True

# camera warm-up time
sleep(2)

#---------------------------------------------------------
# functions for motor
#---------------------------------------------------------
def forward(value):
	explorerhat.motor.forward(int(value))
	backwardSlider.value = "0"
	leftSlider.value = "0"
	rightSlider.value = "0"
	
def backward(value):
        explorerhat.motor.backward(int(value))
        forwardSlider.value = "0"
        leftSlider.value = "0"
        rightSlider.value = "0"
	
def stop():	
	explorerhat.motor.stop()
	forwardSlider.value = "0"
	backwardSlider.value = "0"
	leftSlider.value = "0"
	rightSlider.value = "0"

def turnLeft(value):
        explorerhat.motor.one.forward(int(value))
        explorerhat.motor.two.backward(int(value))
        forwardSlider.value = "0"
        backwardSlider.value = "0"
        rightSlider.value = "0"
	
def turnRight(value):
        explorerhat.motor.two.forward(int(value))
        explorerhat.motor.one.backward(int(value))
        forwardSlider.value = "0"
        backwardSlider.value = "0"
        leftSlider.value = "0"


#---------------------------------------------------------
# Camera functions
#---------------------------------------------------------
def openEye():
    camera.start_preview(fullscreen=False, window=(xLoc,yLoc,xRes,yRes))

def savePic():
    output = strftime(savingLocation, gmtime())
    camera.capture(output)

def closeEye():
    camera.stop_preview()



#---------------------------------------------------------
# Hall effect sensor functions
# connect VCC terminal with Digital out terminal of A3144 with a 4.7kOhm resistor
# connect VCC to 5V, Digital out to Input 1, and GND to GND
#---------------------------------------------------------
def sweeping():
    if explorerhat.input.one.read():
        mineSignal.value = "safe"
    else:
        mineSignal.value = "MINE FOUND!!!"



#---------------------------------------------------------
# LDR light sensor functions
# connect one end of the light sensor to Analog 1 and other end to GND
# connect one end of the 4.7kOhm resistor to Analog 1 and other end to 5V
#---------------------------------------------------------
def measureRadiations():
    radAmount.value = round(Vref - explorerhat.analog.one.read(),2)




#---------------------------------------------------------
# GUI: Graphical User Interface
#---------------------------------------------------------
app = App("Mini Reconnaissance Vehicle", height=300, width=500)

camera.start_preview(fullscreen=False, window=(xLoc,yLoc,xRes,yRes))

dangerBox = Box(app, width="fill", align="top", border=2)
dangerBox1 = Box(dangerBox, height="fill", align="left")
Text(dangerBox1, text="Mine detection status=", align="left")
mineSignal = Text(dangerBox1, text="...", align="right")
mineSignal.repeat(sweepDelay, sweeping)

dangerBox2 = Box(dangerBox, height="fill", align="right")
Text(dangerBox2, text="Amount of radiations=", align="left")
radAmount = Text(dangerBox2, text="...", align="right")
radAmount.repeat(radiationDelay, measureRadiations)


controlBox = Box(app, height="fill", width="fill", align="bottom", border=True)

cameraBox = Box(controlBox, height="fill", width="fill", align="left")
savePic0 = PushButton(cameraBox, savePic, text="Snap picture", height="fill", width="fill", align="left")
cameraBox1 = Box(cameraBox, height="fill", width="fill", align="right")
openEye0 = PushButton(cameraBox1, openEye, height="fill", width="fill", text="Open eye", align="top")
closeEye0 = PushButton(cameraBox1, closeEye, height="fill", width="fill", text="Close eye", align="bottom")

driveBox = Box(controlBox, height="fill", width="fill", align="right")
driveBox1 = Box(driveBox, height="fill", width="fill", align="top")
driveBox11 = Box(driveBox1, height="fill", width="fill", align="left")
forwardSlider = Slider(driveBox11, start=0, end=100, command=forward, height="fill", horizontal=False)
Text(driveBox11, "F")

driveBox12 = Box(driveBox1, height="fill", width="fill", align="left")
backwardSlider = Slider(driveBox12, start=0, end=100, command=backward, height="fill", horizontal=False)
Text(driveBox12, "B")

driveBox13 = Box(driveBox1, height="fill", width="fill", align="left")
leftSlider = Slider(driveBox13, start=0, end=100, command=turnLeft, height="fill", horizontal=False)
Text(driveBox13, "L")

driveBox14 = Box(driveBox1, height="fill", width="fill", align="left")
rightSlider = Slider(driveBox14, start=0, end=100, command=turnRight, height="fill", horizontal=False)
Text(driveBox14, "R")

stopButton = PushButton(driveBox, stop, text="Stop motor", height="fill", width="fill", align="right")

app.display()
app.on_close(camera.stop_preview())
