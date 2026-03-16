from modeles import Pot, Reservoir
# Ces nombres correspondent aux numéros de broches GPIO du Pi
# C'est le schéma de câblage traduit en code
PIN_DHT22            = 4    # Le capteur DHT22 est branché sur la broche 4
PIN_RELAIS_LED       = 22   # Le relais de la LED est sur la broche 22
PIN_EXTRACTEUR_V1    = 27   # Extracteur vitesse 1 sur la broche 27
PIN_EXTRACTEUR_V2    = 17   # Extracteur vitesse 2 sur la broche 17

RESERVOIR_MIN = 0.5

TEMPERATURE = 22.0
HUMIDITE_SOL = 60
HUMIDITE_AIR = 40
LED = True
TEMP_MAX = 27
TEMP_MIN = 22
TEMP_CRIT = 30
HUM_MAX = 80
HUM_MIN = 55
HUM_CIBLE = 65
reservoir = Reservoir(20, 10, 0.5)

pots = [
Pot('Pot1', 8, 30 )
]

SIMULATION = True

if SIMULATION:
    INTERVALLE_SECHAGE     = 10   # secondes
    INTERVALLE_TEMPERATURE = 5    # secondes
    INTERVALLE_ARROSAGE    = 15   # secondes
else:
    INTERVALLE_ARROSAGE    = 1800  # 30 minutes — seul intervalle utile en production