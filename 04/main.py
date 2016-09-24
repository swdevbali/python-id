import os
import flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin


app = flask.Flask(__name__)
app.secret_key = "a@3$DM.<^"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')


class Buku(db.Model):
    __tablename__ = 'buku'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    qty = db.Column(db.Integer, nullable=False)

    def __init__(self, title='', author='', qty=0):
        self.title = title
        self.author = author
        self.qty= qty


class MicroBlogModelView(ModelView):
    def is_accessible(self):
        return True

admin = Admin(app, name='Buku', template_mode='bootstrap3')
admin.add_view(MicroBlogModelView(Buku, db.session))

@app.route('/')
def root():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0.', debug=True)