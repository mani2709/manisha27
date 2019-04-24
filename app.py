import os
from flask import Flask,session,redirect, url_for, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import extract
import calendar
from sqlalchemy import cast, DATE




app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Holiday
from models import Student_Info
from models import Schedule
from models import Timetable
from models import Syllabus
from models import Calendar

#from models import Holiday

@app.route("/")
def hello():
    return "Hello !"

@app.route("/add")
def add_holiday():
    month=request.args.get('month')
    date=request.args.get('date')
    event=request.args.get('event')
    try:
        holiday=Holiday(
            month=month,
            date=date,
            event=event
        )
        db.session.add(holiday)
        db.session.commit()
        return "Holiday added. holiday id={}".format(holiday.id)
    except Exception as e:
        return(str(e))
        
@app.route("/getall")
def get_all():
    try:
        
        holidays=Holiday.query.all()
        return render_template("list.html",holidays = holidays)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))

@app.route("/get",methods=['GET', 'POST'] )
def get_by_id():
    print("helloooo")
    from models import Holiday
    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['parameters']['function']
    month = req['queryResult']['parameters']['Months']
    print("action is", action)
    

    try: 
        if action=='Holiday':
            holiday=Holiday.query.filter_by(start_date = month).all()
            print("holiday is", holiday)
            
            
            if(len(holiday)==0):
                 response =  """
                        {0}
                    
                        """.format("There are no holidays in month of "+ month)
                 reply = {"fulfillmentText": response}
                 print("hi there")
                 return jsonify(reply)
            i = 0
            Result=''
            response=''
            reply= ''
            for row in holiday:

                i = i + 1
                print("print rows", row.id, row.start_date, row.end_date, row.event)

                Result= 'There is a holiday in the month of '+ str(month) + ' on'+str(row.start_date) + 'for the occasion ' + str(row.event) + '  '  
           # Result= 'Dear candidate there is one holiday in the month of {0}'.format(holiday.month)

                print("result is", Result)
                response = response + """
                        {0}
                    
                        """.format(Result,)
                
                reply = {"fulfillmentText": response,}

            return jsonify(reply)
        else:

    
            response =  """
                    Response : {0}
                    """.format("action is not valid")
            reply = {"fulfillmentText": response,}
        #return jsonify(holiday.serialize())
    except Exception as e:
        return(str(e))


@app.route("/add/form",methods=['GET', 'POST'])
def add_book_form():
    if request.method == 'POST':
        
        start_date=request.form.get('start_date')
        end_date=request.form.get('end_date')
        event=request.form.get('event')
        try:
            holiday=Holiday(
    
                start_date=start_date,
                end_date=end_date,
                event=event
            )
            
            db.session.add(holiday)
            db.session.commit()
            return "Holiday added. holiday id={}".format(holiday.id)
        except Exception as e:
            return(str(e))
    return render_template("getdata.html")
    
@app.route("/add/studentinfo",methods=['GET', 'POST'])
def add_student_info():
    if request.method == 'POST':
        name=request.form.get('name')
        address=request.form.get('address')
        city=request.form.get('city')
        try:
            table=Student_Info(
                name=name,
                address=address,
                city=city
            )
            db.session.add(table)
            db.session.commit()
            return "Info added. info id={}".format(table.id)
        except Exception as e:
            return(str(e))
    return render_template("studentdata.html")


@app.route("/getdata")

def get_data():

    try:

        All_Holidays=Holiday.query.all()

        All_Students=Student_Info.query.all()

        for row in All_Students:

            print("All Students name -",row.name)

            print("All Students city -",row.city)

        return render_template("list.html",All_Holidays = All_Holidays,All_Students = All_Students)



        #return  jsonify([e.serialize() for e in books])

    except Exception as e:

        return(str(e))





@app.route("/get/<name_>" )

def get_by_name(name_):

    #req = request.get_json(silent=True, force=True)

    #print("in comin grequest",req)

    #action = req['queryResult']['parameters']['Holiday']

    #month = req['queryResult']['parameters']['Months']

    try:

        table=Holiday.query.filter_by(name=name_).first()

        print("print rows", table)

        return (table)

        #return jsonify(table.serialize())

    except Exception as e:


        return(str(e))


@app.route("/add/schedule",methods=['GET', 'POST'])
def add_schedule():
    if request.method == 'POST':
        course=request.form.get('course')
        branch=request.form.get('branch')
        semester=request.form.get('semester')
        date=request.form.get('date')
        sub_code=request.form.get('sub_code')
        subject=request.form.get('subject')
        try:
            data=Schedule(
                course=course,
                branch=branch,
                semester=semester,
                date=date,
                sub_code=sub_code,
                subject=subject
            )
            db.session.add(data)
            db.session.commit()
            return "schedule added. schedule id={}".format(data.id)
        except Exception as e:
            return(str(e))
    return render_template("exam.html")

