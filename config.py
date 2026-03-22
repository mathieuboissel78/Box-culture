from modeles import Pot, Reservoir
# Ces nombres correspondent aux numéros de broches GPIO du Pi
# C'est le schéma de câblage traduit en code
PIN_DHT22              = 4
PIN_EXTRACTEUR_V1      = 27
PIN_EXTRACTEUR_V2      = 17
PIN_RELAIS_LED         = 22
PIN_RELAIS_BRUMISATEUR = 26   # Phase 3
PIN_HC_SR04_TRIG       = 23
PIN_HC_SR04_ECHO       = 24
PIN_POMPE              = 25
PIN_PWM_VENTILO_1      = 18   # Phase 3
PIN_PWM_VENTILO_2      = 13   # Phase 3
PIN_PWM_VENTILO_HUMID  = 19   # Phase 3



TEMPERATURE = 22.0
HUMIDITE_AIR = 40
LED = True
TEMP_MAX = 27
TEMP_MIN = 22
TEMP_CRIT = 30
HUM_MAX = 80
HUM_MIN = 55
HUM_CIBLE = 65
VAL_AIR = 17514
VAL_SEC = 12216
VAL_HUM = 5680
reservoir = Reservoir(20, 10, 0.5, 30)

pots = [
Pot('Pot1', 8, 30 )
]

SIMULATION = False

if SIMULATION:
    INTERVALLE_SECHAGE     = 10   # secondes
    INTERVALLE_TEMPERATURE = 5    # secondes
    INTERVALLE_ARROSAGE    = 15   # secondes
    INTERVALLE_SURVEILLANCE = 30  # secondes
else:
    INTERVALLE_ARROSAGE    = 600  # 10 minutes
    INTERVALLE_SURVEILLANCE = 300 # 5 minutes

DUREE_ARROSAGE = 4