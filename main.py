from flask import Flask, url_for, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email
from data import db_session
from data.users import User

app = Flask(__name__)


@app.route('/promotion')
def reklama():
    return 'Человечество вырастает из детства.<br/>' \
           'Человечеству мала одна планета.<br/>' \
           'Мы сделаем обитаемыми безжизненные пока планеты.<br/>' \
           'И начнем с Марса!<br/>' \
           'Присоединяйся!'


@app.route('/image_mars')
def image():
    return f'''
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                <h1>Жди нас, Марс!<h1/><br/>
                <img src="{url_for('static', filename='img/mars.png')}" 
                alt="здесь должна была быть картинка, но не нашлась">
                <br/>Вот она какая, красная планета.
            '''


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


@app.route('/astronaut_selection')
def astronaut_selection():
    return render_template('astronaut_selection.html')


@app.route('/<title>')
@app.route('/index/<title>')
def base(title):
    return render_template('base.html', title=title)


@app.route('/choice/<planet>')
def choice(planet):
    return render_template('choice.html', planet=planet)


@app.route('/training/<prof>')
def training(prof):
    prof = prof.lower()
    if 'инженер' in prof or 'строитель' in prof:
        name = 'Инженерные тренажеры'
        im = 'Инжир.png'
    else:
        name = 'Научные симуляторы'
        im = 'химбио.png'
    return render_template('training.html', title='Ракета', name=name,
                           image=url_for('static', filename=f'img/{im}'))


@app.route('/list_prof/<ul_ol>')
def profs(ul_ol):
    return render_template('list_prof.html', title='Пруфы))', ul_ol=ul_ol,
                           profs=[
                            'Рабочий',
                            'Крестьянка',
                            'Военнослужащий',
                            'Партийный деятель',
                            'Член верховно совета народный комисаров ЦК ВКП(б)'
                           ])


if __name__ == '__main__':
    db_session.global_init("db/blogs.db")

    # добавление в таблицу
    user = User()
    user.name = 'Пользователь 3'
    user.about = 'Не любит'
    user.email = 'dontlike@ya.ru'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    # выборка
    # db_sess = db_session.create_session()
    # users = db_sess.query(User).filter(User.id > 1).all()
    # print(users)

    # изменение
    # db_sess = db_session.create_session()
    # user = db_sess.query(User).filter(User.id == 1).first()
    # user.name = 'Суперпользователь 1'
    # db_sess.commit()
    # db_sess = db_session.create_session()
    # news = News(title="Первая новость", content="Привет блог!",
    #             user_id=1, is_private=False)
    # db_sess.add(news)
    # db_sess.commit()

    app.run(debug=True)


