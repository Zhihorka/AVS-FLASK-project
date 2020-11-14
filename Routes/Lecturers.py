from flask.blueprints import Blueprint
from flask import render_template
from models.Lecturer import Lecturer


lecturers = Blueprint('home', __name__, template_folder='templates', static_folder='static')


@lecturers.route('/')
def index():
    return render_template('index.html',lecturers = Lecturer.query.all())