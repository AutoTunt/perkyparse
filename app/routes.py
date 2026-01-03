from flask import Blueprint, request, jsonify
from .logic import process_character

main = Blueprint("main", __name__)

@main.route("/recommend-upgrades", methods=["POST"])
def recommend_upgrades():
    data = request.get_json()
    char_name = data.get("characterName")

    if not char_name:
        return jsonify({"error": "Missing characterName"}), 400

    result = process_character(char_name)
    return jsonify(result)