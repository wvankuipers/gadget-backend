import sqlite3
import psycopg2

from src.config import config


class Database:
    def __init__(self):
        try:
            if config['App'].getboolean('DevMode') is True:
                print("Connecting to SQLite Database")
                self.conn = sqlite3.connect(config['Database.DEV']['Name'])
                self.cursor = self.conn.cursor()
            else:
                print("Connecting to Prostgres Database")
                self.conn = psycopg2.connect(
                    dbname=config['Database.PRD']['Name'],
                    user=config['Database.PRD']['User'],
                    password=config['Database.PRD']['Password'],
                    host=config['Database.PRD']['Host'],
                    port=config['Database.PRD']['Port']
                )
                self.cursor = self.conn.cursor()

        except sqlite3.Error as e:
            print("Error connecting to database!")

    def close(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def write(self, query):
        print("writing to DB")
        print(query)
        self.cursor.execute(query)
        self.conn.commit()

    def query(self, query):
        print(query)
        return self.conn.execute(query)
