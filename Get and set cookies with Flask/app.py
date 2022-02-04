from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setCookie():
    

    user = request.form['nm']

    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('userID', user)

    return resp

@app.route('/getcookie')
def getCookie():
    name = request.cookies.get('userID')
    return '<h1>Welcome'+str(name)+'</h1>'

if __name__=='__main__':
    app.run(debug=True)
