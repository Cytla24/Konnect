import flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///konnect.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')
    rating = db.Column(db.Float, nullable=True)
    address = db.Column(db.Text, nullable=False)
    tags = db.Column(db.Text, nullable=False)
    keywords = db.Column(db.Text, nullable=False)

    tweets = db.relationship('Tweet', backref='biz', lazy=True)

    def __repr__(self):
        return f"Business('{self.name}', '{self.address}', '{self.tags}')"


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=False, default=0.0)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)

    def __repr__(self):
        return f"Tweet('{self.id}', '{self.content}')"