@app.route("/getschedule")
def get_schedule():
    try:
        
        schedule=Schedule.query.all()
        return render_template("list.html",schedule = schedule)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))

@app.route("/get1",methods=['GET', 'POST'] )
def get1():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['parameters']['function1']
    course = req['queryResult']['parameters']['Courses']
    sem_no = req['queryResult']['parameters']['sem_no']
    branch = req['queryResult']['parameters']['Branch']
    print("action is", action)
    print("course is", course)
   

    try: 
        if action=='Exams_schedule.Exams_schedule-custom':
            schedule=Schedule.query.filter_by(course=course , semester=sem_no, branch=branch).all()
            
            #holiday_count=Holiday.query.filter_by(month=month).count()
            #print("count the holidays",holiday_count, len(holiday))

            #print("Month is",row.month)
            #print("Date is",holiday.date)
            #print("Event is",holiday.event)
            if(len(schedule)==0):
                 response =  """
                        {0}
                    
                        """.format("Schedule updation is pending for now. Please check after some time")
                 reply = {"fulfillmentText": response}
                 #print("hi there")
                 return jsonify(reply)
            i = 0
            Result=''
            response=''
            reply= ''
            for row in schedule:

                i = i + 1
                print("print rows", row.date, row.sub_code, row.subject)

                Result= 'There is a holiday in the month of '+ str(row.date) + ' on'+str(row.sub_code) + 'for the occasion ' + str(row.subject) + '  '  
           # Result= 'Dear candidate there is one holiday in the month of {0}'.format(holiday.month)

                print("result is", Result)
                response = response + """
                        {0}
                    
                        """.format(Result,)
                
                reply = {"fulfillmentText": response,}

            return jsonify(reply)
        else:

    
            response =  """
                    Response : {0}
                    """.format("action is not valid")
            reply = {"fulfillmentText": response,}
        #return jsonify(holiday.serialize())
    except Exception as e:
        return(str(e))




@app.route("/add/timetable",methods=['GET', 'POST'])
def add_timetable():
    if request.method == 'POST':
        course=request.form.get('course')
        branch=request.form.get('branch')
        semester=request.form.get('semester')
        timing=request.form.get('timing')
        monday=request.form.get('monday')
        tuesday=request.form.get('tuesday')
        wednesday=request.form.get('wednesday')
        thursday=request.form.get('thursday')
        friday=request.form.get('friday')
        saturday=request.form.get('saturday')
        
        
        try:
            timetable=Timetable(
                course=course,
                branch=branch,
                semester=semester,
                timing=timing,
                monday=monday,
                tuesday=tuesday,
                wednesday=wednesday,
                thursday=thursday,
                friday=friday,
                saturday=saturday

            )
            db.session.add(timetable)
            db.session.commit()
            return "timetable added. timetable id={}".format(timetable.id)
        except Exception as e:
            print("hujhjgjhg")
            return(str(e))
     return render_template("time_table.html")




@app.route("/get/timetable")
def get_timetable():
    try:
        
        timetable=Timetable.query.all()
        return render_template("list.html",timetable = timetable)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))




@app.route("/get3",methods=['GET', 'POST'] )
def get3():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['parameters']['function2']
    course = req['queryResult']['parameters']['Courses']
    sem_no = req['queryResult']['parameters']['sem_no']
    branch = req['queryResult']['parameters']['Branch']
    print("action is", action)
    print("course is", course)
   

    try: 
        if action== Timetable:
            timetable= Timetable.query.filter_by(course=course , semester=semester, branch=branch).all()
            
            #holiday_count=Holiday.query.filter_by(month=month).count()
            #print("count the holidays",holiday_count, len(holiday))

            #print("Month is",row.month)
            #print("Date is",holiday.date)
            #print("Event is",holiday.event)
            if(len(Timetable)==0):
                 response =  """
                        {0}
                    
                        """.format("Timetable updation is pending for now. Please check after some time")
                 reply = {"fulfillmentText": response}
                 #print("hi there")
                 return jsonify(reply)
            i = 0
            Result=''
            response=''
            reply= ''
            for row in Timetable:

                i = i + 1
                print("print rows", row.date, row.sub_code, row.subject)

                Result=  str(row.monday) + str(row.tuesday) + str(row.wednesday) + '  '  
           # Result= 'Dear candidate there is one holiday in the month of {0}'.format(holiday.month)

                print("result is", Result)
                response = response + """
                        {0}
                    
                        """.format(Result,)
                
                reply = {"fulfillmentText": response,}

            return jsonify(reply)
        else:

    
            response =  """
                    Response : {0}
                    """.format("action is not valid")
            reply = {"fulfillmentText": response,}
        #return jsonify(holiday.serialize())
    except Exception as e:
        return(str(e))

