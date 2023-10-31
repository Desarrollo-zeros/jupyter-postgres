import psycopg2
import netifaces as ni
from crud_operations import *


def connect_to_database():
    try:
        conn = psycopg2.connect(
            host="postgres",  # ipv4 colocar la suyas
            database="imdb",
            user="root",
            password="toor"
        )
        return conn
    except psycopg2.Error as e:
        print("Error al conectar a la base de datos:", e)
        return None


def close_connection(conn):
    if conn:
        conn.close()

