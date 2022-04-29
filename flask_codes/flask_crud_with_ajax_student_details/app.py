from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anushka@21'
app.config['MYSQL_DB'] = 'student_data'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql_connector = MySQL(app)


@app.route('/')
def student_form():
    try:
        cur = mysql_connector.connection.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute("SELECT * FROM stud_data ORDER BY id")
        employee = cur.fetchall()
        return render_template('index.html', employee=employee)
    except Exception:
        return "<h3 style='color:red'><b>opps something went wrong while directing to home page</b></h3>"


@app.route("/add_student", methods=["POST", "GET"])
def add_student():
    try:
        cursor = mysql_connector.connection.cursor()
        cur = mysql_connector.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            student_name = request.form['student_name']
            student_department = request.form['student_department']
            student_phone = request.form['student_phone']
            print(student_name)
            if student_name == '':
                msg = '<h4 style="color:red"><b>Error !! Name missing</b></h4>'
            elif student_department == '':
                msg = '<h3 style="color:red"><b>Error !! Department missing</b></h3>'
            elif student_phone == '':
                msg = '<h3 style="color:red"><b>Error !! phone number missing</b></h3>'
            else:
                cur.execute("INSERT INTO stud_data (name,department,phone) VALUES (%s,%s,%s)",
                            [student_name, student_department, student_phone])
                mysql_connector.connection.commit()
                cur.close()
                msg = '<h3 style="color:green"></b>Student details added successfully</b></h3>'
        return jsonify(msg)
    except Exception:
        return '<h3 style="color:red"><b>Something went wrong while adding student details</b></h3>'


@app.route("/update_student", methods=["POST", "GET"])
def update_student():
    try:

        cursor = mysql_connector.connection.cursor()
        cur = mysql_connector.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            string = request.form['string']
            student_name = request.form['student_name']
            student_department = request.form['student_department']
            student_phone = request.form['student_phone']
            print(string)
            cur.execute("UPDATE stud_data SET name = %s, department = %s, phone = %s WHERE id = %s ",
                        [student_name, student_department, student_phone, string])
            mysql_connector.connection.commit()
            cur.close()
            msg = '<h3 style="color:green"><b>Record successfully Updated</b></h3>'
        return jsonify(msg)
    except Exception as e:
        return '<h3 style="color:red"><b>Something went wrong while updating  student details</b></h3>'


@app.route("/delete_student", methods=["POST", "GET"])
def delete_student():
    try:
        cursor = mysql_connector.connection.cursor()
        cur = mysql_connector.connection.cursor(MySQLdb.cursors.DictCursor)
        if request.method == 'POST':
            getid = request.form['string']
            print(getid)
            cur.execute('DELETE FROM stud_data WHERE id = {0}'.format(getid))
            mysql_connector.connection.commit()
            cur.close()
            msg = '<h3 style="color:green"><b>Record successfully deleted</b></h3>'
        return jsonify(msg)
    except Exception:
        return '<h3 style="color:red"><b>Something went wrong while deleting student details</b></h3>'


if __name__ == "__main__":
    app.run(debug=True)
