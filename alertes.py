import config
from etat_simulation import etat
import requests
from datetime import datetime, timedelta


with open('token.txt', 'r') as f:
    lignes = f.read().splitlines()
    CHAT_ID = lignes[4]
    TOKEN = lignes[6]

def envoyer_alerte(message, type_alerte):
    derniere = etat.derniere_alerte.get(type_alerte)
    if derniere is None or datetime.now() - derniere > timedelta(hours = 1):
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data = {'chat_id' : CHAT_ID, 'text' : message})
        etat.derniere_alerte[type_alerte] = datetime.now()


def alerte_temperature():
    if (etat.jour and etat.temperature > config.TEMP_MAX_JOUR) or (not etat.jour and etat.temperature > config.TEMP_MAX_NUIT):
        envoyer_alerte('Température élevée !', 'temperature')
    elif (etat.jour and etat.temperature < config.TEMP_MIN_JOUR) or (not etat.jour and etat.temperature < config.TEMP_MIN_NUIT):
        envoyer_alerte('Température basse !', 'temperature')

    

def alerte_reservoir():
    if etat.reservoir.est_vide():
        envoyer_alerte('Réservoir vide', 'reservoir')


def alerte_capteur(temperature, humidite_air, humidites_sol, niveau):
    if temperature is None:
        envoyer_alerte('DHT22 inaccessible (température)', 'dht22')
    if humidite_air is None:
        envoyer_alerte('DHT22 inaccessible (humidité)', 'dht22')
    if niveau is None:
        envoyer_alerte('HC-SR04 inaccessible', 'hc-sr04')

    for pot, humidite_sol in zip(etat.pots, humidites_sol):
        if humidite_sol is None:
            envoyer_alerte(f'Capteur sol {pot.nom} inaccessible', 'capteur_sol')
        elif humidite_sol == 'hors_sol':
            envoyer_alerte(f'Capteur du {pot.nom} hors sol', 'hors_sol')
        if pot.est_sec:
            envoyer_alerte(f'{pot.nom} est sec', 'est_sec')
    