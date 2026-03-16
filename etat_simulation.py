import config
from modeles import Pot, Reservoir

class EtatSimulation:
    def __init__(self):
        self.temperature = config.TEMPERATURE
        self.humidite_air = config.HUMIDITE_AIR
        self.led = config.LED
        self.pots = config.pots
        self.reservoir = config.reservoir
        self.brumisateur = False
        self.extracteur_v2 = False

etat = EtatSimulation()


