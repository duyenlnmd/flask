from flask import Blueprint
from flask import jsonify, make_response, request
from presenter.hoas import get_hoas, add_hoas, get_hoa
import json

hoa_views = Blueprint("hoa", __name__)

@hoa_views.route('/hoas', methods=['GET'])
def get_all_hoas():
    hoas = get_hoas()
    r = []
    for hoa in hoas:
        r.append(hoa.__dict__)
    return make_response(jsonify({"hoas": r}), 200)


@hoa_views.route('/hoa/<int:id>', methods=['GET'])
def get_hoa_name(id):
    hoa_name = get_hoa(id)
    r = []
    for hoa in hoa_name:
        r.append(hoa.__dict__)
    return make_response(jsonify({"hoa": r}), 200)


@hoa_views.route('/hoa', methods=['POST'])
def add_hoa_view():
    data = str(request.get_data(as_text=True))
    data = json.loads(data)

    if ("name" not in data and "address" not in data):
        return make_response(jsonify({"status": "bad request"}), 400)

    hoa_name = data["name"]
    hoa_address = data["address"]

    add_hoas(hoa_name, hoa_address)
    return make_response(jsonify({"status": "success"}), 200)