
from flask import Flask
import psycopg2
from .config import db_config

def create_app():
    app = Flask(__name__)
    app.secret_key = 'clave_secreta_segura'

    # Conexión a base de datos PostgreSQL
    try:
        connection = psycopg2.connect(**db_config)
        print("✅ Conectado a la base de datos PostgreSQL")
        app.config['db_connection'] = connection
    except Exception as e:
        print("❌ Error al conectar con PostgreSQL:", e)

    return app
