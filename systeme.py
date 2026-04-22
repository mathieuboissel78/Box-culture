import config
from modeles import Pot, Reservoir

class EtatBox:
    def __init__(self):
        self.temperature = config.TEMPERATURE
        self.humidite_air = config.HUMIDITE_AIR
        self.pots = config.pots
        self.reservoir = config.reservoir
        self.led = 