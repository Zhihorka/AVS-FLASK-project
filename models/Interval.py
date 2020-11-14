from appClone import db

class Interval(db.Model):
    __tablename__ = "Interval"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
