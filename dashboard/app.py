from etat_simulation import etat
from flask import Flask, render_template
import config

app = Flask(__name__, template_folder='templates')

@app.route('/')
def accueil():
    if etat.jour:
        temp_max = config.TEMP_MAX_JOUR
        temp_min = config.TEMP_MIN_JOUR
    else:
        temp_max = config.TEMP_MAX_NUIT
        temp_min = config.TEMP_MIN_NUIT
    return render_template('index.html',
                           heure = etat.derniere_maj,
                           temperature = etat.temperature,
                           humidite = etat.humidite_air,
                           pots = etat.pots,
                           reservoir = etat.reservoir.pourcentage,
                           temp_max = temp_max,
                           temp_min = temp_min,
                           temp_crit = config.TEMP_CRIT,
                           hum_max = config.HUM_MAX,
                           hum_min = config.HUM_MIN
                           )


