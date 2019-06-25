import explorerhat
from guizero import App, Text


# connect VCC terminal with Digital out terminal of A3144 with a 4.7kOhm resistor
# connect VCC to 5V, Digital out to Input 1, and GND to GND

delay = 1 # milliseconds

def sweeping():
    if explorerhat.input.one.read():
        text.value = "safe"
    else:
        text.value = "MINE FOUND!!!"

app = App()
text = Text(app, text="...")
text.repeat(delay, sweeping)

