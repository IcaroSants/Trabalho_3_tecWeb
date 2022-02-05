from flask import Flask, render_template, request, url_for, redirect,abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('log_in.html')


@app.route("/login", methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            return redirect(url_for('sucess'))
        else:
            abort(401)
        
    else:
        redirect(url_for('index'))

@app.route('/sucesss')
def sucess():
    return 'login sucessfully'

if __name__ == '__main__':
    app.run(debug=True)