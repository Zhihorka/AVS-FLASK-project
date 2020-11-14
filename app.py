import flask
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from models.Interval import Interval
from models.Group import Group
from models.Schedule import Schedule
from models.Lecturer import Lecturer
from models.Subject import Subject
from flask import request

from Routes.Lecturers import lecturers
from Routes.Intervals import intervals
from Routes.Subjects import subjects
from Routes.Schedule import schedule
from Routes.AddToSchedule import addToSchedule

app = Flask(__name__)

app.config["Debug"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.register_blueprint(lecturers)
app.register_blueprint(intervals)
app.register_blueprint(subjects)
app.register_blueprint(schedule)
app.register_blueprint(addToSchedule)

if __name__ == '__main__':
    app.run(debug=True)


