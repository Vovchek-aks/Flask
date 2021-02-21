from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


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


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


