This is a flask application that allows the user to fill an employee form and submit it.
The employee data is stored in MySQL Database.
--------------------------
Setup instructions 
--------------------------

1. Clone the repository
2. Download MySQL installer https://dev.mysql.com/downloads/installer/
3. Install MySQL workbench and server
4. Setup your local MySQL instance, note down the username, password, and host address
5. Open workbench and select your MySQL instance
6. Click on File menu and select 'Run SQL script'
7. Select the script from the database directory of this project ../Employee_App/database/Employee.sql
8. Once the database is created, go to conf folder and edit the database_conf file
9. Update the respective fields with the username, password and host address of your MySQL instance. Set the Database name as "employees" and save the file
10. Now create a virtual environment with python 3.6 or above and activate it
11. Install the reqirement file `pip install -r requirements.txt`
12. Run the flask app `python flaskapp.py`

