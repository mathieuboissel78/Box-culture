from etat_simulation import etat
from sauvegarde import sauvegarder

def routine_arrosage():

	for pot in etat.pots:
		while pot.humidite < pot.seuil_sec and not etat.reservoir.est_vide():
			pot.humidite += 10
			etat.reservoir.donner(0.5)
			print(f"État : {pot.etat()} | Humidité : {pot.humidite:.1f} | Réservoir : {etat.reservoir.niveau:.1f}")
			sauvegarder(etat.pots, etat.reservoir)