from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    taskId=db.Column(db.Integer, primary_key=True)
    task=db.Column(db.String(8000), nullable=False)
    taskStatus=db.Column(db.String(50), default='Incomplete')
    taskCreationDate=db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, task):
        self.task=task

@app.route('/')
def home():
    tasksList=Todo.query.all()
    return render_template('home.html', t=tasksList)

@app.route('/add/', methods=['POST'])
def add():
    taskDesc=request.form['task']
    newTask = Todo(taskDesc)
    db.session.add(newTask)
    db.session.commit()
    # print(newTask)
    # print(Todo.query.all())
    return redirect('/', 302)

@app.route('/complete/<id>')
def completeTask(id):
    data=Todo.query.filter_by(taskId=id).first()
    data.taskStatus = 'Complete'
    db.session.commit()
    t1=Todo.query.filter_by(taskId=id).first()
    print(t1.taskStatus)
    return redirect('/', 302)

@app.route('/incomplete/<id>')
def incompleteTask(id):
    data=Todo.query.filter_by(taskId=id).first()
    data.taskStatus = 'Incomplete'
    db.session.commit()
    t1=Todo.query.filter_by(taskId=id).first()
    print(t1.taskStatus)
    return redirect('/', 302)

@app.route('/update/<id>')
def updateTask(id):
    data=Todo.query.filter_by(taskId = id).first()
    return render_template('updatePage.html', task=data)

@app.route('/updateDone' , methods = ['POST'])
def updateTaskDone():
    dataID = request.form['taskID']
    dataValue  = request.form['task']
    findTask = Todo.query.filter_by(taskId=dataID).first()
    findTask.task = dataValue
    db.session.commit()
    return redirect('/', 302)

@app.route('/delete/<id>')
def delete(id):
    data = Todo.query.filter_by(taskId=id).first() 
    db.session.delete(data)
    db.session.commit()
    return redirect('/', 302)

