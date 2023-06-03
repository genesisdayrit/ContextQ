from flask import Flask, request
from flask_cors import CORS
import openai
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app)  # Enable CORS

load_dotenv()  # take environment variables from .env.
openai.api_key = os.getenv('OPENAI_API_KEY')  # replace with your actual key

@app.route('/api/generate-response', methods=['POST'])
def generate_response():
    data = request.get_json()

    prompt = data['prompt']
    response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=120)

    print(response)  # Print the complete response for debugging

    response_text = response.choices[0].text.strip()

    return {'response': response_text}

if __name__ == "__main__":
    app.run(port=5000, debug=True)

