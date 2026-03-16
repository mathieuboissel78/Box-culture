from etat_simulation import etat

def lire_temperature():
    return etat.temperature

def lire_humidite_air():
    return etat.humidite_air

def lire_humidite_sol(pot):
    return pot.humidite

def lire_niveau(reservoir):
    return reservoir.niveau