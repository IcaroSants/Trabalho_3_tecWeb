from flask  import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route("/index")

def index():
    name = 'Rosalia'
    return render_template('index.html', title='Welcome', username=name)

@app.route('/index_2')
def if_html():
    name = 'Monica'
    return render_template('index_2.html', title='Welcome', username = name)


@app.route("/loop")
def loop():
    users = ['Rosangela','Monica', 'Maria']
    return render_template('loop.html', title='Welcome', members = users)

if __name__ == '__main__':
    app.run() 