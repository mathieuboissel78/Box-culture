import RPi.GPIO as GPIO
import config

if not config.SIMULATION:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(config.PIN_POMPE, GPIO.OUT)

def pompe_on(pot, reservoir):
    if config.SIMULATION:
        pot.humidite += 10
        reservoir.donner(0.1)
    else:
        GPIO.output(config.PIN_POMPE, GPIO.HIGH)

def pompe_off():
    if not config.SIMULATION:
        GPIO.output(config.PIN_POMPE, GPIO.LOW)
