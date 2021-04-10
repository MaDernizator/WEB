from flask import Flask, render_template
from flask import url_for
from data import db_session

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/create')
def create():
    # return render_template('create.html', temp=get_temp())
    return render_template('create.html')

@app.route('/authorization')
def authorization():
    return 'Страница авторизации'


@app.route('/registration')
def registration():
    return 'Страница регистрации'


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=8000, host='127.0.0.1')
