from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Allen/Documents/workSpace/PythonPack/RESTfulAPI/monitorDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Pattern(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    devicetype = db.Column(db.String(10), unique = True)
    inputvalue = db.Column(db.String(500))
    scenetype = db.Column(db.String(10))

    def __init__(self,devicetype,inputvalue,scenetype):
        self.devicetype = devicetype
        self.inputvalue = inputvalue
        self.scenetype = scenetype

    def __repr__(self,devicetype,inputvalue,scenetype):
        return '&lt;DeviceType %r>' % self.devicetype