from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for simplicity (you can implement a file-based storage)
data_store = {}


@app.route("/store", methods=["POST"])
def store_data():
    key = request.json.get("key")
    value = request.json.get("value")
    data_store[key] = value
    return jsonify({"message": "Data stored successfully"}), 200


@app.route("/retrieve/<key>", methods=["GET"])
def retrieve_data(key):
    value = data_store.get(key)
    if value is None:
        return jsonify({"error": "Key not found"}), 404
    return jsonify({"key": key, "value": value}), 200


@app.route("/heartbeat", methods=["GET"])
def heartbeat():
    return jsonify({"status": "alive"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
