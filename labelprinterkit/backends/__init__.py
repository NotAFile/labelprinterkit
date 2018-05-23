import usb.core
import usb.util
import threading

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
