import datetime

from flask import Blueprint, render_template, request, url_for, redirect, session, g, flash

from app import app

admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

from autosalon.bd_exe import connect_db, FDataBase


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


def login_admin():
    session['admin_logged'] = 1


def isLogged():
    return True if session.get('admin_logged') else False


def logout_admin():
    session.pop('admin_logged', None)


@admin.route('/adminprof/<username>', methods=["POST", "GET"])
def adminprof(username):
    return render_template('admin/adminprofil.html', title='Профиль')


@admin.route('/login', methods=['POST', 'GET'])
def login():
    db = get_db()
    db = FDataBase(db)
    if 'admin_logged' in session:
        return redirect(url_for('.adminprof', username=session['admin_logged']))
    elif request.method == 'POST':
        for item in db.getAdmin():
            if item['login'] == request.form['login'] and item['password'] == request.form['password']:
                session['admin_logged'] = request.form['login']
                username = session['admin_logged']
                print(username)
                return redirect(url_for('.adminprof', username=username))
        else:
            print('Ошибка')
    return render_template('admin/login.html', title='Для Администратора', data=db.getAdmin())


@admin.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_admin()

    return redirect(url_for('.login'))


@admin.route('/zakazi')
def zakazi():
    db = get_db()
    db = FDataBase(db)
    print(db.get_zakaz())
    return render_template('admin/zakazi.html', title='Заказы', vibrusl=db.get_zakaz())


@admin.route('/dobuser', methods=['POST', 'GET'])
def dobuser():
    db = get_db()
    db = FDataBase(db)
    if request.method == "POST":
        db.add_admin(request.form['login'], request.form['password'])
        flash('Пользователь добавлен', category='success')
    return render_template('admin/dobavitpolz.html', title='Добавление Пользователей')


@admin.route('/delusers')
def delusers():
    db = get_db()
    db = FDataBase(db)
    users = db.getUser()
    return render_template('admin/deleteprofil.html', title='Удалить пост', users=users)


@admin.route('/delusers/<num>')
def deluser(num):
    db = get_db()
    db = FDataBase(db)
    try:
        db.deuUserById(num)
        return redirect(url_for('.delusers'))
    except:
        return 'error'
