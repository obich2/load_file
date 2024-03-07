from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" 
                            /> <title>Пример формы</title> </head> <body> <h1>Загрузка фотографии</h1> 
                            <h2>для участия в миссии</h2> <div>
                             <form class="login_form" method="post" form method="post" enctype="multipart/form-data">
                                
                                    <label for="photo">Приложите фотографию</label>


                                    <div class="form-group space">
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    
                                    <img src="{url_for('static', filename='img/photo.jpg')}" 
           alt="">

                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        f = f.read()
        with open("static/img/photo.jpg", 'wb') as file:
            file.write(f)
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
