from flask import Flask, request, jsonify
from pyngrok import ngrok

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json['message']
    bot_response = get_response(user_input)
    save_chat(user_input, bot_response)
    return jsonify({"response": bot_response})

# Start ngrok tunnel
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

app.run(port=5000)
