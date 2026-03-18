from etat_simulation import etat
import config


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