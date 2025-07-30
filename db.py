import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="SistemaPets",
        user="postgres",
        password="suasenhasecreta.",
        host="localhost"
    )