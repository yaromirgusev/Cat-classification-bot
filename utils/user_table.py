import psycopg2
from config import ttoken
import logging

def log_user_if_new(user):
    try:
        connection = psycopg2.connect(
            host=ttoken.host,
            database=ttoken.db_name,
            user=ttoken.user,
            password=ttoken.password
        )

        with connection.cursor() as cursor:
            insert_query = '''
                INSERT INTO users (user_id, username, first_name, last_name)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (user_id) DO NOTHING;
            '''
            cursor.execute(insert_query, (
                user.id,
                user.username,
                user.first_name,
                user.last_name
            ))
            connection.commit()

            if cursor.rowcount == 1:
                logging.info(f"[new user] @{user.username} - {user.first_name}")
            else:
                logging.info(f"[existing user] @{user.username} - {user.first_name}")
    except Exception as e:
        logging.error("DB Error: %s", e)
    finally:
        if connection:
            connection.close()

def save_user_breed(user_id, breed_name, breed_desc):
    try:
        connection = psycopg2.connect(
            host=ttoken.host,
            database=ttoken.db_name,
            user=ttoken.user,
            password=ttoken.password
        )
        with connection.cursor() as cursor:
            insert_query = '''
                INSERT INTO user_cats (user_id, breed_name, breed_desc)
                VALUES (%s, %s, %s)
                ON CONFLICT (user_id, breed_name) DO NOTHING;
            '''
            cursor.execute(insert_query, (user_id, breed_name, breed_desc))
            connection.commit()
    except Exception as e:
        logging.error("Error saving breed:", e)
    finally:
        if connection:
            connection.close()

