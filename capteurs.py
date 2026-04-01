from etat_simulation import etat
import time
import config


TRIG = config.PIN_HC_SR04_TRIG
ECHO = config.PIN_HC_SR04_ECHO

if not config.SIMULATION:
    try:
        import RPi.GPIO as GPIO
        import board
        import adafruit_dht
        import adafruit_ads1x15
        import busio
        import adafruit_ads1x15.ads1115 as ADS
        from adafruit_ads1x15.analog_in import AnalogIn
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        dht = adafruit_dht.DHT22(board.D4)
        i2c = busio.I2C(board.SCL, board.SDA)
        ads = ADS.ADS1115(i2c)
        canal = AnalogIn(ads, 0)
    except Exception as e:
        print(f'Erreur initialisation capteurs : {e}')

def lire_dht():
    if config.SIMULATION:
        return etat.temperature, etat.humidite_air
    for i in range(3):
        try:
            temperature = dht.temperature
            humidite_air = dht.humidity
            return temperature, humidite_air
        except (RuntimeError, NameError) as e:
            time.sleep(2)
    print('DHT22 inaccessible')
    return None, None
    
    

def lire_humidite_sol(pot):
    if config.SIMULATION:
        return pot.humidite
    else:
        try:
            humidite_sol = (config.VAL_SEC - canal.value) / (config.VAL_SEC - config.VAL_HUM) * 100
            if canal.value >= config.VAL_AIR:
                print('Capteur hors sol')
                return None
            return min(100, max(0, humidite_sol))
        except (NameError, ValueError, IOError) as e:
            print(f'Erreur capteur capacitif : {e}')
            return None

def lire_niveau(reservoir):
    if config.SIMULATION:
        return reservoir.niveau
    else:
        try:
            GPIO.output(TRIG, GPIO.HIGH)
            time.sleep(0.00001)
            GPIO.output(TRIG, GPIO.LOW)

            while GPIO.input(ECHO) == 0:
                debut = time.time()

            while GPIO.input(ECHO) == 1:
                fin = time.time()

            duree = fin - debut
            distance = 34300 * duree / 2
            hauteur_eau = reservoir.hauteur - distance
            niveau = hauteur_eau / reservoir.hauteur * reservoir.capacite
            return niveau
        except (ValueError, IOError) as e:
            print(f'Erreur capteur réservoir : {e}')
            return None
    