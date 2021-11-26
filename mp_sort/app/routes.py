from flask import render_template
from app import application
from flask import request
import math

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='2D Project Group 1')

@application.route('/task1')
def exercise1():
    return render_template('task1.html', title='2D Project Task 1')

@application.route('/task2')
def exercise2():
    return render_template('task2.html', title='2D Project Task 2')

@application.route('/computetask1', methods=['GET', 'POST'])
def compute1():
    case = request.form["case"]
    pop = request.form["pop"]
    vac = request.form["vac"]
    vacTranform = math.log(float(vac))
    result = -233776.020116272 + (0.0166529519823677*float(case)) + (15358.7509582749*float(vacTranform)) + (-1650.81859934209*float(pop))
    result = round(result,2)
    print(result)
    if result < 0:
        result = 0
    return render_template('compute.html', title='2D Project Task 1', result=result, case=case, vac=vac, pop=pop)

@application.route('/computetask2', methods=['GET', 'POST'])
def compute2():
    vac = request.form["vac"]
    trans = request.form["trans"]
    delta = request.form["delta"]
    t1 = 10 - math.log(-float(trans))
    print(t1)
    transTransform = t1 + (t1 - 6) * 100
    
    result = -2015.4232914426 + (36.6794577018375*float(vac)) + (1.87494732408569*float(delta)) + (-6.31701556134115*float(transTransform))
    result = round(result,2)
    print(result)
    if result < 0:
        result = 0
    return render_template('compute2.html', title='2D Project Task 2', result=result, vac=vac, trans=trans, delta=delta)