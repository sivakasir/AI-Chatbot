1.🌞 Yoriichi Tsugikuni – Sun Breathing Chatbot

A stylish AI-powered chatbot inspired by Yoriichi Tsugikuni (Demon Slayer), built using Flask, Google Gemini API, and a custom animated frontend UI.
The chatbot responds in real time with graceful error handling, avatar-based chat messages, and a themed design.

2.✨ Features

🔥 Gemini AI (gemini-2.5-flash) integration
🧠 Real-time chatbot responses
🎭 Character-themed UI (Sun Breathing aesthetic)
🖼️ Background + avatar image support
⚠️ Graceful API quota error handling
🌐 Frontend–backend communication using Fetch API
🔐 CORS-enabled backend for browser access

3.📁 Project Structure

chatbot/
│
├── app.py                  # Flask backend (Gemini API logic)
│
├── templates/
│   └── index.html          # Frontend HTML (chat UI)
│
├── static/
│   └── yorichi.jpg         # Background + avatar image
│
├── requirements.txt        # Python dependencies
│
└── README.md               # Project documentation



4.requirements

flask
flask-cors
google-genai
pip install -r requirements.txt


🚀 How to Run the Project
1️⃣ Add your Gemini API Key

In app.py:

client = genai.Client(api_key="YOUR_API_KEY")

⚠️ Do not expose your API key in public repositories.

2️⃣ Start the Backend Server
python app.py

Server will run at:

http://127.0.0.1:5003/
3️⃣ Open the Web App

Open your browser and visit:

http://127.0.0.1:5003/

Start chatting with Yoriichi Tsugikuni ☀️🗡️
