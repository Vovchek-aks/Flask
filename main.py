from flask import Flask, url_for, render_template

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


@app.route('//<title>')
@app.route('/index/<title>')
def base(title):
    return render_template('base.html', title=title)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1', debug=True)


