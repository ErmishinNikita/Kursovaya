import datetime

from autosalon import app
from flask import render_template, request, flash, get_flashed_messages, session, redirect, url_for, abort, g

from autosalon.admin.admin import admin
from autosalon.bd_exe import connect_db, FDataBase

menu = [{'name': 'Главная', 'url': '/index'}, {'name': 'Модельный ряд', 'url': '/model'},
        {'name': 'Контакты', 'url': '/contact'},
        {'name': 'Личный кабинет', 'url': '/kabinet'}]

app.register_blueprint(admin, url_prefix='/admin')


@app.route('/')
@app.route('/index')
def index():
    db = get_db()
    db = FDataBase(db)
    model = db.get_model2top3()
    return render_template('index.html', title='Главная', menu=menu, model=model)


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Контакты', menu=menu)


@app.route('/kabinet')
def kabinet():
    if 'userlogged' not in session:
        return redirect(url_for('login'))
    return render_template('profile.html', title='Личный кабинет', menu=menu)


@app.route('/register', methods=['POST', 'GET'])
def reg():
    db = get_db()
    db = FDataBase(db)
    if request.method == "POST":
        db.add_users(request.form['login'], request.form['password'])
        return redirect(url_for('login'))
    return render_template('registr.html', title='Регистрация', menu=menu)


@app.route('/login', methods=['POST', 'GET'])
def login():
    db = get_db()
    db = FDataBase(db)
    if 'userlogged' in session:
        return redirect(url_for('profile', username=session['userlogged']))
    elif request.method == 'POST':
        for item in db.getUser():
            if item['login'] == request.form['login'] and item['password'] == request.form['password']:
                session['userlogged'] = request.form['login']
                username = session['userlogged']
                print(username)
                return redirect(url_for('profile', username=request.form['login']))
                # return redirect(url_for('profile', username=username))
        else:
            print('Ошибка')
    return render_template('login.html', title='Авторизация', menu=menu, data=db.getUser())


@app.route('/profile/<username>', methods=["POST", "GET"])
def profile(username):
    db = get_db()
    db = FDataBase(db)
    if 'userlogged' not in session or session['userlogged'] != username:
        abort(401)
    if request.method == "POST":
        if len(request.form['fio']) > 2:
            flash('Заказ передан консультанту, с вами свяжутся в ближайшее время', category='success')
            db.add_auto(request.form['fio'], request.form['contact'], request.form['auto'])
        else:
            flash('Ошибка отправки', category='error')
    return render_template('profile.html', title='Профиль', menu=menu)


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route('/quit')
def quit():
    session.clear();
    db = get_db()
    db = FDataBase(db)
    model = db.get_model2top3()
    return render_template('index.html', title='Главная', menu=menu, model=model)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='Все сломалось', menu=menu)


@app.errorhandler(401)
def page_error_401(error):
    return render_template('401.html', title='Ошибка авторизации', menu=menu)


@app.route('/a')
def a():
    db = get_db()
    db = FDataBase(db)
    db.add_model('Lada Granta Фургон', '/static/img/promtovar.png', '1 400 000 ₽', '130 км\ч', '90 л.с', '15.0 c',
                 '9.5 л/км')


@app.route('/model')
def show_models():
    db = get_db()
    db = FDataBase(db)
    model = db.get_model2()
    return render_template('models.html', title='1234', menu=menu, model=model)


@app.route('/model_info/<id>')
def model_info(id):
    db = get_db()
    db = FDataBase(db)
    model = db.getModelById(id)
    print(model)
    return render_template('model_info.html', title='Профиль', menu=menu, model=model)
