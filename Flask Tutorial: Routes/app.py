from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome"

@app.route('/hello')
def hello_world():
    return 'Hello World'

@app.route('/product/<name>')
def get_product(name):
    return 'product:' + str(name)

@app.route('/sale/<transection_id>')
def get_sale(transection_id = 0):
    return  'sales_id:' + str(transection_id)

@app.route('/dashboard/<name>')
def dashboard(name):
    return 'Welcome %s' % name

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('dashboard', name=user))
    else:
        user = request.args.get('name')
        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug = True)