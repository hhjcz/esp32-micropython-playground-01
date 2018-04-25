# This file is executed on every boot (including wake-boot from deepsleep)
import machine
import oled
import wifi

builtin_led = machine.Pin(25, machine.Pin.OUT)
builtin_led.value(0)

oled.setup()
wifi.setup(builtin_led)
