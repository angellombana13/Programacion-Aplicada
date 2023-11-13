import network ,time
from machine import Pin

Led = Pin(2, Pin.OUT)

wifi_ssid = "Infinix HOT 11S"
wifi_password = "angel4138"

i = 0

try:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(wifi_ssid, wifi_password)
    
    while not sta_if.isconnected():
        i = i + 1
        Led.value(i%2)
        time.sleep(0.5)
        print("*"*i)
    Led.value(sta_if.isconnected())
except:
    pass