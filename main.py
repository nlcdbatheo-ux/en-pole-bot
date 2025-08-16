from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Backend Flask fonctionne !"

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')

    # Pour le test, on renvoie juste la question reçue
    response = f"Réponse test : {question}"

    return jsonify({'answer': response})

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
