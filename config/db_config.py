import os
from dotenv import load_dotenv
import psycopg2


class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        self.connection = None

    def connect(self):
        print("PG_HOST =", os.getenv("PG_HOST"))
        print("PG_PORT =", os.getenv("PG_PORT"))
        print("PG_USERNAME =", os.getenv("PG_USERNAME"))
        print("PG_PASSWORD =", os.getenv("PG_PASSWORD"))
        print("PG_DATABASE =", os.getenv("PG_DATABASE"))
        self.connection = psycopg2.connect(
            host=os.getenv("PG_HOST"),
            port=os.getenv("PG_PORT"),
            user=os.getenv("PG_USERNAME"),
            password=os.getenv("PG_PASSWORD"),
            dbname=os.getenv("PG_DATABASE"),
            sslmode="require",
        )
        return self.connection

    def close(self):
        if self.connection:
            self.connection.close()
