import json
from modeles import Pot, Reservoir
from etat_simulation import etat
import config

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
			'niveau_min' : reservoir.niveau_min,
			'hauteur' : reservoir.hauteur
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
		hauteur = donnees['reservoir']['hauteur']
		etat.reservoir = Reservoir(capacite, niveau, niveau_min, hauteur)
	except (FileNotFoundError, json.JSONDecodeError) as e:
		print('Erreur de fichier')
		etat.pots, etat.reservoir = config.pots, config.reservoir