import schedule
import threading
import time
import json
import config
from modeles import Pot, Reservoir
from etat_simulation import etat
from dashboard.app import app
import capteurs
import simulation

LOG = 'log.json'

def sauvegarder(pots, reservoir):
	pots_donnees = []
	for pot in pots:
		pot_dict = {
			'nom' : pot.nom,
			'humidite' : pot.humidite,
            'seuil_sec' : pot.seuil_sec
		}
		pots_donnees.append(pot_dict)
	donnees = {
		'pots' : pots_donnees,
		'reservoir' : {
			'capacite' : reservoir.capacite,
			'niveau' : reservoir.niveau,
			'niveau_min' : reservoir.niveau_min
		}
	}
	with open(LOG, 'w') as f:
		json.dump(donnees, f)
	print('Sauvegarde effectuée')

def charger():
	try:
		with open(LOG, 'r') as f:
			donnees = json.load(f)
		etat.pots = []
		for dict in donnees['pots']:
			dict_nom = dict['nom']
			dict_hum = dict['humidite']
			dict_seuil = dict['seuil_sec']
			etat.pots.append(Pot(dict_nom, dict_hum, dict_seuil))
		capacite = donnees['reservoir']['capacite']
		niveau = donnees['reservoir']['niveau']
		niveau_min = donnees['reservoir']['niveau_min']
		etat.reservoir = Reservoir(capacite, niveau, niveau_min)
	except (FileNotFoundError, json.JSONDecodeError) as e:
		print('Erreur de fichier')
		etat.pots, etat.reservoir = config.pots, config.reservoir

charger()

def routine_arrosage():

	for pot in etat.pots:
		while pot.humidite < pot.seuil_sec and not etat.reservoir.est_vide():
			pot.humidite += 10
			etat.reservoir.donner(0.5)
			print(f"État : {pot.etat()} | Humidité : {pot.humidite:.1f} | Réservoir : {etat.reservoir.niveau:.1f}")
			sauvegarder(etat.pots, etat.reservoir)

def routine_surveillance():
	etat.temperature = capteurs.lire_temperature()
	etat.humidite_air = capteurs.lire_humidite_air()
	for pot in etat.pots:
		pot.humidite = capteurs.lire_humidite_sol(pot)
	etat.reservoir.niveau = capteurs.lire_niveau(etat.reservoir)

def routine_climat():
	if etat.temperature >= config.TEMP_CRIT:
		print('Température critique')
		etat.extracteur_v2 = True
		etat.brumisateur = False
	elif etat.temperature >= config.TEMP_MAX or etat.humidite_air > config.HUM_MAX:
		print('Extracteur V2 activé')
		etat.extracteur_v2 = True
	else:
		print('Extracteur V1 activé')
		etat.extracteur_v2 = False
	if etat.humidite_air < config.HUM_MIN:
		print('Brumisateur ON')
		etat.brumisateur = True
	elif etat.humidite_air > config.HUM_CIBLE:
		print('Brumisateur OFF')
		etat.brumisateur = False
	if etat.brumisateur:
		etat.extracteur_v2 = False




if config.SIMULATION:
	schedule.every(config.INTERVALLE_SECHAGE).seconds.do(simulation.assecher)
	schedule.every(config.INTERVALLE_TEMPERATURE).seconds.do(simulation.evoluer_temperature)
	schedule.every(2).minutes.do(simulation.alterner_led)

schedule.every(10).minutes.do(routine_surveillance)
schedule.every(10).minutes.do(routine_climat)
schedule.every(config.INTERVALLE_ARROSAGE).seconds.do(routine_arrosage)


def lancer_schedule():
	while True:
		schedule.run_pending()
		time.sleep(1)

thread = threading.Thread(target=lancer_schedule)
thread.daemon = True
thread.start()

app.run(host='0.0.0.0', port=5000)
