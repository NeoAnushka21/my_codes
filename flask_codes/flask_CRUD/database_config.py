from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Anushka@21'
app.config['MYSQL_DATABASE_DB'] = 'db_flask_ajax'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
