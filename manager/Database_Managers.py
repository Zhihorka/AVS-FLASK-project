from models.Lecturer import Lecturer
from models.Interval import Interval
from models.Subject import Subject
from models.Group import Group
from models.Schedule import Schedule


class DatabaseManager:
    def __init__(self, db):
        self.db = db


    def add_lecturer(self, **kwargs):
        lecturer = Lecturer(first_name=kwargs["first_name"],
                            last_name=kwargs["last_name"],
                            patronymic=kwargs["patronymic"]
                            )
        self.db.session.add(lecturer)
        self.db.session.commit()


    def add_subject(self, **kwargs):
        subject = Subject(name=kwargs["name"])

        self.db.session.add(subject)
        self.db.session.commit()


    def add_interval(self, **kwargs):
        interval = Interval(name=kwargs["name"])

        self.db.session.add(interval)
        self.db.session.commit()


    def add_group(self, **kwargs):
        group = Group(name = kwargs["name"])

        self.db.session.add(group)
        self.db.session.commit()

    def add_item_to_Schedule(self, **kwargs):
        scheduleItem = Schedule(
                    day=kwargs["day"],
                    chet=kwargs["chet"],
                    group_id=kwargs["group_id"],
                    interval_id=kwargs["interval_id"],
                    subject_id=kwargs["subject_id"],
                    lecturer_id=kwargs["lecturer_id"]
                    )
        self.db.session.add(scheduleItem)
        self.db.session.commit()

