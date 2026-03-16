import config
from modeles import Pot

def etat_pot(pot):
    if pot.humidite < pot.seuil_sec:
        return 'Arrosage nécessaire'
    else:
        return 'Sol ok'

def arroser(pot, reservoir, ):
    if reservoir >= config.RESERVOIR_MIN:
    	reservoir -= 0.5
    	pot.humidite += 10
    else:
    	print('Alerte : reservoir vide')
    return pot, reservoir