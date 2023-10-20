from flask import Flask, render_template, request, redirect, url_for, session, g
import sqlite3
import os
import uuid

app = Flask(__name__)
DATABASE = 'database.db'
app.config['SECRET_KEY'] = os.urandom(24)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        user = db.execute(f"SELECT * FROM User WHERE username = '{username}' AND password = '{password}'").fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('books'))
    return render_template('login.html')

@app.route('/books', methods=['GET', 'POST'])
def books():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    query = request.form.get('query', '')
    db = get_db()
    
    if query:
        books = db.execute(f"SELECT * FROM Book WHERE book_name LIKE '%{query}%'").fetchall()
    else:
        books = db.execute('SELECT * FROM Book').fetchall()
    
    return render_template('books.html', books=books, query=query)

@app.route('/user/<user_id>')
def user_profile(user_id):
    db = get_db()
    user = db.execute('SELECT * FROM User WHERE id = ?', (user_id,)).fetchone()
    if not user:
        return "User not found", 404
    if user[0] == "6837cbcc5":
        
        return f"User ID: {user[0]}<br>Username: {user[1]}<br>Description: {user[3]}<br>" + "FLAG{y0u_pwn3d_l1br4ry_xd}"
    return f"User ID: {user[0]}<br>Username: {user[1]}<br>Description: {user[3]}"

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
