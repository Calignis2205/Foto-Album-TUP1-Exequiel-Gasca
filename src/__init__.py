from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def crear_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    
    from .routes import photo_bp
    from .forms import form_bp
    app.register_blueprint(form_bp, url_prefix='/')
    app.register_blueprint(photo_bp, url_prefix='/')

    return app
