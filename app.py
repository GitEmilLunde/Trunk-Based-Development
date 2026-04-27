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

if __name__ == "__main__":
    app.run(debug=True)
