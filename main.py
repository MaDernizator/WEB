from flask import Flask, render_template, send_from_directory
from data import db_session
from frame.bd_func import get_subjects, get_types, get_patterns
from flask import request
from frame.frame import DocGenerator
from data.user import User
from flask import redirect
from flask_login import LoginManager
from registrarion_form import RegisterForm
from login_form import LoginForm
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user
from flask_login import current_user
from threading import Thread
from clearing import clearing
from data_func import get_docs
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mad'
login_manager = LoginManager()
login_manager.init_app(app)

clearing_thread = Thread(target=clearing)
clearing_thread.start()


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/viewing')
def viewing():
    docs = get_docs(current_user.name if current_user.is_authenticated else 'anonym')
    return render_template('viewing.html', docs=docs)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', form=form)


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html', subjects=get_subjects() + [[0, 'Все']],
                               types=get_types() + [[0, 'Все']], patterns=get_patterns())

    elif request.method == 'POST':
        try:
            if current_user.is_authenticated:
                doc_generator = DocGenerator(request.form, user=current_user.name)
            else:
                doc_generator = DocGenerator(request.form)
        except ValueError:
            return render_template('error.html')
        name = doc_generator.generate_document()
        name += '.zip'
        return send_from_directory(
            directory=f'static/generated_documents/{current_user.name if current_user.is_authenticated else "anonym"}',
            filename=name, as_attachment=True)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            is_admin=False
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        f = open('log/log.txt', 'a')
        data = time.ctime(time.time())
        f.write(f'register {data} | {user.name}\n')
        f.close()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)

if __name__ == '__main__':
    db_session.global_init("db/blogs.db")
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
