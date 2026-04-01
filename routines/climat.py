from etat_simulation import etat
import config
import actionneurs.relais as relais



def routine_climat():

	if etat.jour:
		temp_max = config.TEMP_MAX_JOUR
		temp_min = config.TEMP_MIN_JOUR
	else:
		temp_max =  config.TEMP_MAX_NUIT
		temp_min = config.TEMP_MIN_NUIT

	if etat.temperature >= config.TEMP_CRIT:
		print('Température critique')
		etat.extracteur_v2 = True
		etat.brumisateur = False
		relais.extracteur_v1_off()
		relais.extracteur_v2_on()
		relais.brumisateur_off()
	elif etat.temperature >= temp_max or etat.humidite_air > config.HUM_MAX:
		print('Extracteur V2 activé')
		etat.extracteur_v2 = True
		relais.extracteur_v1_off()
		relais.extracteur_v2_on()
	else:
		print('Extracteur V1 activé')
		etat.extracteur_v2 = False
		relais.extracteur_v2_off()
		relais.extracteur_v1_on()
		
	if etat.humidite_air < config.HUM_MIN:
		print('Brumisateur ON')
		etat.brumisateur = True
		relais.brumisateur_on()
	elif etat.humidite_air > config.HUM_CIBLE:
		print('Brumisateur OFF')
		etat.brumisateur = False
		relais.brumisateur_off()

	if etat.brumisateur:
		relais.extracteur_v2_off()
		relais.extracteur_v1_on()
		etat.extracteur_v2 = False