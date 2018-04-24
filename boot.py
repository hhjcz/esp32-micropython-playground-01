# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import network
import time
import config
import oled


def wifi_setup():
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect(config.wifi_essid, config.wifi_key)
    while not nic.isconnected():
        time.sleep(1)

    builtin_led.value(nic.isconnected())


builtin_led = machine.Pin(25, machine.Pin.OUT)
builtin_led.value(0)

oled.setup()
wifi_setup()
