class Pot:

    def __init__(self, nom, humidite, seuil_sec):
        self.nom = nom
        self.humidite = humidite
        self.seuil_sec = seuil_sec

    def etat(self):
        if self.humidite < self.seuil_sec:
            return 'Arrosage nécessaire'
        else:
            return 'Sol ok'

    def arroser(self, reservoir):
        reservoir -= 0.5
        self.humidite += 10
        return reservoir

class Reservoir:
    def __init__(self, capacite, niveau, niveau_min):
        self.capacite  = capacite
        self.niveau    = niveau
        self.niveau_min = niveau_min

    def est_vide(self):
        return self.niveau <= self.niveau_min

    def donner(self, volume):
        if not self.est_vide() and self.niveau - volume > self.niveau_min:
            self.niveau -= volume
        return self.niveau

    def pourcentage(self):
        return self.niveau / self.capacite * 100