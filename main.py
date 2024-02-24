from flask import Flask, request, jsonify
from llama_index.llms import OpenAI, ChatMessage, LLMMetadata
from llama_index.agent import ReActAgent

app = Flask(__name__)

llm = OpenAI(
    model="gpt-35-turbo-16k",
    api_key="sk-jfoNrqmyPiA_xop2fJ53Wg",
    api_base="https://4veynppxjm.us-east-1.awsapprunner.com",
    temperature=0.1
)

@app.route("/")
def home():
    return "Home"

@app.route("/send", methods=["POST"])
def send():
    data = request.get_json()
    print(data["prompt"])
    
    return llm.chat([ChatMessage(role="user",content=data["prompt"])]).message.content, 201


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)