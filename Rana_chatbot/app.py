from flask import Flask, render_template, request, jsonify
from model.model import Model
import uuid
from conversation import continue_conversation

app = Flask(__name__)
model = Model()

users = {}

@app.route("/", methods=["GET"])
def index():
    return render_template('chat.html')

@app.route("/get_reply", methods=["POST"])
def chat():
    msg = request.form["msg"]
    user_id = request.form["user_id"]
    if not user_id:
        user_id = str(uuid.uuid4())
    if user_id not in users:
        users[user_id] = { "user_id": user_id }
        reply = "Hello and welcome to Razan Aljuraysi Eye Hospital. My name is Rana, before I can help you with anything, I need to confirm your details"
        return {"reply_type": "text", "reply": reply, "user_id": user_id}
    
    reply_type, reply = continue_conversation(users[user_id], msg)
    if reply_type is not None:
        return {"reply_type": reply_type, "reply": reply, "user_id": user_id}
    reply_type, reply = model.predict(msg, users[user_id])
    return {"reply_type": reply_type, "reply": reply, "user_id": user_id}


if __name__ == '__main__':
    app.run()

