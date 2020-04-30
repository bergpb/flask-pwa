from flask import Flask, render_template
from flask_pwa import PWA


def create_app():
    app = Flask(__name__)
    PWA(app)

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
