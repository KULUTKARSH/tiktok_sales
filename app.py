from flask import Flask, request, jsonify, render_template
from openai import AzureOpenAI
import pandas as pd
import azure.cognitiveservices.speech as speechsdk
from todoist_api_python.api import TodoistAPI

app = Flask(__name__)

# Initialize OpenAI configuration
openai_config = AzureOpenAI(
    azure_endpoint="AZURE ENDPOINT",
    api_key="API KEY",
    api_version="2024-02-15-preview"
)

system_message = "You are a helpful assistant for sales support."

# Define model functions
def generate_response(prompt):
    response = openai_config.chat.completions.create(
        model="haha",
        temperature=0.7,
        max_tokens=400,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]
    )
    generated_text = response.choices[0].message.content
    return generated_text

def check_safeguard(text, avoid_phrases):
    warnings = [f"Warning: Avoid using the phrase '{phrase}'" for phrase in avoid_phrases if phrase in text]
    if not warnings:
        warnings.append("No warnings detected.")
    return text, warnings

def summarize_text(text):
    response = openai_config.chat.completions.create(
        model="haha",
        temperature=0.7,
        max_tokens=150,
        messages=[
            {"role": "system", "content": "Summarize the following conversation."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

def extract_todos(text):
    response = openai_config.chat.completions.create(
        model="haha",
        temperature=0.7,
        max_tokens=100,
        messages=[
            {"role": "system", "content": "Extract to-do items from the following conversation."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_sales_tips(topic):
    response = openai_config.chat.completions.create(
        model="haha",
        temperature=0.7,
        max_tokens=150,
        messages=[
            {"role": "system", "content": f"Provide sales tips for {topic}."}
        ]
    )
    return response.choices[0].message.content.strip()

def generate_bi_report(data):
    df = pd.DataFrame(data)
    summary_stats = df.describe().to_json()
    # Add more detailed analysis as needed
    return summary_stats

def recognize_from_microphone():
    speech_config = speechsdk.SpeechConfig(subscription="", region="")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(result.text))
        return result.text
    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized")
        return "No speech could be recognized"
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
        return "Speech Recognition canceled"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def handle_generate_response():
    prompt = request.json.get('prompt')
    response = generate_response(prompt)
    return jsonify(response=response)

@app.route('/check_safeguard', methods=['POST'])
def handle_check_safeguard():
    text = request.json.get('text')
    avoid_phrases = request.json.get('avoid_phrases')
    safe_text, warnings = check_safeguard(text, avoid_phrases)
    return jsonify(safe_text=safe_text, warnings=warnings)

@app.route('/summarize_text', methods=['POST'])
def handle_summarize_text():
    text = request.json.get('text')
    summary = summarize_text(text)
    return jsonify(summary=summary)

@app.route('/extract_todos', methods=['POST'])
def handle_extract_todos():
    text = request.json.get('text')
    todos = extract_todos(text)
    return jsonify(todos=todos)

@app.route('/generate_sales_tips', methods=['POST'])
def handle_generate_sales_tips():
    topic = request.json.get('topic')
    sales_tips = generate_sales_tips(topic)
    return jsonify(sales_tips=sales_tips)

@app.route('/generate_bi_report', methods=['POST'])
def handle_generate_bi_report():
    data = request.json.get('data')
    bi_report = generate_bi_report(data)
    return jsonify(bi_report=bi_report)

@app.route('/recognize_from_microphone', methods=['GET'])
def handle_recognize_from_microphone():
    recognized_text = recognize_from_microphone()
    return jsonify(recognized_text=recognized_text)

@app.route('/add_todos_to_todoist', methods=['POST'])
def add_todos_to_todoist():
    todos = request.json.get('todos')
    api_token = request.json.get('api_token')
    api = TodoistAPI(api_token)
    for todo in todos:
        api.add_task(content=todo)
    return jsonify(message="Todos added to Todoist successfully")

if __name__ == '__main__':
    app.run(debug=True)
