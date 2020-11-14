from appClone import db

class Lecturer(db.Model):
    __tablename__ = "Lecturer"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), unique=False, nullable=False)
    last_name = db.Column(db.String(30), unique=False, nullable=False)
    patronymic = db.Column(db.String(30), unique=True, nullable=False)
