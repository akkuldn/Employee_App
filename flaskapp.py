"""
Flask app to submit a form and store the data in Database
"""
from flask import Flask,render_template,flash,url_for,redirect
from form import EmployeeForm
app = Flask(__name__)
from flask_mysqldb import MySQL
import conf.database_conf as db_conf

app.config['MYSQL_HOST'] = db_conf.MYSQL_HOST
app.config['MYSQL_USER'] = db_conf.MYSQL_USER
app.config['MYSQL_PASSWORD'] = db_conf.MYSQL_PASSWORD
app.config['MYSQL_DB'] = db_conf.MYSQL_DATABASE
app.config['SECRET_KEY'] = "qxf2"
mysql = MySQL(app)

@app.route("/",methods=["GET","POST"])
def homepage():
    "This page contains the form to be filled by the user "
    form = EmployeeForm()
    if form.validate_on_submit():
        name=form.name.data
        email=form.email.data
        department=form.department.data
        run_queries(name,email,department)
        flash(f'Form submitted successfully', 'success')
        return redirect(url_for("homepage"))
    return render_template('EmployeeForm.html',form=form)

def run_queries(name,email,department):
    "Setup the connection to database and run the queries"
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO employee(email, name) VALUES (%s, %s);", (email, name))
    cur.execute("SELECT id from department WHERE department_name=%s;",[department])
    fetched_id=cur.fetchone()
    department_id,*removed=fetched_id
    cur.execute("UPDATE employee SET department_id=%s WHERE name=%s;",(department_id, name))
    mysql.connection.commit()
    cur.close()


if __name__=="__main__":
    app.run(debug=True)
