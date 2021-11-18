from flask import Blueprint, Flask, jsonify, request

api = Flask(__name__)


@api.route("/", methods=["GET"])
def base(content: str = None):
    return "OK"


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=8000)
