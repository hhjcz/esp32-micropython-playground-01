import socket
import machine
import time
import random
import config
import oled


def main():
    builtin_led = machine.Pin(25, machine.Pin.OUT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    led_toggle = 1

    while True:
        randint = random.randint(1, 100)
        sock.sendto("zkouska:{}|g".format(randint), (config.statsd_host, 8125))
        time.sleep(1)
        led_toggle = 1 - led_toggle
        builtin_led.value(led_toggle)
        # oled.toggle()
        oled.print(str(randint))


main()
