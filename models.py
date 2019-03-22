from app import db


class Holiday(db.Model):
    __tablename__ = 'holidays'

   

    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String())
    start = db.Column(db.String())
    end = db.Column(db.String())
    event = db.Column(db.String())

    def __init__(self, month, start, end, event):
        self.month = month
        self.start = start
        self.end = end
        self.event = event

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'month' : self.month,
            'start': self.start,
            'end': self.end,
            'event':self.event
        }


class Schedule(db.Model):
    __tablename__ = 'schedule'

   
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String())
    branch = db.Column(db.String())
    semester = db.Column(db.String())
    date = db.Column(db.String())
    sub_code = db.Column(db.String())
    subject = db.Column(db.String())

    def __init__(self, course, branch, semester, date, sub_code, subject):
        self.course = course
        self.branch = branch
        self.semester = semester
        self.date = date
        self.sub_code = sub_code
        self.subject = subject

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'course': self.course,
            'branch': self.branch,
            'semester': self.semester,
            'date':self.date,
            'sub_code':self.sub_code,
            'subject':self.subject
        }

class Student_Info(db.Model):
    __tablename__ = 'stu_info'

   

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())

    def __init__(self, name, address, city):
        self.name = name
        self.address = address
        self.city = city

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'address': self.address,
            'city':self.city
        }




class Book(db.Model):
    __tablename__ = 'books'



    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String())
    date = db.Column(db.String())
    event = db.Column(db.String())

    def __init__(self, month, date, event):
        self.month = month
        self.date = date
        self.event = event

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'month': self.month,
            'date': self.date,
            'event':self.event
        }