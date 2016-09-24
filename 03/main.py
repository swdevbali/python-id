import os
import flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


class Buku(db.Model):
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    def __init__(self, title, author, qty=0):
        self.title = title
        self.author = author
        self.qty= qty


@app.route('/')
def root():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0.', debug=True)