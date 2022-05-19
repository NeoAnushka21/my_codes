from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


# Establishing connection with sqlite
def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect("sample_data.db")

        conn.row_factory = sqlite3.Row

        # print("Database connected successfully")
        return conn
    except Exception as e:
        print(e)
        return "Something went wrong while connecting to database"


@app.route('/')
def student_form():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students_info_ ORDER BY id")
        students = cur.fetchall()
        conn.commit()
        #print(students)
        return render_template('index.html', students=students)
    except Exception as e:
        print(e)
        return "<h3 style='color:red'><b>opps something went wrong while directing to home page</b></h3>"


@app.route("/add_student", methods=["POST", "GET"])
def add_student():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        if request.method == 'POST':
            student_name = request.form['student_name']
            student_department = request.form['student_department']
            student_email = request.form['student_email']
            #print(student_name)

            if student_name == '':
                msg = '<h4 style="color:red"><b>Error !! Name missing</b></h4>'
            elif student_department == '':
                msg = '<h3 style="color:red"><b>Error !! Department missing</b></h3>'
            elif student_email == '':
                msg = '<h3 style="color:red"><b>Error !! Email missing</b></h3>'
            else:
                sql = "SELECT * from students_info_ where email like ?"
                cur.execute(sql, [student_email])
                result = cur.fetchall()
                # print(result)
                if len(result) >= 1:
                    msg = "Oops !! email already exists"
                else:
                    sql = """INSERT INTO students_info_ (name,department,email) VALUES (?,?,?)"""
                    cur.execute(sql, (student_name, student_department, student_email))
                    conn.commit()
                    cur.close()
                    msg = 'New record created successfully'
        return jsonify(msg)
    except Exception as e:
        print(e)
        return '<h2 style="color:red"><b>Something went Wrong while adding student</b></h2>'


@app.route("/update_student", methods=["POST", "GET"])
def update_student():
    try:

        conn = get_db_connection()
        cur = conn.cursor()
        if request.method == 'POST':
            string = request.form['string']
            student_name = request.form['student_name']
            student_department = request.form['student_department']
            student_email = request.form['student_email']
            print(string)

            sql = "UPDATE students_info_ SET name = ?,department = ?, email=? WHERE id = ? "
            cur.execute(sql, [student_name, student_department, student_email, string])
            conn.commit()
            cur.close()
            msg = '<h3 style="color:green"><b>Record successfully Updated</b></h3>'

            # sql = "SELECT * from students_info_  where email like ?"
            # cur.execute(sql, [student_email])
            # result = cur.fetchall()
            # # print(result)
            # if len(result) >= 1:
            #     msg = "Oops !! email already exists"
            # else:
            #     cur.execute("UPDATE students_info_ SET name = ?,department = ?, email=? WHERE id = ? ",
            #                 (student_name, student_department, student_email, string))
            #     conn.commit()
            #     cur.close()
            #     msg = 'Record successfully Updated'
        return jsonify(msg)
    except Exception as e:
        print(e)
        return '<h2 style="color:red"><b>Email Already exists!! please try other one</b></h2>'


@app.route("/delete_student", methods=["POST", "GET"])
def delete_student():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        if request.method == 'POST':
            getid = request.form['string']
            print(getid)
            cur.execute('DELETE FROM students_info_ WHERE id = {0}'.format(getid))
            conn.commit()
            cur.close()
            msg = 'Successfully Deleted student record'
        return jsonify(msg)
    except Exception as e:
        print(e)
        return '<h3 style="color:red"><b>Something went wrong while deleting student details</b></h3>'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
