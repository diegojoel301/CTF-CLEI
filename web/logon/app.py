from flask import Flask, render_template, request, redirect, url_for, flash, g, session
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
import hashlib

app = Flask(__name__)
app.config['DATABASE'] = 'users.db'
app.secret_key = 'some_secret_key'

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    return g.db

def hash_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        query = f"SELECT * FROM users WHERE username = '{username}' and password = '{hash_md5(password)}'"
        ans = db.execute(query).fetchall()
        
        if ans != list():
            ans = ans[len(ans) - 1]
            session['user_id'] = ans['id']
            if ans['username'] == "isabel":
                return "FLAG{sql1_byp44ss_1s_izi}"

            return redirect(url_for('dashboard'))
        flash('Invalid credentials.')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    users = get_db().execute('SELECT * FROM users').fetchall()
    return render_template('dashboard.html', users=users)

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    users = get_db().execute('SELECT * FROM users WHERE username LIKE ?', ('%' + query + '%',)).fetchall()
    return render_template('dashboard.html', users=users)

@app.teardown_appcontext
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
