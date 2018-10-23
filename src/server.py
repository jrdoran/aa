from flask import Flask

# the all-important app variable:
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World from Jim Doran 3"


@app.route('/jim')
def accounts():
    return "jjjiiimmmaa!"


@app.route('/login')
def login():
    return "bbbb"

if __name__ == "__main__":
	app.config['TEMPLATES_AUTO_RELOAD'] = True
	app.run(host='0.0.0.0', debug=True, port=8080)
