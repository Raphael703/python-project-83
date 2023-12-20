import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash

from page_analyzer import db
from page_analyzer.site_checker import get_status_code
from page_analyzer.utils import validate_url, normalize_url

app = Flask(__name__)

load_dotenv()

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')


@app.route('/')
def index():
    return render_template('index.html')


@app.post('/urls')
def add_url():
    url = request.form['url']
    error_msg = validate_url(url)
    if error_msg:
        flash(error_msg, 'danger')
        return render_template('index.html', url=url)

    conn = db.connect_db(app)
    normalized_url = normalize_url(url)
    existed_url = db.get_url_by_name(conn, normalized_url)

    if existed_url:
        flash('Данный URL уже существует', 'info')
        url_id = existed_url.id
    else:
        url_id = db.insert_url(conn, normalized_url)
        db.commit(conn)
        flash('URL успешно добавлен', 'success')

    db.close(conn)
    return redirect(url_for('show_url_page', url_id=url_id))


@app.route('/urls/<int:url_id>')
def show_url_page(url_id):
    conn = db.connect_db(app)
    url = db.get_url(conn, url_id)
    url_checks = db.get_checks_by_url_id(conn, url_id)
    db.close(conn)
    return render_template('urls/url.html', url=url, url_checks=url_checks)


@app.get('/urls')
def show_urls_page():
    conn = db.connect_db(app)
    urls_data = db.get_urls_with_last_check_date_and_status_code(conn)
    db.close(conn)
    return render_template('urls/urls.html', urls_data=urls_data)


@app.route('/urls/<int:url_id>/checks', methods=['POST'])
def add_url_check(url_id):
    conn = db.connect_db(app)
    url = db.get_url(conn, url_id)
    status_code = get_status_code(url.name)
    if status_code is None:
        flash('Произошла ошибка при проверке', 'danger')
        return redirect(url_for('show_url_page', url_id=url_id))

    db.insert_url_check(conn, url_id, status_code)
    db.commit(conn)
    db.close(conn)

    return redirect(url_for('show_url_page', url_id=url_id))


if __name__ == '__main__':
    app.run(debug=True)
