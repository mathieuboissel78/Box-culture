from etat_simulation import etat
from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def accueil():
    return render_template('index.html',
                           temperature=etat.temperature,
                           humidite=etat.humidite_air,
                           pots=etat.pots,
                           reservoir=etat.reservoir.pourcentage()
                           )


