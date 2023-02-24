
from os import getenv, environ
from flask import Flask, render_template, session, request, redirect, url_for, g
from helper import books, get_text


app=Flask(__name__, static_url_path='/static')

app.secret_key = 'Bruce Wayne is Batman'

@app.route('/', methods=['GET', 'POST'])
def home_page():
    global books
    path_to_pdf = url_for('static', filename='files/Bijbel_01.pdf')
    path_to_pdf = "static/files/Bijbel_01.pdf"
    nt_dict = get_text()
    current_book = "Matteus"

    if request.method == 'POST':
        current_book = request.form['book']
        print(current_book)  
    
    text_list = nt_dict[current_book]
    return render_template('home.html', current_book=current_book, books=books, text_list=text_list)


@app.route('/login', methods=['GET', 'POST'])
def login():
   return "login"

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   return "signup"

@app.route('/logout')
def logout():
    session.pop('userid', None)
    return redirect(url_for('home_page'))

# Do not alter this if statement below
# This should stay towards the bottom of this file
if __name__ == "__main__":
    flask_env = getenv('FLASK_ENV')
    if flask_env != 'production':
        environ['FLASK_ENV'] = 'development'
        app.debug = True
        app.asset_debug = True
        server = Server(app.wsgi_app)
        server.serve()
    app.run()


