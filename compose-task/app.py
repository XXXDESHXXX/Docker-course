# app.py

from flask import Flask

import psycopg2

app = Flask(__name__)

@app.route("/")

def home():

    try:

        conn = psycopg2.connect(

            dbname="mydb",  # Замените на имя БД из docker-compose.yml

            user="db_admin",          # Замените на пользователя из docker-compose.yml

            password="112233",  # Замените на пароль из docker-compose.yml

            host="database"             # Замените на имя сервиса базы данных из docker-compose.yml

        )

        conn.close()

        return "Connected to the database successfully!"

    except Exception as e:

        return f"Error: {e}"

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
