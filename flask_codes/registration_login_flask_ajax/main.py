import rest_api_
from app import app
from flask import render_template, request, redirect, flash
from werkzeug.security import generate_password_hash
from database_config import mysql


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/signup')
def add_user_view():
    return render_template('/add.html')


@app.route('/add', methods=['POST'])
def add_user():

    conn = None
    cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _name and _email and _password and request.method == 'POST':
            # To save password not as plain text
            _hashed_password = generate_password_hash(_password)
            # Saving the edits
            sql = "INSERT INTO user(name, email, pwd) VALUES(%s, %s, %s)"
            data = (_name, _email, _hashed_password,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User added successfully!')
            return redirect('/index.html')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return "email already exists , please go back and change it"


@app.route('/login/page')
def login_page():
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
