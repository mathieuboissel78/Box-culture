from etat_simulation import etat
import capteurs
from datetime import datetime
import historique
import alertes

def routine_surveillance():
	temperature, humidite_air = capteurs.lire_dht()

	if temperature is not None:
		etat.temperature = temperature

	if humidite_air is not None:
		etat.humidite_air = humidite_air

	niveau = capteurs.lire_niveau(etat.reservoir)
	etat.reservoir.niveau = niveau

	humidites_sol = []
	
	for pot in etat.pots:
		humidite_sol = capteurs.lire_humidite_sol(pot)
		if humidite_sol is not None:
			pot.humidite = humidite_sol
		humidites_sol.append(humidite_sol)

	etat.derniere_maj = datetime.now().strftime("%H:%M:%S")
	alertes.alerte_capteur(temperature, humidite_air, humidites_sol, niveau)
	historique.enregistrer_mesure()