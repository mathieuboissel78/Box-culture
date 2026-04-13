class Pot:

    def __init__(self, nom, humidite, seuil_sec):
        self.nom = nom
        self.humidite = humidite
        self.seuil_sec = seuil_sec

    def __str__(self):
        return f"{self.nom} humidité : {self.humidite}% ( seuil : {self.seuil_sec})"
    
    @property
    def est_sec(self):
        return self.humidite < self.seuil_sec

    def etat(self):
        if self.humidite < self.seuil_sec:
            return 'Arrosage nécessaire'
        else:
            return 'Sol ok'


class Reservoir:
    def __init__(self, capacite, niveau, niveau_min, hauteur):
        self.capacite  = capacite
        self.niveau    = niveau
        self.niveau_min = niveau_min
        self.hauteur = hauteur

    def est_vide(self):
        return self.niveau <= self.niveau_min

    def donner(self, volume):
        if not self.est_vide() and self.niveau - volume > self.niveau_min:
            self.niveau -= volume
        return self.niveau
    
    @property
    def pourcentage(self):
        return self.niveau / self.capacite * 100