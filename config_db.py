import sqlite3

def initialiser_config_db():

    conn = sqlite3.connect('config.db')

    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS plantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT UNIQUE
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phases_plantes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plantes_id INTEGER,
            phase TEXT,
            led_active INTEGER,
            h_lever TEXT,
            h_coucher TEXT,
            temp_max_jour REAL,
            temp_min_jour REAL,
            temp_max_nuit REAL,
            temp_min_nuit REAL,
            hum_max INTEGER,
            hum_min INTEGER,
            hum_cible INTEGER,
            temp_crit REAL,
            duree_arrosage REAL,
            FOREIGN KEY (plantes_id) REFERENCES plantes(id)
        )
    ''')
    
    conn.commit()
    conn.close()


def peupler_config_db(nom, phase, led_active, h_lever, h_coucher, temp_max_jour, temp_min_jour,
                      temp_max_nuit, temp_min_nuit, hum_max, hum_min, hum_cible,
                      temp_crit, duree_arrosage):

    conn = sqlite3.connect('config.db')

    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id FROM plantes WHERE nom = ?''',
        (nom,)
    )

    result = cursor.fetchone()

    if result is None:
        cursor.execute('''
            INSERT INTO plantes (nom)
            VALUES (?)''',
            (nom,)
        )
        plante_id = cursor.lastrowid
    else:
        plante_id = result[0]

    cursor.execute('''
        INSERT INTO phases_plantes (
            plantes_id,
            phase,
            led_active,
            h_lever,
            h_coucher,
            temp_max_jour,
            temp_min_jour,
            temp_max_nuit,
            temp_min_nuit,
            hum_max,
            hum_min,
            hum_cible,
            temp_crit,
            duree_arrosage
            )
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''', 
            (
            plante_id, 
            phase, 
            led_active,
            h_lever,
            h_coucher,
            temp_max_jour,
            temp_min_jour,
            temp_max_nuit,
            temp_min_nuit,
            hum_max,
            hum_min,
            hum_cible,
            temp_crit,
            duree_arrosage
            )
            )
    
    conn.commit()
    conn.close()