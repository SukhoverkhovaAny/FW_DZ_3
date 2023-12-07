# Задание №3
# Доработаем задача про студентов
# Создать базу данных для хранения информации о студентах и их оценках в
# учебном заведении.
# База данных должна содержать две таблицы: "Студенты" и "Оценки".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, группа
# и email.
# В таблице "Оценки" должны быть следующие поля: id, id студента, название
# предмета и оценка.
# Необходимо создать связь между таблицами "Студенты" и "Оценки".
# Написать функцию-обработчик, которая будет выводить список всех
# студентов с указанием их оценок.

from flask import Flask, render_template
from models_3 import db, Students, Ratings

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/')
def index():
    return 'Hi!'

STUDENTS = [
    ['Ivan', 'Ivanov', 101, 'VanyaIvanov@mail.ru'],
    ['Maria', 'Andreeva', 102, 'MashaAndreeva@mail.ru'],
    ['Maksim', 'Maksimov', 201, 'MaxMax@mail.ru'],
    ['Evgenii', 'Evgenev', 203, 'EvgenEvgenev@mail.ru'],
    ['Olga', 'Olegova', 101, 'OlechkaO@mail.ru'],
]
RAINGS = [
    [1, 'Psychology', 5],
    [2, 'Geometry', 5],
    [3, 'Psychology', 4],
    [4, 'Biology', 4],
    [5, 'Geometry', 3],
]

@app.cli.command("add-db")
def add_db():
    for rait in RAINGS:
        student_id, subject, rating = rait
        new_raiting = Ratings(student_id = student_id, subject = subject,  rating =  rating)
        db.session.add(new_raiting)
    db.session.commit()
    for student in STUDENTS:
        name, surname, group, email = student
        new_student = Students(name = name, surname = surname, group= group, email = email)
        db.session.add(new_student)
    db.session.commit()
    print('OK')


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/data/')
def show_data():
    students = Students.query.all()
    ratings = Ratings.query.all()
    context = {'students' : students, 'ratings' : ratings, 
               'title' : 'Данные о студентах'}
    return render_template('students.html', **context)


if __name__ == '__main__':
    app.run(debug=True)
