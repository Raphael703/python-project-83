import psycopg2
from psycopg2.extras import NamedTupleCursor


def connect_db(app):
    return psycopg2.connect(app.config['DATABASE_URL'])


def commit(conn):
    conn.commit()


def close(conn):
    conn.close()


def insert_url(conn, url):
    with conn.cursor() as curs:
        curs.execute(
            'INSERT INTO urls (name) VALUES (%s);',
            (url,)
        )


def get_url(conn, url_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(
            'SELECT * FROM urls WHERE id = (%s);',
            (url_id,)
        )
        return curs.fetchone()
