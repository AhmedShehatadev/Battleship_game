from http import HTTPStatus
import pdb

from flask import abort, Flask, jsonify, json, request

from battleship.models import *

app = Flask(__name__)

game_instance = None

@app.route('/battleship', methods=['POST'])
def create_battleship_game():
    global game_instance = BattleshipGameBoard()
    req_data = request.get_json()

    pdb.set_trace()


    for ship in req_data['ships']:
        game_instance.add_ship(Ship(ship["x"],ship["y"],ship["direction"],ship["size"]))

    game_instance.ships = game_ships

    print(game_instance.ships)

    return json.dumps(request.json)


@app.route('/battleship', methods=['PUT'])
def shot():
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED


@app.route('/battleship', methods=['DELETE'])
def delete_battleship_game():
    return jsonify({}), HTTPStatus.NOT_IMPLEMENTED3D
