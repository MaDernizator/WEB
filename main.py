from flask import Flask, render_template
from flask import url_for


app = Flask(__name__)


@app.route('/')
def main():
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
    app.run(port=8000, host='127.0.0.1')
