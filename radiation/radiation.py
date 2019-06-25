# connect one end of the light sensor to Analog 1 and other end to GND
# connect one end of the 4.7kOhm resistor to Analog 1 and other end to 5V

import explorerhat
from time import sleep
from guizero import App, Text

delay = 1000 # milliseconds
Vref = 5.125

def measureRadiations():
    text.value = Vref - explorerhat.analog.one.read()

app = App("Amount of radiations")
text = Text(app, text="Amount of radiations ...")
text.repeat(delay, measureRadiations)
app.display()


