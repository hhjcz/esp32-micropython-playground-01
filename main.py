import network
import socket
import machine
import time
import random


def setup():
    pin25 = machine.Pin(25, machine.Pin.OUT)
    pin25.value(0)

    nic = network.WLAN(network.STA_IF)
    nic.active(True)
    nic.connect("heureka_hotspot", "Heureka_2007")
    while not nic.isconnected():
        time.sleep(1)

    pin25.value(nic.isconnected())


def main():
    pin25 = machine.Pin(25, machine.Pin.OUT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i = 1

    while True:
        sock.sendto("zkouska:{}|g".format(random.randint(1, 100)), ("195.181.211.119", 8125))
        time.sleep(1)
        i = 1 - i
        pin25.value(i)


# setup()
main()
