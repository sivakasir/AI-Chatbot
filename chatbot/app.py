# from flask import  Flask, request , render_template
# from google import genai

# client = genai.Client(api_key="AIzaSyDN981oex4PswEd2AN_hobpyQt-_tnlRfo")

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/chat", methods=["POST"])
# def chat():
#     return client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=request.json["msg"]
#     ).text

# app.run(port=5003)






from flask import Flask, request, render_template
from flask_cors import CORS
from google import genai
from google.genai.errors import ClientError

client = genai.Client(api_key="AIzaSyDN981oex4PswEd2AN_hobpyQt-_tnlRfo")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "msg" not in data:
        return "No message received.", 400

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=data["msg"]
        )
        return response.text

    except ClientError as e:
        # 🔥 Handle quota exceeded
        if "RESOURCE_EXHAUSTED" in str(e):
            return "☀️ The sun rests for now… API quota exceeded. Try again later.", 429
        return "An AI error occurred.", 500

    except Exception as e:
        print(e)
        return "Server error occurred.", 500


if __name__ == "__main__":
    app.run(port=5003, debug=True)