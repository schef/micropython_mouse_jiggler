import time
import usb_hid
from mouse import Mouse

m = None

def get_millis():
    return int(time.monotonic_ns() / 1000 / 1000)

def millis_passed(timestamp):
    return get_millis() - timestamp

def reset_speed():
    m.move(1, 1, 0)
    m.move(-1, -1, 0)


def test_mouse():
    print("test_mouse")
    m.move(-5000, -5000, 0)
    reset_speed()
    time.sleep(1)
    m.move(100, 100, 0)
    m.move(100, 100, 0)
    time.sleep(1)



def init():
    print("init")
    time.sleep(2)
    global m
    m = Mouse(usb_hid.devices)


def loop():
    print("loop")
    while True:
        test_mouse()
        time.sleep(2)
        pass


def run():
    init()
    loop()
