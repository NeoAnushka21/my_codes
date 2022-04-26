from flask import Flask, render_template, json, request, redirect, session, jsonify
from flask_mysqldb import MySQL, MySQLdb  # pip install flask-mysqldb https://github.com/alexferl/flask-mysqldb
from datetime import datetime

app = Flask(__name__)

app.secret_key = "caircocoders-ednalan-2020"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Anushka@21'
app.config['MYSQL_DB'] = 'blogs'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def main():
    return redirect('/userHome')


@app.route('/userHome')
def userHome():
    session['sessionusername'] = "cairocoders@gmail.com"
    print(session.get('sessionusername'))
    if session.get('sessionusername'):
        return render_template('userHome.html')
    else:
        return render_template('error.html', error='Unauthorized Access')


@app.route('/addBlog', methods=['GET', 'POST'])
def addBlog():
    now = datetime.now()
    print("now =", now)
    if request.method == 'POST':
        _title = request.form['inputTitle']
        _description = request.form['inputDescription']
        _user = session.get('sessionusername')
        # validate the received values
        if _title and _description:
            cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            result = cur.execute("SELECT * FROM users WHERE email = %s", [_user])
            print(result)
            if result > 0:
                data = cur.fetchone()
                blog_user_id = data['id']
                cur.execute(
                    "INSERT INTO tbl_blog (blog_title, blog_description, blog_user_id, blog_date) VALUES (%s,%s,%s,%s)",
                    (_title, _description, blog_user_id, now,))
                mysql.connection.commit()
                cur.close()
                return redirect('/userHome')
            else:
                error = 'Invalid login'
                return render_template('addBlog.html', error=error)
        else:
            error = 'Enter the required fields'
            return render_template('addBlog.html', error=error)

    return render_template('addBlog.html')


@app.route('/getBlog')
def getBlog():
    if session.get('sessionusername'):
        # _user = session.get('sessionusername')
        _user = '12'
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute("SELECT * FROM tbl_blog WHERE blog_user_id = %s", [_user])
        blogs = cur.fetchall()
        blogs_dict = []
        for blog in blogs:
            blog_dict = {
                'Id': blog['blog_id'],
                'Title': blog['blog_title'],
                'Description': blog['blog_description'],
                'Date': blog['blog_date']}
            blogs_dict.append(blog_dict)
        return json.dumps(blogs_dict)
    else:
        print("error getblog")
        return render_template('error.html', error='Unauthorized Access')


@app.route('/getBlogById', methods=['GET', 'POST'])
def getBlogById():
    if session.get('sessionusername'):
        _id = request.form['id']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        result = cur.execute("SELECT * FROM tbl_blog WHERE blog_id = %s", [_id])
        blogs = cur.fetchall()
        blogs_dict = []
        for blog in blogs:
            blog_dict = {
                'Id': blog['blog_id'],
                'Title': blog['blog_title'],
                'Description': blog['blog_description']}
            blogs_dict.append(blog_dict)
        return json.dumps(blogs_dict)
    else:
        return render_template('error.html', error='Unauthorized Access')


@app.route('/updateBlog', methods=['POST'])
def updateBlog():
    if session.get('sessionusername'):
        _title = request.form['title']
        _description = request.form['description']
        _blog_id = request.form['id']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("""
            UPDATE tbl_blog
            SET blog_title = %s,
                blog_description = %s
            WHERE blog_id = %s
        """, (_title, _description, _blog_id))
        mysql.connection.commit()
        cur.close()
        return json.dumps({'status': 'OK'})
    else:
        return render_template('error.html', error='Unauthorized Access')


@app.route('/deleteBlog', methods=['POST'])
def deleteBlog():
    if session.get('sessionusername'):
        _id = request.form['id']
        _user = session.get('user')
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute('DELETE FROM tbl_blog WHERE blog_id = {0}'.format(_id))
        mysql.connection.commit()
        cur.close()
        return json.dumps({'status': 'OK'})
    else:
        return render_template('error.html', error='Unauthorized Access')


if __name__ == '__main__':
    app.run(debug=True)