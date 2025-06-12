import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="gestion_citas_db",
        user="postgres",  # tu usuario real
        password="rafael1517"  # tu contraseña real
    )
