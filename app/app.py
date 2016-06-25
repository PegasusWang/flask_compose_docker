#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from redis import Redis
from model import db, User, CreateDB
from model import app as application
import simplejson as json
from sqlalchemy.exc import IntegrityError

r = Redis(host='redis', port=6379)
app = Flask(__name__)

m = MongoClient('mongo', 27017)
mongodb = m.tododb


@app.route('/')
def todo():
    _items = mongodb.tododb.find()
    items = [item for item in _items]
    return render_template('todo.html', items=items)


@app.route('/hehe')
def hehe():
    import time
    return 'hehe' + '<br>' + str(time.time())


@app.route('/new', methods=['POST'])
def new():
    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    mongodb.tododb.insert_one(item_doc)
    return redirect(url_for('todo'))


@app.route('/redis')
def hello():
    r.incr('hits')
    return 'I have been seen %s times' % r.get('hits')


@app.route('/user')
def show_user():
    # return json.dumps({'username':request.args['username']})
    try:
        user = User.query.filter_by(
            username=request.args['username']
        ).first_or_404()
        return json.dumps({
            user.username: {'email': user.email,
                            'phone': user.phone,
                            'fax':user.fax}}
        )
    except IntegrityError:
        return json.dumps({})


@app.route('/insert')
def insert_user():
    try:
        user = User(request.args['username'],
                request.args['email'],
                request.args['phone'],
                request.args['fax'])
        db.session.add(user)
        db.session.commit()
        return json.dumps({'status':True})
    except IntegrityError:
        return json.dumps({'status':False})

@app.route('/createtbl')
def createUserTable():
    try:
        db.create_all()
        return json.dumps({'status':True})
    except IntegrityError:
        return json.dumps({'status':False})

@app.route('/users')
def users():
    try:
        users = User.query.all()
        users_dict = {}
        for user in users:
            users_dict[user.username] = {
                            'email': user.email,
                            'phone': user.phone,
                            'fax': user.fax
                            }

        return json.dumps(users_dict)
    except IntegrityError:
        return json.dumps({})


@app.route('/createdb')
def createDatabase():
    HOSTNAME = 'localhost'
    try:
        HOSTNAME = request.args['hostname']
    except:
        pass
    database = CreateDB(hostname = HOSTNAME)
    return json.dumps({'status':True})


@app.route('/info')
def app_status():
    return json.dumps({'server_info':application.config['SQLALCHEMY_DATABASE_URI']})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
