from flask import Flask, jsonify, request
import random
from datetime import datetime

app = Flask(__name__)

# In-memory “plays” store
plays = [
    {"id": 1, "type": "dunk",   "description": "Monster slam in Q4", "timestamp": "2025-05-01T20:15:00Z"},
    {"id": 2, "type": "assist","description": "Threaded the needle", "timestamp": "2025-05-02T18:30:00Z"}
]

# LeBron facts/quotes
lebron_facts = [
    "King James scored 61 points in a single game (2014).",
    "LeBron has 4 NBA championships, fam.",
    "LeBron’s real name is LeBron Raymone James Sr.",
    "\"I’m coming home.\" – The Decision, 2010."
]

@app.route('/plays', methods=['GET'])
def get_plays():
    return jsonify({'plays': plays}), 200

@app.route('/plays/<int:play_id>', methods=['GET'])
def get_play(play_id):
    play = next((p for p in plays if p['id'] == play_id), None)
    if not play:
        return jsonify({'error': 'Play not found'}), 404
    return jsonify(play), 200

@app.route('/plays', methods=['POST'])
def create_play():
    data = request.get_json()
    if not data or 'type' not in data or 'description' not in data:
        return jsonify({'error': 'Type and description are required'}), 400

    new_id = max(p['id'] for p in plays) + 1 if plays else 1
    play = {
        'id': new_id,
        'type': data['type'],
        'description': data['description'],
        'timestamp': datetime.utcnow().isoformat() + 'Z'
    }
    plays.append(play)
    return jsonify(play), 201

@app.route('/plays/<int:play_id>', methods=['PUT'])
def update_play(play_id):
    play = next((p for p in plays if p['id'] == play_id), None)
    if not play:
        return jsonify({'error': 'Play not found'}), 404

    data = request.get_json()
    play['type'] = data.get('type', play['type'])
    play['description'] = data.get('description', play['description'])
    return jsonify(play), 200

@app.route('/plays/<int:play_id>', methods=['DELETE'])
def delete_play(play_id):
    global plays
    plays = [p for p in plays if p['id'] != play_id]
    return jsonify({}), 204

@app.route('/lebron', methods=['GET'])
def lebron():
    fact = random.choice(lebron_facts)
    return jsonify({"lebron_fact": fact}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)

