from etat_simulation import etat
from sauvegarde import sauvegarder
from actionneurs.pompes import pompe_on, pompe_off
import time
import config

def routine_arrosage():

	for pot in etat.pots:
		if pot.est_sec and not etat.reservoir.est_vide():
			pompe_on(pot, etat.reservoir)
			time.sleep(config.DUREE_ARROSAGE)
			pompe_off()
			print(f"État : {pot.etat()} | Humidité : {pot.humidite:.1f} | Réservoir : {etat.reservoir.niveau:.1f}")
			sauvegarder(etat.pots, etat.reservoir)
			
