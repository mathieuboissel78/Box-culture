from flask import Flask, jsonify, request
from etat_simulation import etat

app = Flask(__name__)

# GET 
@app.route('/api/status')
def api_climat():
    return jsonify({
        'temperature' : etat.temperature,
        'humidite' : etat.humidite_air,
        'phase' : etat.phase
    }), 200

# POST 
@app.route('/api/phase', methods = ['POST'])
def post_phase():
    data = request.get_json()
    phases_valides = ['croissance', 'floraison', 'sechage']

    if not data or 'phase' not in data:
        return jsonify({'erreur' : 'Phase manquante'}), 400
    
    phase = data['phase']

    if phase not in phases_valides:
        return jsonify({'erreur' : 'Phase incorrecte'}), 400
    
    etat.phase = phase
    return jsonify({'phase' : etat.phase}), 200

# PATCH
@app.route('/api/pot', methods = ['PATCH'])
def patch_seuil():
    data = request.get_json()

    if not data:
        return jsonify({'erreur' : 'Body JSON manquant'}), 400
    
    if 'seuil_sec' not in data:
        return jsonify({'erreur' : 'Champ seuil_sec manquant'}), 400
    
    seuil = data['seuil_sec']

    if not isinstance(seuil, (int, float)):
        return jsonify({'erreur' : 'seuil_sec doit être un nombre'}), 422
    
    if not 0 <= seuil <= 100:
        return jsonify({'erreur' : 'seuil_sec doit être compris entre 0 et 100'}), 422
    
    pot = None

    for p in etat.pots:
        if p.nom == data['pot']:
            pot = p

    if pot is None:
        return jsonify({'erreur' : 'Pot introuvable'}), 404
    
    pot.seuil_sec = seuil
    return jsonify({'statut' : 'OK', 'nouveau_seuil' : seuil}), 200