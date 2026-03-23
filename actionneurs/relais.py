import RPi.GPIO as GPIO
import config 
import time

if not config.SIMULATION:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(config.PIN_RELAIS_LED, GPIO.OUT)
    GPIO.setup(config.PIN_EXTRACTEUR_V1, GPIO.OUT)
    GPIO.setup(config.PIN_EXTRACTEUR_V2, GPIO.OUT)
    GPIO.setup(config.PIN_RELAIS_BRUMISATEUR, GPIO.OUT)
    GPIO.output(config.PIN_RELAIS_LED, GPIO.HIGH)          # Eteint les relais par défaut au démarage
    GPIO.output(config.PIN_EXTRACTEUR_V1, GPIO.HIGH)
    GPIO.output(config.PIN_EXTRACTEUR_V2, GPIO.HIGH)
    GPIO.output(config.PIN_RELAIS_BRUMISATEUR, GPIO.HIGH)

def extracteur_v1_on():
    if not config.SIMULATION:
        GPIO.output(config.PIN_EXTRACTEUR_V2, GPIO.HIGH)    # Eteint V2 au cas où / GPIO.HIGH = OFF
        time.sleep(1)
        GPIO.output(config.PIN_EXTRACTEUR_V1, GPIO.LOW)     # Allume V1 / GPIO.LOW = ON

def extracteur_v1_off():
    if not config.SIMULATION:
        GPIO.output(config.PIN_EXTRACTEUR_V1, GPIO.HIGH)

def extracteur_v2_on():
    if not config.SIMULATION:
        GPIO.output(config.PIN_EXTRACTEUR_V1, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(config.PIN_EXTRACTEUR_V2, GPIO.LOW)

def extracteur_v2_off():
    if not config.SIMULATION:
        GPIO.output(config.PIN_EXTRACTEUR_V2, GPIO.HIGH)

def led_on():
    if not config.SIMULATION:
        GPIO.output(config.PIN_RELAIS_LED, GPIO.LOW)

def led_off():
    if not config.SIMULATION:
        GPIO.output(config.PIN_RELAIS_LED, GPIO.HIGH)

def brumisateur_on():
    if not config.SIMULATION:
        GPIO.output(config.PIN_RELAIS_BRUMISATEUR, GPIO.LOW)

def brumisateur_off():
    if not config.SIMULATION:
        GPIO.output(config.PIN_RELAIS_BRUMISATEUR, GPIO.HIGH)