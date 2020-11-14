from appClone import db

class Test(db.Model):
    __tablename__ = "Test"
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(30), unique=True, nullable=False)
