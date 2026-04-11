import sqlite3
from datetime import datetime
from etat_simulation import etat

def initialiser_db():

    conn = sqlite3.connect('historique.db')

    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mesures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            humidite_air REAL,
            humidite_pot1 REAL,
            niveau_reservoir REAL
        )
    ''')

    conn.commit()
    conn.close()

def enregistrer_mesure():

    conn = sqlite3.connect('historique.db')

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO mesures (timestamp, temperature, humidite_air, humidite_pot1, niveau_reservoir)
        VALUES (?,?,?,?,?)
    ''', (datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), etat.temperature, etat.humidite_air, etat.pots[0].humidite, etat.reservoir.niveau))

    conn.commit()
    conn.close()