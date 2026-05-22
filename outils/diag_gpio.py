import RPi.GPIO as GPIO
import config

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(config.PIN_RELAIS_LED, GPIO.OUT)

if GPIO.input(config.PIN_RELAIS_LED) == 0:
    print('LED allumée')

else:
    print('LED éteinte')