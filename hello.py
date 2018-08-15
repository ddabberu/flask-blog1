##flask app

from flask import Flask, url_for
app = Flask(__name__)  #name of the app

## absolute urls
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/1')
def hello_world1():
    return 'Hello, World1!'

@app.route('/2')
def hello_world2():
    return 'Hello, World2!'

##adding meaningful routes and variables with flask
## sting
@app.route('/hello/<user>')
def hello_user(user):
    return 'Hello %s' %user

## int
@app.route('/hello/<user>/<int:id>')
def hello_user_id(user,id):
    retStr="Hello {} with Id:{}".format(user,id)
    return retStr

## path
@app.route('/hello/<path:subpath>')
def hello_user_path(subpath):
    return 'Hello %s' %subpath

##redirection add a slash at the end
@app.route('/projects/')
def projects():
    return 'The project page'

###Using url_function to build urls for a specific function

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('hello_user_id',user='dvd',id=1))
#url_for('static', filename='style.css')
#The file has to be stored on the filesystem as static/style.css.

##HTTP, import request, and use request.

