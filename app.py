from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Hej! Min dummy API kører 🚀"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/info")
def info():
    return jsonify({
        "navn": "Emil",
        "projekt": "Dummy API",
        "version": "1.0"
    })

@app.route("/status")
def status():
    return jsonify({
        "online": True,
        "besked": "Alt kører som det skal 👍"
    })

@app.route("/vindmoeller")
def vindmoeller():
    return jsonify({
        "antal": 42,
        "lokation": "Nordsøen",
        "status": "online"
    })

if __name__ == "__main__":
    app.run(debug=True)