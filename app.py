from flask import Flask,render_template,g, request
import sqlite3

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    db = getattr(g, '_database', None)
    if db == None:
        db = sqlite3.connect(DATABASE)
    return db

def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS database(
                            id INTEGER PRIMARY KEY,
                            title TEXT NOT NULL,
                            content TEXT NOT NULL,
                            date TEXT NOT NULL
                           )''')
        db.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/database', methods=['GET'])
def database_entries():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM database")
    entries = cursor.fetchall
    return render_template('database_entries.html', entries=entries)



if __name__ == '__main__':
    init_db()
    app.run(debug=True)