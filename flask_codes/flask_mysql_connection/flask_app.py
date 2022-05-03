from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from configparser import ConfigParser
import yaml
app = Flask(__name__)

# Configure db
db = yaml.load(open('my_config.yaml'), Loader=yaml.FullLoader)
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

# Instantiating mysql object
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Fetch form data
        user_details = request.form
        user_name = user_details['name']
        user_email = user_details['email']
        sql_cur = mysql.connection.cursor()
        sql_cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)", (user_name, user_email))
        mysql.connection.commit()
        sql_cur.close()
        return '<h1>"User added Successfully"</h1>'
    return render_template('home.html')


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    result_values = cur.execute("SELECT * FROM users")
    if result_values > 0:
        user_details = cur.fetchall()
        return render_template('users.html', userDetails=user_details)


if __name__ == "__main__":
    app.run(debug=True,port=3000)
