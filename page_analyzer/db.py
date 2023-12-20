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


def get_urls(conn):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(
            'SELECT * FROM urls ORDER BY id DESC;'
        )
        return curs.fetchall()


def insert_url_check(conn, url_id, status_code):
    with conn.cursor() as curs:
        curs.execute(
            'INSERT INTO url_checks (url_id, status_code) VALUES (%s, %s);',
            (url_id, status_code)
        )


def get_checks_by_url_id(conn, url_id):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(
            'SELECT id, created_at FROM url_checks '
            'WHERE url_id = (%s) ORDER BY id DESC;',
            (url_id,)
        )
        return curs.fetchall()


def get_urls_with_last_check_date(conn):
    with conn.cursor(cursor_factory=NamedTupleCursor) as curs:
        curs.execute(
            'SELECT DISTINCT ON (u.id) '
            'u.id, u.name, uc.created_at AS last_check_date '
            'FROM urls u '
            'LEFT JOIN url_checks uc ON u.id = uc.url_id '
            'ORDER BY u.id DESC, uc.created_at DESC;'
        )
        return curs.fetchall()
