from flask import Flask

app = Flask(__name__)

students = [
     {'id': '1', 'first_name': 'John', 'last_name': 'Doe', 'age': 18, 'grade': 'A'},
     {'id': '2', 'first_name': 'Jane', 'last_name': 'Smith', 'age': 19, 'grade': 'B'},
     {'id': '3', 'first_name': 'Bob', 'last_name': 'Johnson', 'age': 20, 'grade': 'C'},
     {'id': '4', 'first_name': 'Emily', 'last_name': 'Williams', 'age': 18, 'grade': 'A'},
     {'id': '5', 'first_name': 'Michael', 'last_name': 'Brown', 'age': 19, 'grade': 'B'},
     {'id': '6', 'first_name': 'Samantha', 'last_name': 'Davis', 'age': 22, 'grade': 'A'},
     {'id': '7', 'first_name': 'Oliver', 'last_name': 'Jones', 'age': 20, 'grade': 'B'},
     {'id': '8', 'first_name': 'Sophia', 'last_name': 'Miller', 'age': 21, 'grade': 'A'},
     {'id': '9', 'first_name': 'Ethan', 'last_name': 'Wilson', 'age': 19, 'grade': 'C'},
     {'id': '10', 'first_name': 'Isabella', 'last_name': 'Moore', 'age': 22, 'grade': 'B'}
 ]

@app.route('/api/v1/students/', methods=['GET'])
def get_students():
    return students

@app.route('/api/v1/old_students/', methods=['GET'])
def get_old_students():
    stud = []
    for student in students:
        if student['age'] > 20:
            stud.append(student)   
    return stud

@app.route('/api/v1/young_students/', methods=['GET'])
def get_young_students():
    stud = []
    for student in students:
        if student['age'] < 21:
            stud.append(student)   
    return stud

@app.route('/api/v1/advance_students/', methods=['GET'])
def get_advance_students():
    stud = []
    for student in students:
        if student['age'] < 21 and student['grade'] == 'A':
            stud.append(student)   
    return stud

@app.route('/api/v1/student_names/', methods=['GET'])
def get_student_names():
    stud = []
    for student in students:
        stud.append({'first_name': student['first_name'], 'last_name': student['last_name']})   
    return stud

@app.route('/api/v1/student_ages/', methods=['GET'])
def get_student_ages():
    stud = []
    for student in students:
        stud.append({'student_name': student['first_name'] + ' ' + student['last_name'], 'age': student['age']})   
    return stud

app.run(debug=True)