# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import oled
import wifi
import webrepl
from lib.ftp import ftpserver

builtin_led = machine.Pin(25, machine.Pin.OUT)
builtin_led.value(0)

oled.setup()
wifi.setup(builtin_led)

webrepl.start()

ftpserver = ftpserver()
ftpserver.start_thread()
