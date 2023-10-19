from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/robots.txt')
def robots_txt():
    x_forwarded_for = request.headers.get('X-Forwarded-For')
    if not x_forwarded_for or x_forwarded_for.split(',')[0] != '127.0.0.1':
        abort(403)  # Forbidden
    with open("robots.txt", "r") as f:
        return f.read(), 200, {'Content-Type': 'text/plain'}

@app.route('/4qu1_3st4_l4_b4nd3r4')
def four_quarter():
    return "FLAG{byp4ss_403_c0d3_st4at3}"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
