from flask.blueprints import Blueprint
from flask import render_template
from models.Schedule import Schedule


schedule = Blueprint('sched', __name__, template_folder='templates', static_folder='static')


@schedule.route('/schedule')
def index():
    return render_template('Schedule.html',schedule = Schedule.query.all())



