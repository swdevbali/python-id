import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def root():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0.', debug=True)