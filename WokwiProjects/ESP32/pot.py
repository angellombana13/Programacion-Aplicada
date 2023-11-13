from machine import Pin,ADC
from time import sleep

Pot = ADC(Pin(34))
Pot.atten(ADC.ATTN_11DB)

while True:
    pot_value = Pot.read()
    print(pot_value,'hola')
    sleep(1)
    