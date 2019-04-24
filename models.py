from app import db
from datetime import datetime




class Holiday(db.Model):
    __tablename__ = 'holidays'

   

    id = db.Column(db.Integer, primary_key=True)
    
    start_date = db.Column(db.DateTime, default=datetime.utcnow)

    end_date = db.Column(db.DateTime, default=datetime.utcnow)

    event = db.Column(db.String())

    def __init__(self, start_date, end_date, event):
        
        self.start_date = start_date
        self.end_date = end_date
        self.event = event

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
        
            'start_date': self.start_date,
            'end_date': self.end_date,
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
    registration_number = db.Column(db.String())
    email = db.Column(db.String())

    def __init__(self, name, registration_number, email):
        self.name = name
        self.registration_number = registration_number
        self.email = email

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'name': self.name,
            'registration_number': self.registration_number,
            'email':self.email
        }

class Syllabus(db.Model):
    __tablename__ = 'syllabus'

   
    id = db.Column(db.Integer, primary_key=True)
    units= db.Column(db.String())
    course = db.Column(db.String())
    branch = db.Column(db.String())
    semester = db.Column(db.String())
    date = db.Column(db.String())
    sub_code = db.Column(db.String())
    subject = db.Column(db.String())

    def __init__(self, units, course, branch, semester,  sub_code, subject):
        self.units = units
        self.course = course
        self.branch = branch
        self.semester = semester
        self.sub_code = sub_code
        self.subject = subject

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'units': self.units,
            'course': self.course,
            'branch': self.branch,
            'semester': self.semester,
            'sub_code':self.sub_code,
            'subject':self.subject
        }


class Timetable(db.Model):
    __tablename__ = 'timetable'

   
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String())
    branch = db.Column(db.String())
    semester = db.Column(db.String())
    timing = db.Column(db.String())
    monday = db.Column(db.String())
    tuesday = db.Column(db.String())
    wednesday = db.Column(db.String())
    thursday = db.Column(db.String())
    friday = db.Column(db.String())
    saturday = db.Column(db.String())
    

    def __init__(self, course, branch, semester, timing, monday, tuesday, wednesday, thursday, friday, saturday):
        self.course = course
        self.branch = branch
        self.semester = semester
        self.timing = timing
        self.monday = monday
        self.tuesday = tuesday
        self.wednesday = wednesday
        self.thursday = thursday
        self.friday = friday
        self.saturday = saturday

        
    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id, 
            'course': self.course,
            'branch': self.branch,
            'semester': self.semester,
            'timing': self.timing,
            'monday': self.monday,
            'tuesday': self.tuesday,
            'wednesday': self.wednesday,
            'thursday': self.thursday,
            'friday': self.friday,
            'saturday': self.saturday
            
        }

class Calendar(db.Model):
    __tablename__ = 'calendar'

   

    id = db.Column(db.Integer, primary_key=True)
    
    month =  db.Column(db.String())

    date =db.Column(db.String())

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




 
class Event(db.Model):
    __tablename__= 'events'

   

    id = db.Column(db.Integer, primary_key=True)
    
    month =  db.Column(db.String())

    date =db.Column(db.String())

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