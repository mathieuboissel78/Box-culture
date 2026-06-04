import sqlite3 
from datetime import datetime
from systeme import meta

def initialiser_alertes():

    conn = sqlite3.connect('config.db')
    
    cursor = conn.cursor()

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alertes (
                    type_alerte TEXT PRIMARY KEY,
                    timestamp TEXT
                    )
                    ''')
    
    conn.commit()
    conn.close()


def enregistrer_alertes(type_alerte):

    conn = sqlite3.connect('config.db')

    cursor = conn.cursor()

    cursor.execute('''
                    SELECT timestamp FROM alertes 
                    WHERE type_alerte = ?
                    ''', (type_alerte,)
                    )
    
    result = cursor.fetchone()
    timestamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    if result is None:
        cursor.execute('''
                        INSERT INTO alertes (type_alerte, timestamp)
                        VALUES (?, ?) ''',
                        (type_alerte, timestamp)
                        )
    else:
        cursor.execute('''
                        UPDATE alertes 
                        SET timestamp = ?
                        WHERE type_alerte = ?
                        ''', (timestamp, type_alerte)
                    )
    
    conn.commit()
    conn.close()

def lire_alerte(type_alerte):

    conn = sqlite3.connect('config.db')

    cursor = conn.cursor()

    cursor.execute('''
                    SELECT timestamp FROM alertes
                    WHERE type_alerte = ?
                   ''', (type_alerte,)
                   )
    
    result = cursor.fetchone()

    if result is None:
        meta.derniere_alerte[type_alerte] is None
    else:
        derniere_alerte = datetime.strptime(result[0], "%d/%m/%Y, %H:%M:%S")
        meta.derniere_alerte[type_alerte] = derniere_alerte

    conn.close()