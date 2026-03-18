import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
    debut = time.time()

while GPIO.input(ECHO) == 1:
    fin = time.time()

duree = fin - debut
distance = duree * 17150
print(f"Distance : {distance:.1f} cm")

GPIO.cleanup()
