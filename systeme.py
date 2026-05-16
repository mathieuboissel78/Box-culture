from modeles import Pot, Reservoir
from dataclasses import dataclass, field

@dataclass
class EtatBox:
    temperature : float = 22.0
    humidite_air : float = 50.0
    led : bool = False
    jour : bool = False
    pots : list[Pot] = field(default_factory = list)
    reservoir : Reservoir = None
    brumisateur : bool = False
    extracteur_v2 : bool = False
    phase : str = None

etat = etatBox()

@dataclass
class Seuils:
    led_active : bool = False
    h_lever : str = "6"
    h_coucher : str = "0"
    temp_max_jour : float = 28.0
    temp_min_jour : float = 22.0
    temp_max_nuit : float = 24.0
    temp_min_nuit : float = 20.0
    hum_max : int = 70
    hum_min : int = 50
    hum_cible : int = 65

@dataclass
class Metadonnees:
    derniere_maj : str = None
    derniere_mesure_id : int = None
    derniere_alerte : dict = {}

    
