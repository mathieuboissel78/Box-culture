import RPi.GPIO as GPIO
import time
import config
from actionneurs.relais import led_off, led_on

GPIO.setmode(GPIO.BCM)
GPIO.setup(config.PIN_RELAIS_LED, GPIO.OUT)

time.sleep(2)

led_on()

time.sleep(5)

led_off()


