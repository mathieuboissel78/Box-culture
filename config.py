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

CROISSANCE = True
FLORAISON = False
SECHAGE = False

if CROISSANCE:
    FLORAISON = False
    SECHAGE = False
    LED_ACTIVE = True
    H_LEVER = 6
    H_COUCHER = 22
    TEMP_CRIT = 30
    TEMP_MAX_JOUR = 28   
    TEMP_MIN_JOUR = 22
    TEMP_MAX_NUIT = 24
    TEMP_MIN_NUIT = 20 
    HUM_MAX = 70
    HUM_MIN = 50
    HUM_CIBLE = 65

if FLORAISON:
    CROISSANCE = False
    SECHAGE = False
    LED_ACTIVE = True
    H_LEVER = 8
    H_COUCHER = 20
    TEMP_CRIT = 28
    TEMP_MAX_JOUR = 26
    TEMP_MIN_JOUR = 20 
    TEMP_MAX_NUIT = 22
    TEMP_MIN_NUIT = 18
    HUM_MAX = 50
    HUM_MIN = 40
    HUM_CIBLE = 45


if SECHAGE:
    CROISSANCE = False
    FLORAISON = False
    LED_ACTIVE = False
    H_LEVER = 0
    H_COUCHER = 0
    TEMP_CRIT = 24
    TEMP_MAX_JOUR = 20
    TEMP_MIN_JOUR = 18
    TEMP_MAX_NUIT = 20
    TEMP_MIN_NUIT = 18 
    HUM_MAX = 55
    HUM_MIN = 45
    HUM_CIBLE = 50


TEMPERATURE = 22.0
HUMIDITE_AIR = 40
LED = True
VAL_AIR = 17514
VAL_SEC = 15254
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