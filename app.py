from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import google.generativeai as genai
import markdown

# config do .env
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)

generation_config = {
  "temperature": 0.8,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings, generation_config=generation_config)

@app.route("/", methods=["GET","POST"])
def makePrompt():
    try:
      if request.method == "POST":
          text = request.form["text"]
          
          response = model.generate_content(text)
          response.resolve()
          
          modelResponse = response.text
          modelResponse = markdown.markdown(modelResponse)

          return render_template(
              "chatTemplate.html",
              modelResponse = modelResponse,
              text = text
          )

      else:
        return render_template(
              'chatTemplate.html',
              modelResponse = None
          )
      
    except Exception as e:
        return render_template(
            "error.html",
            error = e
        )
    
