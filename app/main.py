import base64
from flask import Flask, request, jsonify

app = Flask(__name__)


def add_cors(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    return response


@app.after_request
def after_request(response):
    return add_cors(response)


@app.route("/api/encode", methods=["POST", "OPTIONS"])
def encode():
    if request.method == "OPTIONS":
        return jsonify({}), 204

    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"success": False, "error": "Field 'text' is required"}), 400

    try:
        encoded = base64.b64encode(data["text"].encode("utf-8")).decode("utf-8")
        return jsonify({"success": True, "result": encoded})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/decode", methods=["POST", "OPTIONS"])
def decode():
    if request.method == "OPTIONS":
        return jsonify({}), 204

    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"success": False, "error": "Field 'text' is required"}), 400

    try:
        text = data["text"].strip()
        padding_needed = len(text) % 4
        if padding_needed:
            text += "=" * (4 - padding_needed)

        decoded = base64.b64decode(text.encode("utf-8")).decode("utf-8")
        return jsonify({"success": True, "result": decoded})
    except Exception as e:
        return jsonify({"success": False, "error": "Invalid Base64 input"}), 400


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
