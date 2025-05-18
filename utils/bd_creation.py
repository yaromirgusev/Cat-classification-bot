import psycopg2
from config import ttoken
from config.breed_list import listt
import logging

def bd_creation():
    connection = None
    try:
        connection = psycopg2.connect(
            host = 'db',
            database = ttoken.db_name,
            user = ttoken.user,
            password =  ttoken.password)
        
        with connection.cursor() as cursor:
            cursor.execute('DROP TABLE IF EXISTS data;')
            connection.commit()

            cursor.execute('DROP TABLE IF EXISTS users;')
            connection.commit()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS data(
            id SERIAL PRIMARY KEY, 
            names VARCHAR(255) NOT NULL, 
            descs VARCHAR(255) NOT NULL
        );
            ''')
            connection.commit()

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            user_id BIGINT UNIQUE NOT NULL,
            username VARCHAR(255),
            first_name VARCHAR(255),
            last_name VARCHAR(255)
        );
                        ''')
            connection.commit() 

            cursor.execute('''
            CREATE TABLE IF NOT EXISTS user_cats (
            id SERIAL PRIMARY KEY,
            user_id BIGINT NOT NULL,
            breed_name VARCHAR(255) NOT NULL,
            breed_desc TEXT,
            UNIQUE(user_id, breed_name)
        );

                        ''')
            connection.commit() 

            insert_query = 'INSERT INTO data (id, names, descs) VALUES (%s, %s, %s);'
            cursor.executemany(insert_query, listt)
            connection.commit()

    except Exception as e:
        logging.exception("Error while processing photo or prediction")


    finally:
        if connection:
            connection.close()
            logging.info('Database connection closed')