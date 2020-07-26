### Labelprinterkit

Labelprinterkit is a Python3 library for creating and printing labels. It was
developed for the Networking department of the KIT (Karlsruhe Institute of
Technology).

Labelprinterkit's simple layout engine can be used to declaratively create
simple labels:

```python
from Labelprinterkit import backends, items, label
from Labelprinterkit.printers.brother_pt700 import P700

# Define the layout of our label
# We define a single row with two text items.
# In real usage, you will probably want to change the font of the text.
class MyLabel(label.Label):
    items = [
        [items.Text(pad_right=50), items.Text()]
    ]

# Instantiate the label with specific data
l = MyLabel("text1", "text2")
# scan for a USB printer using the PyUSBBackend
printer = P700(PyUSBBackend.auto())
# Print!
printer.print_label(l)
```

Example of using a better font:

```python
from PIL import Image, ImageFont
SIZE = 60
font = ImageFont.truetype("FreeSans.ttf", SIZE)
# Use it in the label template, e.g.
Text(font, pad_right=50)
```

To use a Bluetooth connection:
1. pair your device
2. specify the serial device node when instantiating the printer:

```
printer = P700(BTSerialBackend.auto(devPath='/dev/ttyS8'))
```

The Following printers are currently supported:

 * Brother P-Touch PT-700 (aka P700)

The following printers will probably work, as they are supposedly identical,
but have not been tested (please tell us if they do!):

 * Brother H500
 * Brother E500

The following printers have been tested to mostly work, although not
officially supported (their protocol is similar, although not identical):

* Brother P-touch CUBE Plus PTP710BT

The following backends are currently supported:

 * USB Printer Device Class via PyUSB
 * Bluetooth Serial connection via PySerial

The official source of this repository is at https://git.scc.kit.edu/scc-net/labelprinterkit.
Pull requests and issues are also accepted on github at https://github.com/notafile/labelprinterkit.
