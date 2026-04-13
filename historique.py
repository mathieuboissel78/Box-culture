import sqlite3
from datetime import datetime
from etat_simulation import etat
import config

def initialiser_db():

    conn = sqlite3.connect('historique.db')

    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''               
        CREATE TABLE IF NOT EXISTS mesures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            temperature REAL,
            humidite_air REAL,
            humidite_pot1 REAL,
            niveau_reservoir REAL,
            phase TEXT
        )
    ''')

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS arrosages (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   timestamp TEXT,
                   pot_nom TEXT,
                   duree REAL,
                   niveau_reservoir_apres REAL,
                   mesure_id INTEGER,
                   FOREIGN KEY (mesure_id) REFERENCES mesures(id)
                )
''')

    conn.commit()
    conn.close()

def enregistrer_mesure():

    conn = sqlite3.connect('historique.db')

    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO mesures (timestamp, temperature, humidite_air, humidite_pot1, niveau_reservoir, phase)
        VALUES (?,?,?,?,?,?)
    ''', (datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), etat.temperature, etat.humidite_air, etat.pots[0].humidite, etat.reservoir.niveau, etat.phase)
    )

    etat.derniere_mesure_id = cursor.lastrowid

    conn.commit()
    conn.close()

def enregistrer_arrosage():

    conn = sqlite3.connect('historique.db')

    cursor = conn.cursor()

    cursor.execute('''
                   INSERT INTO arrosages (timestamp, pot_nom, duree, niveau_reservoir_apres, mesure_id)
                   VALUES (?,?,?,?,?)
                   ''', (datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), etat.pots[0].nom, config.DUREE_ARROSAGE, etat.reservoir.niveau, etat.derniere_mesure_id)
                   )
    
    conn.commit()
    conn.close()