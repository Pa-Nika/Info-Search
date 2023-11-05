import traceback
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5432/info_search_flask'
db = SQLAlchemy(app)


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_title = db.Column(db.String(128), nullable=False)
    small_title = db.Column(db.String(15), nullable=False)
    date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return '<University %r>' % self.id


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    university = db.relationship("University", backref=db.backref('student', lazy=True))

    def __repr__(self):
        return '<Student %r>' % self.id


with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/university/history')
def university_history():
    university = University.query.order_by(University.full_title).all()
    return render_template("history/university_history.html", university=university)


@app.route('/add/university', methods=['POST', 'GET'])
def add_university():
    if request.method == 'POST':
        full_title = request.form['full_title']
        small_title = request.form['small_title']
        date_str = request.form['date']
        date_obj = datetime.strptime(date_str, '%d.%m.%Y').date()

        university = University(full_title=full_title, small_title=small_title, date=date_obj)
        try:
            db.session.add(university)
            db.session.commit()
            return redirect('/add/university')

        except Exception as e:
            print(e)
            print(traceback.format_exc())
            return "УУУПС, что-то пошло не так"
    else:
        return render_template("add/add_university.html")


@app.route('/edit/university/<int:id>', methods=['POST', 'GET'])
def edit_university(id):
    university = University.query.get(id)
    if request.method == 'POST':
        university.full_title = request.form['full_title']
        university.small_title = request.form['small_title']
        date_str = request.form['date']
        university.date = datetime.strptime(date_str, '%d.%m.%Y').date()
        try:
            db.session.commit()
            return redirect('/university/history')
        except:
            return "УУУПС, что-то пошло не так"
    else:
        return render_template("edit/edit_university.html",  university=university)


@app.route('/delete/university/<int:id>', methods=['POST', 'GET'])
def delete_university(id):
    university = University.query.get_or_404(id)
    students_with_university = Student.query.filter_by(university_id=id).all()

    try:
        for student in students_with_university:
            db.session.delete(student)
        db.session.delete(university)
        db.session.commit()
        return redirect('/university/history')
    except:
        return "УУУПС, что-то пошло не так"


@app.route('/student/history')
def student_history():
    students = Student.query.order_by(Student.name).all()
    return render_template("history/students_history.html", students=students)


@app.route('/add/student', methods=['POST', 'GET'])
def add_student():
    universities = University.query.all()
    if request.method == 'POST':
        name = request.form['name']
        birthday_str = request.form['birthday']
        year = request.form['year']
        university_id = request.form['university']
        birthday_obj = datetime.strptime(birthday_str, '%d.%m.%Y').date()

        student = Student(name=name, birthday=birthday_obj, year=year, university_id=university_id)
        try:
            db.session.add(student)
            db.session.commit()
            return redirect('/add/student')

        except:
            return "УУУПС, что-то пошло не так"
    else:
        return render_template("add/add_student.html",  universities=universities)


@app.route('/edit/student/<int:id>', methods=['POST', 'GET'])
def edit_student(id):
    student = Student.query.get(id)
    universities = University.query.all()
    if request.method == 'POST':
        student.name = request.form['name']
        birthday_str = request.form['birthday']
        student.year = request.form['year']
        student.university_id = request.form['university']
        birthday_obj = datetime.strptime(birthday_str, '%d.%m.%Y').date()
        student.birthday = birthday_obj
        try:
            db.session.commit()
            return redirect('/student/history')

        except:
            return "УУУПС, что-то пошло не так"
    else:
        return render_template("edit/edit_student.html",  student=student, universities=universities)


@app.route('/delete/student/<int:id>', methods=['POST', 'GET'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    try:
        db.session.delete(student)
        db.session.commit()
        return redirect('/student/history')
    except:
        return "УУУПС, что-то пошло не так"


if __name__ == '__main__':
    app.run(debug=True)
