from flask import Flask, render_template
from data import db_session
from frame.bd_func import get_subjects, get_types, get_patterns
from flask import request
from frame.frame import DocGenerator
from frame.frame import TaskGenerator
import requests

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html', subjects=get_subjects() + [[0, 'Все']],
                               types=get_types() + [[0, 'Все']], patterns=get_patterns())

    elif request.method == 'POST':

        doc_generator = DocGenerator(request.form)
        name = doc_generator.generate_document()

        return render_template('downolad.html', name=name)


@app.route('/authorization')
def authorization():
    return 'Страница авторизации'


@app.route('/registration')
def registration():
    return 'Страница регистрации'


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    app.run(port=5000, host='127.0.0.1')
