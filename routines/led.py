from datetime import datetime
import config
from actionneurs.relais import led_on, led_off
from etat_simulation import etat

def routine_led():
    
    heure = datetime.now().hour

    if config.H_LEVER <=  heure < config.H_COUCHER:
        etat.jour = True
    else:
        etat.jour = False

    if config.LED_ACTIVE and etat.jour:
        led_on()
        print(f"[LED] {datetime.now().strftime('%H:%M:%S')}, {etat.phase}, lever : {config.H_LEVER}, coucher : {config.H_COUCHER}, led active : {config.LED_ACTIVE}, LED ON", flush=True)
    else: 
        led_off()
        print(f"[LED] {datetime.now().strftime('%H:%M:%S')}, {etat.phase}, lever : {config.H_LEVER}, coucher : {config.H_COUCHER}, led active : {config.LED_ACTIVE},LED OFF", flush=True)