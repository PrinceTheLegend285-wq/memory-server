from flask import Flask, request, jsonify

app = Flask(__name__)

# Temporary memory storage
database = {}

@app.route("/")
def home():
    return "Prince Memory Server Running 😎"

# Save memory
@app.route("/save", methods=["POST"])
def save():

    data = request.json

    user_id = str(data["user_id"])

    if user_id not in database:
        database[user_id] = []

    database[user_id].append({
        "role": data["role"],
        "content": data["content"]
    })

    return jsonify({
        "status": "saved"
    })

# Get memory
@app.route("/memory/<user_id>")
def memory(user_id):

    chats = database.get(user_id, [])

    return jsonify(chats[-10:])

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080
    )