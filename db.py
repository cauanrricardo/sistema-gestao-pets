import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="SistemaPets",
        user="postgres",
        password="224508rS.",
        host="localhost"
    )