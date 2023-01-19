from flask import Flask
from app.users.routes import user_api

def createApp():
    app = Flask(__name__)
    app.register_blueprint(user_api)
    return app