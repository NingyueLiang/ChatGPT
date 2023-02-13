import revChatGPT.Official
import json

from flask import Flask, request, jsonify, render_template

api = Flask(__name__)
chatbot = revChatGPT.Official.Chatbot(api_key = "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") 

@api.route('/response', methods=['POST'])
def get_answers():
    question = request.json.get('prompt')
    response = chatbot.ask(user_request = question) 
    return {"response": response["choices"][0]["text"]}
    # return {"success": 0, "response": response}
    