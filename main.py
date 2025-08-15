from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Récupération de la clé OpenAI depuis les variables d'environnement
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"response": "Aucun prompt reçu."}), 400

    prompt = data["prompt"]

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        response_text = completion.choices[0].message.content
        return jsonify({"response": response_text})
    except Exception as e:
        # Retourne l'erreur côté bot pour debug
        return jsonify({"response": f"Erreur côté bot: {str(e)}"}), 500

if __name__ == "__main__":
    # Render fournit le PORT via variable d'environnement
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # <--- autorise toutes les origines
