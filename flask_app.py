from os import getenv, environ
from flask import Flask, render_template, session, request, redirect, url_for, g
from helper import books, get_text, nr_of_chapters
from db import init_db
import sqlite3


app=Flask(__name__, static_url_path='/static')
app.secret_key = 'Bruce Wayne is Batman'
init_db(app)

show_login_btn = True

@app.route('/', methods=['GET', 'POST'])
def home_page():
    global show_login_btn
    global books
    global nr_of_chapters
    path_to_pdf = url_for('static', filename='files/Bijbel_01.pdf')
    path_to_pdf = "static/files/Bijbel_01.pdf"
    nt_dict = get_text()
    current_book = "Matteus"
    if 'userid' in session:
        userid = session['userid']
        if 'current_book' in session:
            current_book = session['current_book']
            print("Changed current book to: ", current_book, "based on login (session)")


    if request.method == 'POST':
        current_book = request.form['book']
        print("Book clicked: ", current_book)
        if 'userid' in session:
            session['current_book'] = current_book
        else:
            print("All Keys:")
            for key in session.keys():
                print(f"{key}: {session[key]}")
            
    
    text_list = nt_dict[current_book]
    print(f"Current book: {current_book}, text_list: {text_list}")

    current_nr_of_chapters = nr_of_chapters[books.index(current_book)]
    chapters = ""
    for i in range(1, current_nr_of_chapters+1):
        chapters += f" <a href='#ch{i}'><span class='chapter_btn' value='{i}'>{i}</span></a>"
    return render_template('home.html', current_book=current_book, books=books, text_list=text_list, chapters=chapters, show_login_btn=show_login_btn, path_to_pdf=path_to_pdf)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global show_login_btn
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == "Alex" and password == "qwerty":
            session['userid'] = "Alex"
            show_login_btn = False
            print("User logged in.")
            return redirect(url_for('home_page'))
        else:
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
   return "signup"

@app.route('/logout')
def logout():
    print("User logged out.")
    global show_login_btn
    session.pop('userid', None)
    show_login_btn = True
    
    return redirect(url_for('home_page'))


# ------------- functions that are not routes after this line ----------------





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


