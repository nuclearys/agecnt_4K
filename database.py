import os
import psycopg2
from psycopg2 import sql
from dotenv import load_dotenv

load_dotenv()

# def get_connection():
#     """Возвращает соединение с базой данных."""
#     return psycopg2.connect(
#         dbname=os.getenv('DB_NAME'),
#         user=os.getenv('DB_USER'),
#         password=os.getenv('DB_PASSWORD'),
#         host=os.getenv('DB_HOST'),
#         port=os.getenv('DB_PORT')
#     )

def get_connection():
    return psycopg2.connect(
        dbname='agent_4K',
        user='postres',
        password='Dolwestern123',
        host='localhost',
        port='5432'
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(create_table_query)
        conn.commit()

def save_survey(first_name, last_name, position, responsibilities):
    """Сохраняет ответы пользователя в базу данных."""
    insert_query = """
    INSERT INTO survey (first_name, last_name, position, responsibilities)
    VALUES (%s, %s, %s, %s);
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(insert_query, (first_name, last_name, position, responsibilities))
        conn.commit()