from flask import Flask, request
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv('OPENAI_API_KEY')  # replace with your actual key

@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    data = request.get_json()

    prompt = data['prompt']
    response = openai.Completion.create(engine="text-davinci-004", prompt=prompt, max_tokens=60)
    response_text = response.choices[0].text.strip()

    return {'response': response_text}

if __name__ == "__main__":
    app.run(port=5000)
