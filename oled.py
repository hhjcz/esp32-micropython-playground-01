import machine
from lib.ssd1306 import SSD1306_I2C
from lib.writer import Writer
from lib import freesans20

OLED_WIDTH = 128
OLED_HEIGHT = 64
OLED_SCL = 15
OLED_SDA = 4

ssd = None
wri = None
is_inverted = 1


def setup():
    global ssd, wri
    # enable OLED
    p16 = machine.Pin(16, machine.Pin.OUT)
    p16.value(1)

    pscl = machine.Pin(OLED_SCL, machine.Pin.OUT)
    psda = machine.Pin(OLED_SDA, machine.Pin.OUT)
    i2c = machine.I2C(scl=pscl, sda=psda)
    ssd = SSD1306_I2C(OLED_WIDTH, OLED_HEIGHT, i2c)

    # sample graphics
    # rhs = OLED_WIDTH - 1
    # bts = OLED_HEIGHT - 1
    # ssd.line(0, 20, 20, 0, 1)
    # ssd.line(rhs - 20, 0, rhs, 20, 1)
    # ssd.line(rhs - 20, bts, rhs, bts - 20, 1)
    # ssd.line(0, bts - 20, 20, bts, 1)
    # square_side = 10
    # ssd.fill_rect(0, 0, square_side, square_side, 1)
    # ssd.fill_rect(rhs - square_side, 0, square_side, square_side, 1)
    # ssd.fill_rect(rhs - square_side, bts - square_side, square_side, square_side, 1)
    # ssd.fill_rect(0, bts - square_side, square_side, square_side, 1)

    # sample text
    # wri = Writer(ssd, freesans20, verbose=False)
    # print_string('Skol !!!\n', y=2, x=30)
    ssd.show()


def print_string(text, y=30, x=50):
    global wri, ssd
    # Writer.set_clip(True, True)
    # Writer.set_textpos(y, x)
    # wri.printstring(text + '\n')
    ssd.fill(0)
    ssd.text(str(text), x, y)
    ssd.show()


def toggle():
    global is_inverted
    is_inverted = 1 - is_inverted
    ssd.invert(is_inverted)

