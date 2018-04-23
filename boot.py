# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import network
import time
import config

pin25 = machine.Pin(25, machine.Pin.OUT)
pin25.value(0)

nic = network.WLAN(network.STA_IF)
nic.active(True)
nic.connect(config.wifi_essid, config.wifi_key)
while not nic.isconnected():
    time.sleep(1)

pin25.value(nic.isconnected())

