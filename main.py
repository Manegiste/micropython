# Complete project details at https://RandomNerdTutorials.com

from machine import Pin, I2C
import ssd1306
from time import sleep
import network
from ntptime import settime
import utime


#attach to a network as a station
#this will make us able to set time using NTP
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('manegisteflou', 'b3f4b8028c7e')

while not wlan.isconnected():
    pass

settime()
hour="{0:02d}:{1:02d}:{2:02d}".format( utime.localtime()[3], utime.localtime()[4], utime.localtime()[5])

# ###########################################
# Initialize display 
#
# ###########################################

# ESP8266 Pin assignment
i2c = I2C(-1, scl=Pin(5), sda=Pin(4))

oled_width = 128
oled_height = 32
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Hello, World !', 0, 0)
oled.text( hour, 0, 10)
oled.text('Hello, World 3!', 0, 20)
        
oled.show()

