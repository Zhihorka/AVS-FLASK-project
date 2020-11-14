from flask.blueprints import Blueprint
from flask import render_template
from models.Subject import Subject


subjects = Blueprint('sub', __name__, template_folder='templates', static_folder='static')


@subjects.route('/subjects')
def index():
    return render_template('Subjects.html',subjects = Subject.query.all())


