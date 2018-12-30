from flask import Flask
from flask.json import jsonify

# the all-important app variable:
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Jim Doran 3"

cache = {}

@app.route("/create")
def create():
    cache['foo'] = 0
    return jsonify(cache['foo'])

@app.route("/increment")
def increment():
    cache['foo'] = cache['foo'] + 1
    return jsonify(cache['foo'])

@app.route("/read")
def read():
    return jsonify(cache['read route - foo'])


@app.route('/jim')
def jim():
    return "this is jim Endpoint"


@app.route('/login')
def login():
    return "login bbbb"

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', debug=True, port=8080)




