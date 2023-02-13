import revChatGPT.Official
import json

from flask import Flask, request, jsonify, render_template

api = Flask(__name__)
chatbot = revChatGPT.Official.Chatbot(api_key = "key") 

@api.route('/response', methods=['POST'])
def get_answers():
    question = request.json.get('prompt')
    response = chatbot.ask(user_request = question) 
    return {"response": response["choices"][0]["text"]}
    # return {"success": 0, "response": response}
    
