import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


def get_connection():
    connection = psycopg2.connect(
        host=os.getenv("localhost"),
        port=os.getenv("5433"),
        database=os.getenv("expansion_gis"),
        user=os.getenv("postgres"),
        password=os.getenv("Larome02")
    )

    return connection
