from flask import Flask, render_template, json, request, redirect, session
from flask_mysqldb import MySQL, MySQLdb
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key = "secret key"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anushka@21'
app.config['MYSQL_DB'] = 'flask_register'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/userHome')
def userHome():
    print(session.get('sessionusername'))
    if session.get('sessionusername'):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error='Unauthorized Access')


@app.route('/logout')
def logout():
    session.pop('sessionusername', None)
    return redirect('/')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST':
        _name = request.form['inputName']
        _email = request.form['inputEmail']
        _password = request.form['inputPassword']
        # validate the received values
        if _name and _email and _password:
            _hashed_password = generate_password_hash(_password)
            curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curl.execute("SELECT * FROM users WHERE email=%s", (_email,))
            user = curl.fetchone()
            # print(user)
            if user is None:
                curl.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",
                             (_name, _email, _hashed_password,))
                mysql.connection.commit()
                curl.close()
                return json.dumps({'message': 'User created successfully !'})
            else:
                return json.dumps({'html': '<span>A user with this email address already exists</span>'})
        else:
            msg = '{ "html":"<b>Enter the required fields</b>"}'
            msghtml = json.loads(msg)
            return msghtml["html"]
    else:
        return render_template("signup.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        _username = request.form['inputEmail']
        _password = request.form['inputPassword']

        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        # Get user by username
        result = cur.execute("SELECT * FROM users WHERE email = %s", [_username])

        if result > 0:
            # Get stored hash
            data = cur.fetchone()
            password = data['password']

            # Compare Passwords
            if check_password_hash(password, _password):
                # Passed
                session['sessionusername'] = _username
                return redirect('/userHome')
            else:
                error = 'Invalid login'
                return render_template('signin.html', error=error)
            # Close connection
            cur.close()
        else:
            error = 'Username not found'
            return render_template('signin.html', error=error)

    return render_template('signin.html')


if __name__ == '__main__':
    app.run(port=3000,debug=True)
