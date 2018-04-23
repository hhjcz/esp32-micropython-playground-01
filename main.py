import socket
import machine
import time
import random
import config


def main():
    builtin_led = machine.Pin(25, machine.Pin.OUT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    led_toggle = 1

    while True:
        sock.sendto("zkouska:{}|g".format(random.randint(1, 100)), (config.statsd_host, 8125))
        time.sleep(1)
        led_toggle = 1 - led_toggle
        builtin_led.value(led_toggle)


main()
