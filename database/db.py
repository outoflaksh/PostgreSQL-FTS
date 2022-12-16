import psycopg2
from psycopg2 import DatabaseError

from config import db_config


def get_db_conn():
    """
    Connect to PostgreSQL database server
    """
    conn = None
    try:
        params = db_config()

        print("Connecting to the PostgreSQL server...")
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        print("PostgreSQL db version:")
        cursor.execute("SELECT version()")
        print(cursor.fetchone())

        cursor.close()
    except (Exception, DatabaseError) as err:
        print(err)

    return conn


def create_tables(conn=get_db_conn()):
    if not conn:
        return False

    query = """
    CREATE TABLE IF NOT EXISTS posts (
        post_id SERIAL PRIMARY KEY,
        post_title VARCHAR(255) NOT NULL,
        post_desc VARCHAR(255) NOT NULL 
    )
    """

    cursor = conn.cursor()

    cursor.execute(query)

    cursor.close()
    conn.commit()

    return True
