from etat_simulation import etat
import capteurs
from datetime import datetime

def routine_surveillance():
	temperature, humidite_air = capteurs.lire_dht()
	if temperature is not None:
		etat.temperature = temperature
	if humidite_air is not None:
		etat.humidite_air = humidite_air
	for pot in etat.pots:
		humidite_sol = capteurs.lire_humidite_sol(pot)
		if humidite_sol is not None:
			pot.humidite = humidite_sol
	etat.reservoir.niveau = capteurs.lire_niveau(etat.reservoir)
	etat.derniere_maj = datetime.now().strftime("%H:%M:%S")