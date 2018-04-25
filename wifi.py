import time
import network
import config
import oled

nic = None


def setup(builtin_led):
    global nic
    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect(config.wifi_essid, config.wifi_key)
    while not nic.isconnected():
        time.sleep(1)

    builtin_led.value(nic.isconnected())
    oled.print_string(nic.ifconfig()[0], y=0, x=0)
