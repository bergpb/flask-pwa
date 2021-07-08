from flask import Flask, render_template
from flask_pwa import PWA


app = Flask(__name__)
PWA(app)

@app.route("/")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	app.run()
