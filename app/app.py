from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flask behind Nginx. Cloud Project by OBED - Reverse Proxy Working!"

@app.route("/api")
def api():
    return {"message": "This is a backend API by OBED"}

@app.route("/health")
def health():
    return {"status": "ok"}
