import psycopg2


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
