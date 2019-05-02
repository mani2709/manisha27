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
from models import Event

#from models import Holiday

@app.route("/")
def hello():
    return render_template("front.html")

#------------------------------------HOLIDAY--------------------------------------------------------
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
    #action = req['queryResult']['parameters']['function']
    month = req['queryResult']['parameters']['Months']

    print("month is", month)

    

    try: 

        
        holiday=Holiday.query.filter(extract('month',Holiday.start_date) == month).all()
            #Event.query.filter(extract('month',Event.start_date) >= datetime.today().month).all()
        print("holiday is", holiday)
            
            
        if(len(holiday)==0):

            response =  """
                    {0}
                    
                    """.format("There are no holidays in month of "+ month)
            reply = {"fulfillmentText": response}
            print("hi there")
            return reply
        i = 0
        Result=''
        response=''
        reply= ''
        for row in holiday:

            i = i + 1
            print("print rows", row.id, row.start_date, row.end_date, row.event)

            
            Result= 'There is a holiday on ' +str(row.start_date) +' '+ 'for the occasion ' + str(row.event) + '  '  
            print("result is", Result)
            response = response + """
                    {0}
                    
                    """.format(Result,)
                
            reply = {"fulfillmentText": response,}
        return reply
    except Exception as e:
        return(str(e))


#-------------------------------STUDENT INFO---------------------------------------------------------
    
    
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

#-----------------------------------SCHEDULE-------------------------------------------------------------

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

@app.route("/schedule",methods=['GET', 'POST'] )
def schedule():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    
    course = req['queryResult']['parameters']['Courses']
    semester = req['queryResult']['parameters']['sem_no']
    branch = req['queryResult']['parameters']['Branch']
    #print("action is", action)
    print("course is", course)
   

    try: 
        schedule=Schedule.query.filter_by(course=course , semester=semester, branch=branch).all()
        print("hi there")   
            
        if(len(schedule)==0):

            response =  """
                    {0}
                    
                    """.format("Schedule updation is pending for now. Please check after some time")
            reply = {"fulfillmentText": response}
                 #print("hi there")
            return reply
        i = 0
        Result=''
        response=''
        reply= ''
        for row in schedule:

            i = i + 1
            print("print rows", row.date, row.sub_code, row.subject)

            Result=  str(row.date)+str(row.sub_code)  + str(row.subject) + '  '  
          
            print("result is", Result)
            response = response + """
                    {0}
                    
                    """.format(Result,)
                
            reply = {"fulfillmentText": response,}

            return reply
        
    except Exception as e:
        return(str(e))

#-------------------------------------TIMETABLE------------------------------------------------------


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

@app.route("/time",methods=['GET', 'POST'] )
def timet():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    
    course = req['queryResult']['parameters']['Courses']
    semester = req['queryResult']['parameters']['sem_no']
    branch = req['queryResult']['parameters']['Branch']
    print("course is",course)
    
   

    try: 
        timetable=Timetable.query.filter_by(course=course , semester=semester, branch=branch).all()
        print(timetable)
        if(len(timetable)==0):


            response =  """
                    {0}
                    
                    """.format("Timetable updation is pending for now. Please check after some time")
            reply = {"fulfillmentText": response}
                 
            return reply
        i = 0
        Result=''
        response=''
        reply= ''
        for row in timetable:

            i = i + 1
            print("print rows", row.timing, row.monday, row.tuesday)

            Result=  str(row.timing)+'  '+str(row.monday) +'  ' + str(row.tuesday) + '  ' + str(row.wednesday) + '  ' + str(row.thursday)+ '  ' + str(row.friday) + '  '  + str(row.saturday) + '  '  
          
            print("result is", Result)
            response = response + """
                    {0}
                    
                    """.format(Result,)
                
            reply = {"fulfillmentText": response,}
        return reply

            
    except Exception as e:
        return(str(e))
#---------------------------------------SYLLABUS------------------------------------------------------

@app.route("/gettt")
def test():
    return render_template("test1.html")

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


