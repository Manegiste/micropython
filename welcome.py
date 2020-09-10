# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep
import network
from ntptime import settime

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('manegisteflou', 'b3f4b8028c7e')

while not wlan.isconnected():
    pass

settime()

# ESP32 Pin assignment 
#i2c = I2C(-1, scl=Pin(22), sda=Pin(21))

# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World !', 0, 0)
oled.text(wlan.ifconfig(),0, 10)
oled.text('Hello, World 3!', 0, 20)
        
oled.show()

