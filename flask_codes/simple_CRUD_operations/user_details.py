import pymysql
from flask import Flask
from flask_table import Table, Col, LinkCol
from flaskext.mysql import MySQL
from flask import flash, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.secret_key = "secret key"


class Results(Table):

    user_id = Col('Id', show=False)
    user_name = Col('Name')
    user_email = Col('Email')
    user_password = Col('Password', show=False)
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='user_id'))
    delete = LinkCol('Delete', 'delete_user', url_kwargs=dict(id='user_id'))


mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Anushka@21'
app.config['MYSQL_DATABASE_DB'] = 'student_data'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)


@app.route('/new_user')
def add_user_view():
    return render_template('add.html')


# for adding new user
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
            sql = "INSERT INTO students(user_name, user_email, user_password) VALUES(%s, %s, %s)"
            data = (_name, _email, _hashed_password,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User added successfully!')
            return redirect('/')
        else:
            return 'Error while adding user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return "<h1>email already exists , please go back and change it</h1>"


# Displaying the users , fetching from database
@app.route('/')
def users():

    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM students")
        rows = cursor.fetchall()
        table = Results(rows)
        table.border = True
        return render_template('users.html', table=table)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return "oops something went wrong"


@app.route('/edit/<int:id>')
def edit_view(id):

    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM students WHERE user_id=%s", id)
        row = cursor.fetchone()
        if row:
            return render_template('edit.html', row=row)
        else:
            return 'Error loading #{id}'.format(id=id)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return "oops something went wrong"


# To update user details
@app.route('/update', methods=['POST'])
def update_user():

    conn = None
    cursor = None
    try:
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        _id = request.form['id']
        # Validating the received records
        if _name and _email and _password and _id and request.method == 'POST':
            # To save password not as plain text
            _hashed_password = generate_password_hash(_password)
            print(_hashed_password)
            # Saving the edits
            sql = "UPDATE students SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
            data = (_name, _email, _hashed_password, _id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            flash('User updated successfully!')
            return redirect('/')
        else:
            return 'Error while updating user'
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return "oops something went wrong"


# for deleting the user
@app.route('/delete/<int:id>')
def delete_user(id):
    conn = None
    cursor = None
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE user_id=%s", (id,))
        conn.commit()
        flash('User deleted successfully!')
        # Gets redirected to users.html
        return redirect('/')
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
    return "oops something went wrong"


if __name__ == "__main__":
    app.run(debug=True)
