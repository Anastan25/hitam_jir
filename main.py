from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.json
    user_input = data.get("text", "")
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a gangster slang translator. Translate all input into natural street slang, with Crips/Black culture influence. Don’t be too formal."},
            {"role": "user", "content": user_input}
        ]
    )
    
    result = response.choices[0].message.content.strip()
    return jsonify({"result": result})