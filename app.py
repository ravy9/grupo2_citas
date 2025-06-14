from flask import Flask
from modelo.conexion import get_connection

app = Flask(__name__)

@app.route('/')
def home():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        version = cursor.fetchone()
        cursor.close()
        conn.close()
        return f'¡Conexión exitosa a PostgreSQL!<br>Versión: {version[0]}'
    except Exception as e:
        return f'Error de conexión: {e}'

if __name__ == '__main__':
    app.run(debug=True)
