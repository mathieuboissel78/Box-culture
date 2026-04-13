import config
from etat_simulation import etat
import requests
if not config.SIMULATION:
    from capteurs import canal, lire_dht, lire_humidite_sol,lire_niveau


with open('token.txt', 'r') as f:
    lignes = f.read().splitlines()
    CHAT_ID = lignes[4]
    TOKEN = lignes[6]

def envoyer_alerte(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data = {'chat_id' : CHAT_ID, 'text' : message})


def alerte_temperature():
    if (etat.jour and etat.temperature > config.TEMP_MAX_JOUR) or (not etat.jour and etat.temperature > config.TEMP_MAX_NUIT):
        envoyer_alerte('Température élevée !')
    elif (etat.jour and etat.temperature < config.TEMP_MIN_JOUR) or (not etat.jour and etat.temperature < config.TEMP_MIN_NUIT):
        envoyer_alerte('Température basse !')

    

def alerte_reservoir():
    if etat.reservoir.est_vide():
        envoyer_alerte('Réservoir vide')


def alerte_capteur(temperature, humidite_air, humidites_sol, niveau):
    if temperature is None:
        envoyer_alerte('DHT22 inaccessible (température)')
    if humidite_air is None:
        envoyer_alerte('DHT22 inaccessible (humidité)')
    if niveau is None:
        envoyer_alerte('HC-SR04 inaccessible')

    for pot, humidite_sol in zip(etat.pots, humidites_sol):
        if humidite_sol is None:
            envoyer_alerte(f'Capteur sol {pot.nom} inaccessible')
        if not config.SIMULATION and canal.value >= config.VAL_AIR:
            envoyer_alerte(f'Capteur du {pot.nom} hors sol')
        if pot.est_sec:
            envoyer_alerte(f'{pot.nom} est sec')
    