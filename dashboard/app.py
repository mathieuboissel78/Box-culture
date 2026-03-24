from etat_simulation import etat
from flask import Flask, render_template
import config
from datetime import datetime

app = Flask(__name__, template_folder='templates')

@app.route('/')
def accueil():
    return render_template('index.html',
                           heure = etat.derniere_maj,
                           temperature = etat.temperature,
                           humidite = etat.humidite_air,
                           pots = etat.pots,
                           reservoir = etat.reservoir.pourcentage(),
                           temp_max = config.TEMP_MAX,
                           temp_min = config.TEMP_MIN,
                           temp_crit = config.TEMP_CRIT,
                           hum_max = config.HUM_MAX,
                           hum_min = config.HUM_MIN
                           )


