# Задание №2
# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания,
# количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы".
# Написать функцию-обработчик, которая будет выводить список всех книг с
# указанием их авторов.

from flask import Flask, render_template
from models_2 import db, Authors, Books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)

@app.route('/')
def index():
    return 'Hi!'

BOOKS = [
    ['War and peace', 1867, 1000, 2],
    ['Anna Karenina', 1878, 500, 2],
    ["Capitain's daughter", 1836, 2010, 1],
    ['Stationmaster', 1831, 203, 1]
]
AUTHORS = [['Alex', 'Pushkin'], ['Lev', 'Tolstoy']]

@app.cli.command("add-db")
def add_db():
    for author in AUTHORS:
        name, surname = author
        new_author = Authors(name = name, surname = surname)
        db.session.add(new_author)
    db.session.commit()
    for book in BOOKS:
        name, year_pub, copies, id_author = book
        new_book = Books(name = name, year_pub = year_pub, copies = copies, id_author = id_author)
        db.session.add(new_book)
    db.session.commit()
    print('OK')


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('OK')


@app.route('/data/')
def show_data():
    authors = Authors.query.all()
    books = Books.query.all()
    context = {'authors' : authors, 'books' : books}
    return render_template('book.html', **context)


if __name__ == '__main__':
    app.run(debug=True)