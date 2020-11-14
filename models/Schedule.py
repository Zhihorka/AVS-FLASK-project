from appClone import db


class Schedule(db.Model):
    __tablename__ = "Schedule"
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(30), nullable=False)
    chet = db.Column(db.Boolean, nullable=False)
    group_id = db.Column (db.Integer, db.ForeignKey('group.id'))
    interval_id = db.Column(db.Integer, db.ForeignKey('Interval.id'))
    subject_id = db.Column (db.Integer, db.ForeignKey('Subject.id'))
    lecturer_id = db.Column(db.Integer, db.ForeignKey('Lecturer.id'))
