from flask import Flask, request, jsonify
import os
import openai

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"response": "Aucun message reçu."}), 400

    prompt = data["prompt"]

    try:
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        answer = completion.choices[0].message.content
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"response": f"Erreur OpenAI : {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
