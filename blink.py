from machine import Pin
from time import sleep

# Led rouge sur la carte
led = Pin(0, Pin.OUT)
# Eteindre LED (logique inversée)
led.value(1)


def blink(count=3):
    # Clignoter = changer 2 fois d'état
    for i in range(count * 2):
        # changer l'état de l'entrée
        led.value(0 if led.value() == 1 else 1)
        sleep(1)
    # Eteindre la led
    led.value(1)


# Execution pour un temps limité
print('Blink x 10')
blink(10)
print("C'est fait")
