 Yoriichi AI: Breath of the Sun Chatbot

An immersive AI-powered chatbot interface themed after the legendary first Demon Slayer, Yoriichi Tsugikuni. This project combines a Python Flask backend with the Google Gemini API to provide a wise, stoic, and character-driven conversational experience.

✨ Features

Character Accuracy: System-prompted AI that speaks with the humility and wisdom of Yoriichi.

Sun Breathing UI: A "Glassmorphism" design with deep crimson and gold accents.

Form Buttons: Interactive buttons to quickly trigger Sun Breathing technique dialogues.

Error Handling: Graceful handling of API quotas (Resource Exhausted) with thematic messages.

Responsive Design: Large, expanded interface optimized for both desktop and mobile viewing.

📁 Project Structure

yoriichi-ai/
├── app.py                 # Flask server & Gemini API logic
├── templates/             # HTML files
│   └── index.html         # Main chatbot interface
├── static/                # CSS, JS, and Media
│   ├── yorichi.jpg        # Background & Avatar image
│   └── style.css          # (Optional) External CSS
└── README.md              # Documentation


🚀 Setup Instructions

1. Prerequisites

Python 3.9+

A Google Gemini API Key

2. Installation

Clone the project or create the directory structure as shown above, then install the dependencies:

pip install flask flask-cors google-genai


3. API Configuration

Open app.py and replace "API-KEY" with your actual Google AI Studio API key.

4. Running the App

Navigate to the project folder and run:

python app.py


The application will start on http://127.0.0.1:5003.

🛠️ Technology Stack

Backend: Python Flask

Frontend: HTML5, Tailwind CSS, JavaScript (Vanilla)

AI Model: Google Gemini 2.5 Flash

Styling: Google Fonts (Cinzel, Noto Sans JP)

📜 License

This project is for fan/educational purposes. Characters and imagery belong to Koyoharu Gotouge / Shueisha / Aniplex / ufotable.
