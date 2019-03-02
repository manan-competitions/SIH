import os
import json
import requests
import time
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
count = 0
data = {
    'transformers': json.load(open('db/transformers.json')),
    'inventory': json.load(open('db/inventory.json')),
    'tickets': json.load(open('db/tickets.json')),
    'health-history': json.load(open('db/health-history.json'))
}

no_of_t=0


# Views
@app.route('/', methods=['GET'])
def base_index():
    return "Home Page for edge-triggered", 200


@app.route('/transformers', methods=['GET'])
@cross_origin()
def get_transformer_list():
    return jsonify(data['transformers']), 200


@app.route('/inventory', methods=['GET'])
@cross_origin()
def get_inventory_list():
    return jsonify(inventory=data['inventory'], status_code=200)


@app.route('/tickets', methods=['GET'])
@cross_origin()
def get_tickets_list():
    return jsonify(data['tickets']), 200


@app.route('/tickets-per-transformer', methods=['POST'])
@cross_origin()
def get_tickets_per_transformer_list():
    try:
        data = request.get_json()
        t_id = data['t_id']
    except:
        return "KeyError: t_id", 500

    tickets = {}
    for ticket_id, ticket_value in data['tickets'].items():
        if ticket_id == t_id:
            tickets[ticket_id] = ticket_value

    return jsonify(tickets), 200


@app.route('/health-history', methods=['GET'])
@cross_origin()
def get_health_history_list():
    return jsonify(data['health-history']), 200


@app.route('/unresolved-tickets', methods=['GET'])
@cross_origin()
def get_unresolved_tickets():
    unresolved_tickets = {}

    for ticket_id, ticket_data in data['tickets'].items():
        if not ticket_data['is_resolved']:
            unresolved_tickets[ticket_id] = ticket_data
            data['tickets'][ticket_id]['is_new'] = False
    json.dump(data['tickets'], open('db/tickets.json', 'w'), indent=4)
    return jsonify(unresolved_tickets), 200


@app.route('/low-inventory', methods=['GET'])
@cross_origin()
def get_low_inventory():
    low_inventory = {}

    for inv_name, inv_data in data['inventory'].items():
        if inv_data['amount'] < inv_data['threshold']:
            low_inventory[inv_name] = inv_data

    return jsonify(low_inventory), 200


# updates
@app.route('/update-transformers', methods=['POST'])
@cross_origin()
def update_transformers_list():
    try:
        request_data = request.get_json()
        t_id = request_data['t_id']
        new_data = request_data['new_data']
    except:
        return "KeyError: t_id, new_data", 500

    for new_key, new_value in new_data.items():
        data['transformers'][t_id][new_key] = new_value

    json.dump(data['transformers'], open('db/transformers.json', 'w'), indent=4)
    update_health_history(t_id, new_data['health'])
    return "ok", 200


@app.route('/update-inventory', methods=['POST'])
@cross_origin()
def update_inventory_list(product_count_json = None):
    try:
        request_data = request.get_json()
        product_count_json = request_data['product_count_json']
    except:
        pass

    for product, count in product_count_json.items():
        data['inventory'][product]["amount"] = str(int(data['inventory'][product]["amount"])-int(product_count_json[product]["amount"]))
    json.dump(data['inventory'], open('db/inventory.json', 'w'), indent=4)
    return "ok", 200


@app.route('/update-ticket', methods=['POST'])
@cross_origin()
def update_ticket_list():
    try:
        request_data = request.get_json()
        t_id = request_data['t_id']
        ticket_data = request_data['ticket_data']
    except:
        return "KeyError: t_id, ticket_data", 500

    for ticket_data_key, ticket_data_value in ticket_data.items():
        data['tickets'][t_id][ticket_data_key] = ticket_data_value
    json.dump(data['tickets'], open('db/tickets.json', 'w'), indent=4)
    update_inventory_list(ticket_data['products_used'])

    return "ok", 200


@app.route('/update-health', methods=['POST'])
@cross_origin()
def update_health_history(t_id = None, health_data = None):
    try:
        request_data = request.get_json()
        t_id = request_data['t_id']
        health_data = data['health_data']
    except:
        pass

    for health_data_key, health_data_value in health_data.items():
        data['health-history'][t_id][health_data_key][time.ctime()] = health_data_value
    json.dump(data['health-history'], open('db/health-history.json', 'w'), indent=4)
    return "ok", 200


@app.route('/add-transformer', methods=['POST'])
@cross_origin()
def add_transformer():
    new_data = request.get_json()
    t_location = new_data['location']
    no_of_t += 1
    t_id = no_of_t
    data['transformers'][t_id] = {
        "location": t_location,
        "health": {
            "oil": "-",
            "current": "-"
        }
    }
    json.dump(data['transformers'], open('db/transformers.json', 'w'), indent=4)
    return "ok", 200


@app.route('/add-inventory', methods=['POST'])
@cross_origin()
def add_inventory():
    new_data = request.get_json()
    new_inventory_name = new_data['name']
    data['inventory'][new_inventory_name] = {
        "amount": new_data["amount"],
        "threshold": new_data["threshold"]
    }
    json.dump(data['inventory'], open('db/inventory.json', 'w'), indent=4)
    return "ok", 200


if __name__ == '__main__':
    app.run(debug=True)