@app.route("/add/syllabus",methods=['GET', 'POST'])
def add_syllabus():
    if request.method == 'POST':
        units= request.form.get('units')
        course=request.form.get('course')                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        branch=request.form.get('branch')
        semester=request.form.get('semester')
        sub_code=request.form.get('sub_code')
        subject=request.form.get('subject')
        try:
            data=Syllabus(
                units=units,
                course=course,
                branch=branch,
                semester=semester,
                sub_code=sub_code,
                subject=subject
            )
            db.session.add(data)
            db.session.commit()
            return "syllabus added. syllabus id={}".format(data.id)
        except Exception as e:
            return(str(e))
    return render_template("syllabus.html")

@app.route("/getsyllabus")
def get_syllabus():
    try:
        
        syllabus=Syllabus.query.all()
        return render_template("list.html",syllabus = syllabus)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))


#--------------------------------------calender--------------------------------------------------------#

@app.route("/add/calendar",methods=['GET', 'POST'])
def add_calendar():
    if request.method == 'POST':
        
        month=request.form.get('month')
        date=request.form.get('date')
        event=request.form.get('event')
        try:
            calendar=Calendar(
    
                month=month,
                date=date,
                event=event
            )
            
            db.session.add(calendar)
            db.session.commit()
            print("calendar", calendar)
            message = "calendar updated. calendar id={}".format(calendar.id)
            session['message'] = message
            print("session is",session)
            return redirect(url_for('get_cal'))
            #return render_template("list.html",calendar = calendar)

            
        except Exception as e:
            return(str(e))
    return render_template("calendar.html")

@app.route("/getcal")
def get_cal():
    try:
        
        calendar=Calendar.query.all()
        print("message value was previously set to:" +session['message'])
        message = session['message']
        session['message'] = ''
        return render_template("list.html",calendar = calendar,message =message)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))

@app.route("/get5",methods=['GET', 'POST'] )
def get5():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['parameters']['calendar']
    #month = req['queryResult']['parameters']['Months']
    print("action is", action)
    #print("month is", month)
    #today_month = datetime.today().month
    #print('today_month', today_month)
    #months = Holiday.query.filter_by(extract('month', Holiday.datetime) == datetime.today().month.strftime("%B")).all()
    #print("months is", months)

    #Payment.query.filter(extract('month', Payment.due_date) >= datetime.today().month,)

    #start =datetime.strptime(request.vars.Expected_Possession_Date,"%Y-%m-%d").date()
    #end   =datetime.strptime(request.vars.Expected_Possession_Date,"%Y-%m-%d").date()

    try: 
        if action=='Academic calendar':
            calendar=Calendar.query.all()
            
            #holiday_count=Holiday.query.filter_by(month=month).count()
            #print("count the holidays",holiday_count, len(holiday))

            #print("Month is",row.month)
            #print("Date is",holiday.date)
            #print("Event is",holiday.event)2
            if(len(calendar)==0):
                 response =  """
                        {0}
                    
                        """.format("There are no holidays  ")
                 reply = {"fulfillmentText": response}
                 print("hi there")
                 return jsonify(reply)
            i = 0
            Result=''
            response=''
            reply= ''
            for row in calendar:

                i = i + 1
                print("print rows", row.id, row.month, row.date, row.event)

                Result=  str(row.month) +str(row.date)  + str(row.event) + '  '  
           # Result= 'Dear candidate there is one holiday in the month of {0}'.format(holiday.month)

                print("result is", Result)
                response = response + """
                        {0}
                    
                        """.format(Result,)
                
                reply = {"fulfillmentText": response,}

            return jsonify(reply)
        else:

    
            response =  """
                    Response : {0}
                    """.format("action is not valid")
            reply = {"fulfillmentText": response,}
        #return jsonify(holiday.serialize())
    except Exception as e:
        return(str(e))


#-------------------------------------------------Events---------------------------------------------------

@app.route("/add/event",methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        
        month=request.form.get('month')
        date=request.form.get('date')
        event=request.form.get('event')
        try:
            event1=Event(
    
                month=month,
                date=date,
                event=event
            )
            
            db.session.add(event1)
            db.session.commit()
            return "event1 added. event1 id={}".format(event1.id)
             
        except Exception as e:
            return(str(e))
    return render_template("event.html")

@app.route("/geteve")
def get_eve():
    try:
        
        events = Event.query.all()
        return render_template("list.html", events = events)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))


if __name__ == '__main__':
    app.run()