import usb.core
import usb.util
import threading
import serial

def is_usb_printer(dev):
    if dev.bDeviceClass == 7:
        return True
    for cfg in dev:
        if usb.util.find_descriptor(cfg, bInterfaceClass=7) is not None:
            return True


class PyUSBBackend():
    def __init__(self, dev):
        self.dev = dev
        self.lock = threading.Lock()

    @classmethod
    def auto(cls):
        dev = usb.core.find(custom_match=is_usb_printer)
        if dev is None:
            raise OSError('Device not found')
        return cls(dev)

    def write(self, data: bytes):
        self.dev.write(0x2, data)

    def read(self, count: int) -> bytes:
        return self.dev.read(0x81, count)

class BTSerialBackend():
    def __init__(self, dev):
        self.dev = dev
        self.lock = threading.Lock()

    @classmethod
    def auto(cls, devPath: str):
        dev = serial.Serial(
            devPath,
            baudrate=9600,
            stopbits=serial.STOPBITS_ONE,
            parity=serial.PARITY_NONE,
            bytesize=8,
            dsrdtr=False,
            timeout=1
        )
        if dev is None:
            raise OSError('Device not found')
        return cls(dev)

    def write(self, data: bytes):
        self.dev.write(data)

    def read(self, count: int) -> bytes:
        data = self.dev.read(count)
        return data