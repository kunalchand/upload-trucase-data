from calendar import c
import os
from dotenv import load_dotenv
import psycopg2

load_dotenv(override=True)


class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=os.getenv("PG_HOST"),
                port=os.getenv("PG_PORT"),
                user=os.getenv("PG_USERNAME"),
                password=os.getenv("PG_PASSWORD"),
                dbname=os.getenv("PG_DATABASE"),
                sslmode="require",
            )
            print("Connected to the database successfully!")
            return self.connection
        except Exception as e:
            print(f"Error connecting to the database: {e}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