@app.route("/syllabus",methods=['GET', 'POST'] )
def syllabus():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    print(req)
    #action = req['queryResult']['parameters']['Syllabus']
    course = req['queryResult']['parameters']['Courses']
    semester = req['queryResult']['parameters']['sem_no']
    branch = req['queryResult']['parameters']['Branch']
    #print("action is", action)
    print("course is", course)
   

    try: 
        
        syllabus=Syllabus.query.filter_by(course=course , semester=semester, branch=branch).all()
            
            
        if(len(syllabus)==0):

            response =  """
                    {0}
                    
                    """.format("Syllabus updation is pending for now. Please check after some time")
            reply = {"fulfillmentText": response}
                 #print("hi there")
            return reply
        i = 0
        Result=''
        response=''
        reply= ''
        for row in syllabus:

            i = i + 1
            print("print rows", row.date, row.sub_code, row.subject)

            Result=  str(row.sub_code)+'  '+str(row.subject) +' ' + str(row.units) + '  '  
          
            print("result is", Result)
            response = response + """
                    {0}
                    
                    """.format(Result,)
                
            reply = {"fulfillmentText": response,}
        return reply

            
        
        
    except Exception as e:
        return(str(e))

#------------------------------------CALENDAR-----------------------------------------------------------
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
    return render_template("calender.html")

@app.route("/getcal")
def get_cal():
    try:
        
        calendar=Calendar.query.all()
        #print("message value was previously set to:" +session['message'])
        message = session['message']
        session['message'] = ''
        return render_template("list.html",calendar = calendar,message =message)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))

@app.route("/calendar",methods=['GET', 'POST'] )
def calendar():
    print("helloooo")

    req = request.get_json(silent=True, force=True)
    
    try: 
        
            calendar=Calendar.query.all()
            print(calendar)
            
            if(len(calendar)==0):
                 response =  """
                        {0}
                    
                        """.format("No calendar updates")
                 reply = {"fulfillmentText": response}
                 print("hi there")
                 return reply
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
            return reply

            
        
    except Exception as e:
        return(str(e))

#----------------------------------------EVENT-------------------------------------------------------------




@app.route("/add/event",methods=['GET', 'POST'])
def add_event():
    if request.method == 'POST':
        
        start_date=request.form.get('start_date')
        end_date=request.form.get('end_date')
        event=request.form.get('event')
        try:
            events=Event(
    
                start_date=start_date,
                end_date=end_date,
                event=event
            )
            
            db.session.add(events)
            db.session.commit()
            return "Event added. event id={}".format(events.id)
        except Exception as e:
            return(str(e))
    return render_template("event.html")


@app.route("/getevent")
def get_event():
    try:
        
        events=Event.query.all()
        return render_template("list.html",events = events)

        return  jsonify([e.serialize() for e in books])
    except Exception as e:
        return(str(e))

@app.route("/events",methods=['GET', 'POST'] )
def getevents():
    print("helloooo")
    from models import Holiday
    req = request.get_json(silent=True, force=True)
    #action = req['queryResult']['parameters']['function']
    month = req['queryResult']['parameters']['Months']

    #print("action is", action)
    

    try: 

        event=Event.query.filter(extract('month',Event.start_date) == month).all()
        print("Event is", event)
        if(len(event)==0):

            response =  """
                    {0}
                    
                    """.format("There are no events in month of "+ month)
            reply = {"fulfillmentText": response}
            print("hi there")
            return reply
            
            
            
        i = 0
        Result=''
        response=''
        reply= ''
        #d=datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
        #day_string = d.strftime('%d')
        #print(day_string)
        for row in event:

            i = i + 1
            print("print rows", row.id, row.start_date, row.end_date, row.event)
            

            Result= 'There is an event from' +' '+str(row.start_date) +' '+ 'to'+ ' '+str(row.end_date)+' '+'for the occasion '+' ' + str(row.event) + '  '  
           

            print("result is", Result)
            response = response + """
                    {0}
                    
                    """.format(Result,)
                
            reply = {"fulfillmentText": response,}
        return reply
            

            
        
    except Exception as e:
        return(str(e))

        

@app.route("/action",methods=['GET', 'POST'] )
def getaction():
    print("helloooo")
    
    
    req = request.get_json(silent=True, force=True)
    action = req['queryResult']['action']
   
    
            
       

    try: 
        if action=='Holiday':
            print("action is",action)
            reply = get_by_id()
            
            

        if action=='Academic_Calendar':
            print("action is",action)
            reply = calendar()
            
            
            
            
        if action=='Event':
            print("action is",action)
            reply = getevents()
            #return jsonify(reply)
            

            
            
        if action=='Syllabus.Syllabus-custom':
            print("action is",action)
            reply = syllabus()
            
            

        if action=='Timetable.Timetable-custom':
            print("action is",action)
            reply=time()
            

        if action=='Exams_schedule.Exams_schedule-custom':
            print("action in try is",action)
            reply= schedule()
            
            

        
    except Exception as e:
        response =  """                        Response : {0}
                        """.format("An application error has occured")
        reply = {"fulfillmentText": response,}
    finally:    
        return jsonify(reply)

        


if __name__ == '__main__':
    app.run()