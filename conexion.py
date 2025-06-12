import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="gestion_citas_db",
        user="postgres",
        password="rafael1517"
    )
