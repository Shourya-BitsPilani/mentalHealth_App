from flask import Flask, render_template, request, jsonify, redirect, url_for
import sqlite3
from datetime import datetime
from local_llm import LocalLLM
import os

app = Flask(__name__)

# Set Ollama host environment variable
os.environ['OLLAMA_HOST'] = 'http://localhost:11434'

# Initialize LocalLLM with error handling
try:
    llm = LocalLLM()
except Exception as e:
    print(f"Error initializing LocalLLM: {str(e)}")
    llm = None

# Initialize chat history
chat_history = []

def store_chat_log(user_message, ai_response):
    conn = sqlite3.connect('chat_logs.db')
    c = conn.cursor()
    
    # Ensure table structure
    c.execute("""
        CREATE TABLE IF NOT EXISTS chat_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            user_message TEXT,
            ai_response TEXT
        )
    """)
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO chat_logs (timestamp, user_message, ai_response) VALUES (?, ?, ?)",
              (timestamp, user_message, ai_response))
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/user')
def user():
    return render_template('user.html')

@app.route('/option')
def option():
    return render_template('option.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/redirect_to_user', methods=['POST'])
def redirect_to_user():
    return render_template('user')

@app.route('/redirect_to_option', methods=['POST'])
def redirect_to_option():
    return redirect(url_for('option'))

@app.route('/redirect_to_index', methods=['POST'])
def redirect_to_index():
    return redirect(url_for('home'))

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    if llm is None:
        return jsonify({'response': 'Sorry, the AI model is currently unavailable. Please try again later.'})
    
    try:
        ai_response = llm.chat(user_message)
        store_chat_log(user_message, ai_response)
        return jsonify({'response': ai_response})
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return jsonify({'response': 'Sorry, there was an error processing your request. Please try again.'})

@app.route('/reset', methods=['POST'])
def reset():
    global chat_history
    chat_history = []
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
