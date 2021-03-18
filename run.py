from flask import Flask, request, abort
from datetime import datetime
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/date')
def date():
    return datetime.today().strftime('%Y-%m-%d')

@app.route('/square')
def square():
    x = int(request.args.get('x'))
    return("{}".format(x*x))

@app.route('/divide')
def divide():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    if y == 0:
        abort(400)
    else:
        print(x/y)
        return("{}".format(x/y))

app.run(host='0.0.0.0', port = 8080, debug = True)

