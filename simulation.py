from etat_simulation import etat
import random

def assecher():
    for pot in etat.pots:
        pot.humidite -= random.uniform(1.0, 3.0)

def evoluer_temperature():
    if etat.led and etat.temperature < 32:
        etat.temperature += random.uniform(0.0, 1.0)
    elif not etat.led and etat.temperature > 16 :
        etat.temperature -= random.uniform(0.0, 1.0)

def humidifier():
    etat.humidite_air += random.uniform(1.0, 3.0)

def assecher_air():
    etat.humidite_air -= random.uniform(1.0, 3.0)

def alterner_led():
    etat.led = not etat.led