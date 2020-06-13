import time

import machine

def run():
    led = machine.Pin(16, machine.Pin.OUT)

    while True:
        time.sleep(1)
        led.on()
        time.sleep(1)
        led.off()