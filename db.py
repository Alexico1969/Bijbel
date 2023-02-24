import sqlite3, os
from flask import g
from urllib import parse

def connect_db():
    return sqlite3.connect('static/files/bible.db')

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

def init_db(app):
    with app.app_context():
        db = get_db()
        with app.open_resource('static/files/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()