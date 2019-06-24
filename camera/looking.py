from time import sleep, gmtime, strftime
from picamera import PiCamera
from guizero import App, PushButton, Text, Picture

camera = PiCamera()
camera.resolution = (640, 480)
camera.vflip = True

# camera warm-up time
sleep(2)

def openEye():
    camera.start_preview(fullscreen=False, window=(100,20,640,680))
#   preview_overlay(camera, overlay)

def savePic():
    output = strftime("/home/ninja/Pictures/image-%d-%m %H:%M:%S.png", gmtime())
    camera.capture(output)

def closeEye():
    camera.stop_preview()

app = App("Eye", layout="grid")
camera.start_preview(fullscreen=False, window=(100,20,640,680))
openEye0 = PushButton(app, openEye, text="Open eye", grid=[0,0])
savePic0 = PushButton(app, savePic, text="Snap picture", grid=[1,0])
closeEye0 = PushButton(app, closeEye, text="Close eye", grid=[0,1])
app.display()
app.on_close(closeEye)

