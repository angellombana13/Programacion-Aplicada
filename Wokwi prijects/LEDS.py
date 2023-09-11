from machine import Pin
from utime import sleep
import time

led1=Pin(13,Pin.OUT)
led2=Pin(12,Pin.OUT)
led3=Pin(14,Pin.OUT)
led4=Pin(27,Pin.OUT)
led5=Pin(26,Pin.OUT)
led6=Pin(25,Pin.OUT)
led7=Pin(33,Pin.OUT)
led8=Pin(32,Pin.OUT)

while True:
  led1.value(1)
  sleep(0.2)
  led1.value(0)
  
  led2.value(1)
  sleep(0.2)
  led2.value(0)

  led3.value(1)
  sleep(0.2)
  led3.value(0)

  led4.value(1)
  sleep(0.2)
  led4.value(0)

  led5.value(1)
  sleep(0.2)
  led5.value(0)

  led6.value(1)
  sleep(0.2)
  led6.value(0)

  led7.value(1)
  sleep(0.2)
  led7.value(0)

  led8.value(1)
  sleep(0.2)
  led8.value(0)
