from machine import Pin,ADC
from time import sleep, urequests

Pot = ADC(Pin(34))
Pot.atten(ADC.ATTN_11DB)

pines = [25, 33, 32, 26, 27, 14, 12, 13]
leds = [Pin(x, Pin.OUT) for x in pines]
url = "https://api.thingspeak.com/update?api_key=KFXD157MM6T7TH0L"

def reconectar():
    print('Fallo de conexión. Reconectando...')
    time.sleep(10)
    reset()

while True:
    try:
        time.sleep(2)
        pot_value = Pot.read()
        maximo = pot_value//455

        for i in range(len(leds)):
            if(i<maximo): leds[i].on()
            else: leds[i].off()

        print(pot_value, "\t",maximo)
        time.sleep(0.01)

        respuesta = urequest.get(url + "&field1=" + str(pot_value))
        print("Respuesta: " + str(respuesta.status_code))
        respuesta.close()
    
    except OSError as e:
        reconectar