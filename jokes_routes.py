import random
from flask import Blueprint, jsonify, request
from resources import jokes


joke_bp = Blueprint("joke", __name__)


@joke_bp.get("/joke/random")
def random_joke():
    chosen = random.choice(jokes)
    return jsonify(chosen)


@joke_bp.get("/joke/<int:id>")
def get_joke(id):
    if id > 14:
        return (
            jsonify(
                {
                    "joke": None,
                    "message": "Error getting fact as id provided is out of range.",
                }
            ),
            400,
        )

    return jsonify(jokes[id])


@joke_bp.post("/joke/create")
def create_joke():
    data = request.get_json()
    return jsonify({"message": "Joke Created successfully", "data": data}), 201
