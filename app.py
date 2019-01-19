from flask import Flask,render_template

from data import Faculties

app=Flask(__name__)     #__variable__ is a special variable in python

myFaculties=Faculties()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def a():
    return render_template('index.html')

@app.route('/register')
def reg():
    return render_template('register.html')

@app.route('/faculty')
def re():
    return render_template('faculties.html',facultyList=myFaculties)

if __name__=='__main__':
    app.run(debug=True)