import sqlite3
from datetime import datetime

conn = sqlite3.connect('box_culture.db')

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute('''
    CREATE TABLE mesures_climat (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        horodatage DATETIME,
        temperature REAL,
        humidite_air REAL,
        phase TEXT
    )
''')


cursor.execute('''
    INSERT INTO mesures_climat (horodatage, temperature, humidite_air, phase)
    VALUES (?, ?, ?, ?)
''', (datetime.now(), 24.2, 58.0, 'croissance'))


cursor.execute('''
    CREATE TABLE arrosages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        horodatage DATETIME,
        pot_nom TEXT,
        duree REAL,
        niveau_reservoir_apres REAL, 
        mesure_climat_id INTEGER,
        FOREIGN KEY (mesure_climat_id) REFERENCES mesures_climat(id)
    )
''')

cursor.execute('''
    SELECT mesures_climat.temperature,
        arrosages.pot_nom,
        arrosages.horodatage
    FROM arrosages
    JOIN mesures_climat ON arrosages.horodatage = mesures_climat.horodatage
''')


cursor.execute('''
    SELECT * FROM mesures_climat;
''')
mesures = cursor.fetchall()
for ligne in mesures:
    print(ligne)


cursor.execute('''
    SELECT horodatage, temperature 
    FROM mesures_climat 
    WHERE temperature > 25;
''')
temp_sup = cursor.fetchall()
for ligne in temp_sup:
    print(ligne)


cursor.execute('''
    SELECT * FROM mesures_climat
    ORDER BY id DESC 
    LIMIT 10
''')
dernieres = cursor.fetchall()
for ligne in dernieres:
    print(ligne)


conn.commit()
conn.close()