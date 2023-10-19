from flask import Flask, render_template, request, redirect, session, url_for, g
import sqlite3
import hashlib

app = Flask(__name__)
app.secret_key = "supersecretkey"  # This should be a random string in production

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

@app.before_request
def before_request():
    g.db = sqlite3.connect("database.db")

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    cursor = g.db.execute("SELECT title, content, username FROM posts JOIN users ON posts.user_id = users.id WHERE user_id=?", (user_id,))
    posts = cursor.fetchall()
    return render_template('index.html', posts=posts)

@app.route('/myposts')
def my_posts():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    cursor = g.db.execute("SELECT title, content FROM posts WHERE user_id=?", (user_id,))
    posts = cursor.fetchall()
    return render_template('my_posts.html', posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = hash_password(request.form['password'])
        cursor = g.db.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('index'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))

@app.route('/new_post', methods=['GET', 'POST'])
def new_post():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        g.db.execute("INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)", (title, content, session['user_id']))
        g.db.commit()
        return redirect(url_for('index'))

    return render_template('new_post.html')

@app.route('/users', methods=['GET'])
def list_users():
    cursor = g.db.execute("SELECT id, username FROM users")
    users = cursor.fetchall()

    return render_template('users.html', users=users)


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
