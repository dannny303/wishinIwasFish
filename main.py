from flask import Flask, render_template, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy
from hashutils import make_pw_hash, check_pw_hash

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://wishinIwasFish:fishfishfish@localhost:8889/wishinIwasFish'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'ZmHKz'

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), unique = True)
    pw_hash = db.Column(db.String(120))
    report = db.relationship('Report', backref = 'owner')

    def __init__(self, username, password):
        self.username = username
        self.pw_hash = make_pw_hash(password)


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date = db.Column (db.DateTime)
    location = db.Column(db.String(120))
    companions = db.Column(db.String(120))
    weatherCond = db.Column(db.String(120))
    weatherTemp = db.Column(db.Integer)
    cfs = db.Column(db.Integer)
    waterCond = db.Column(db.String(120))
    waterTemp = db.Column(db.Integer)
    bugs = db.Column(db.String(120))
    description = db.Column(db.Text(500))

    def __init__(self, owner, date, location, companions, weatherCond, weatherTemp, cfs, waterTemp, waterCond, bugs, description):
        self.owner = owner
        self.date = date
        self.location = location
        self.companions = companions
        self.weatherCond = weatherCond
        self.weatherTemp = weatherTemp
        self.cfs = cfs
        self.waterCond = waterCond
        self.waterTemp = waterTemp
        self.bugs = bugs
        self.description = description

class Fish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    species = db.Column(db.String(120))
    length = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    time = db.Column(db.String(120))
    location = db.Column(db.String(120))
    pattern = db.Column(db.String(120))

    def __init__(self, owner, species, length, weight, time, location, pattern):
        self.owner = owner
        self.species = species
        self.length = length
        self.weight = weight
        self.time = time
        self.location = location
        self.pattern = pattern