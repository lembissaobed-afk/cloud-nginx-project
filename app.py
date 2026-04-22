from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "Hello depuis Flask derriere Nginx. Cloud Project by OBED - Nginx Reverse Proxy Working!"

@app.route("/api")
def api():
	return {"message": "Ceci est une API backend par OBED"}

if __name__== "__main__":
	app.run(host="127.0.0.1", port=5000)
