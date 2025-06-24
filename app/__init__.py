from flask import Flask
import psycopg2
from .config import db_config

def create_app():
    app = Flask(__name__)
    app.secret_key = 'clave_secreta_segura'

    try:
        connection = psycopg2.connect(**db_config)
        app.config['db_connection'] = connection
    except Exception:
        app.config['db_connection'] = None

    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp)
    from app.routes.dashboard_routes import dashboard_bp
    app.register_blueprint(dashboard_bp)


    return app

