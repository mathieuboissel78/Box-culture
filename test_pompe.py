from actionneurs.pompes import pompe_on, pompe_off
from etat_simulation import etat
import config
import time

time.sleep(2)

pompe_on(etat.pots[0], etat.reservoir)

time.sleep(4)

pompe_off()

print("Arrosage effectué")