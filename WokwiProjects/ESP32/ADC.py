from machine import Pin, ADC
from time import sleep

Pot = ADC(Pin(34))
Pot.atten(ADC.ATTN_11DB)

pines = [25, 33, 32, 26, 27, 14, 12, 13]
leds = [Pin(x, Pin.OUT) for x in pines]

while True:
    
    pot_value = Pot.read()
    maximo = pot_value//455

    for i in range(len(leds)):
        if(i<maximo): leds[i].on()
        else: leds[i].off()

    print(pot_value, "\t",maximo)
    sleep(0.01)
