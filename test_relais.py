import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)  # LED

print("Relais LED ON")
GPIO.output(22, GPIO.LOW)  # LOW = ON pour relais optocouplé
time.sleep(3)

print("Relais LED OFF")
GPIO.output(22, GPIO.HIGH)  # HIGH = OFF
GPIO.cleanup()