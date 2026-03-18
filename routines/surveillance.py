from etat_simulation import etat
import capteurs

def routine_surveillance():
	etat.temperature = capteurs.lire_temperature()
	etat.humidite_air = capteurs.lire_humidite_air()
	for pot in etat.pots:
		pot.humidite = capteurs.lire_humidite_sol(pot)
	etat.reservoir.niveau = capteurs.lire_niveau(etat.reservoir)