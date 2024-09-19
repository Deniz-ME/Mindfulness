from flask import Flask,g
import sqlite3

app = Flask(__name__)
DATABASE = 'diary.db'

def get_db():
    db = getattr(g, '_database', None)
    if db == None:
        db = sqlite3.connect(DATABASE)
    return db

