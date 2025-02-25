from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(message="Bienvenue sur mon site d'ouverture de booster !")

if __name__ == "__main__":
    app.run(debug=True)
