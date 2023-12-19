import os

from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for, flash

from page_analyzer import db

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

    if url:
        conn = db.connect_db(app)
        db.insert_url(conn, url)
        db.commit(conn)
        db.close(conn)
        return redirect(url_for('index'))
    else:
        return render_template('index.html', error='URL не был предоставлен')


if __name__ == '__main__':
    app.run(debug=True)
