# Mental Health App AI Chatbot

This is a locally hosted AI chatbot built using Flask and SQLite. The chatbot utilizes **Ollama LLaMA 3.2 3B** model running on a local machine. The application provides a user authentication system, stores chat history, and allows users to log in to view past conversations.

## Features
- **User Authentication**: Users must sign up or log in before accessing the chatbot.
- **Chat Storage**: Stores conversations in `chat_logs.db` associated with each user.
- **Chat History Sidebar**: Displays previous chats for logged-in users.
- **Locally Hosted AI**: Uses **Ollama LLaMA 3 3B** to generate responses.
- **Logout Option**: Users can log out to end their session.

## Installation & Setup

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Flask (`pip install flask`)
- SQLite (included with Python)
- Ollama (`ollama` must be installed and running locally)
- LLaMA 3 3B model downloaded (`ollama pull llama3:3b`)

### Steps to Run
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd ai-chatbot
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Start the Ollama LLaMA 3B model:
   ```bash
   ollama run llama3:3b
   ```
4. Run the Flask application:
   ```bash
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## File Structure
- `app.py` - Main Flask backend handling user authentication, chat history, and AI response generation.
- `chat_logs.db` - SQLite database storing user credentials and chat history.
- `templates/`
  - `index.html` - Chatbot UI with chat history.
  - `login.html` - Login page.
  - `user.html` - Signup page.
- `static/` - Contains CSS/JS files if needed.

## How It Works
- When a user accesses the chatbot, they are prompted to **Sign Up** or **Login**.
- After logging in, their **previous chats are loaded from SQLite**.
- New chat messages are **sent to the Ollama LLaMA 3B model** for response generation.
- Conversations are stored and can be accessed later.

## Notes
- The chatbot runs **entirely locally**; no external API calls are required.
- Ensure **Ollama is running** before starting the Flask app.
- The SQLite database is lightweight and stores user authentication and chat data.

## Future Improvements
- Add support for multiple AI models.
- Improve UI/UX with a more dynamic frontend.
- Implement a feedback mechanism for AI responses.

---
This chatbot is a great example of running **AI models locally** for personal or enterprise use without cloud dependency.


Group: Penguin
Rishabh, Pratosh, Harshal, Praneeth
for query mail : 2022A3PS0485H
