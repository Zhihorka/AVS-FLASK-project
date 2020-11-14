from flask.blueprints import Blueprint
from flask import render_template
from flask import request
from models.Group import Group
from models.Interval import Interval
from models.Subject import Subject
from models.Lecturer import Lecturer
from manager.Database_Managers import DatabaseManager
from appClone import db

db_manager = DatabaseManager(db)

addToSchedule = Blueprint('addToSched', __name__, template_folder='templates', static_folder='static')

@addToSchedule.route('/addToSchedule')
def index():
    return render_template('AddToSchedule.html',group = Group.query.all(),interval = Interval.query.all(),subject = Subject.query.all(),lecturer = Lecturer.query.all())


@addToSchedule.route('/addToSchedule',methods=['post', 'get'])
def addNew():
    message = ''
    if request.method == 'POST':
        group = request.form.get('group')
        day = request.form.get('day')
        chet = request.form.get('chat')
        time = request.form.get('time')
        subject = request.form.get('subject')
        lecturer = request.form.get('lecturer')

    if group and day and chet and time and subject and lecturer:
        message = "EVERYTHING IS OK"
        new_dict = {"group":group,"day": day,"chet":chet, "time":time,"subject":subject,"lecturer":lecturer}
        new_dict = {}
        new_dict["group"] = group
        new_dict["day"] = day
        new_dict["chet"] = chet
        new_dict["time"] = time
        new_dict["subject"] = subject
        new_dict["lecturer"] = lecturer
        db_manager.add_item_to_Schedule(group, day, chet, time, subject, lecturer)

    else:
        print("NOT OK - BAD DATA")
        message = "NOT OK - BAD DATA"

    return render_template('AddToSchedule.html', message=message, prob=" ", group = Group.query.all(),interval = Interval.query.all(),subject = Subject.query.all(),lecturer = Lecturer.query.all())

    