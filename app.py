import psycopg2
import os
from flask import Flask,render_template, redirect, url_for,flash,request,session


app = Flask(__name__) #creating the Flask class object
app.secret_key = 'your secret key'


PORT_NUMBER = os.getenv("PORT_NUMBER")
DB_USER = os.getenv("DB_USER")
DB_PWD = os.getenv("DB_PWD")
DB_URL = os.getenv("DB_URL")
DB_DBNAME = os.getenv("DB_DBNAME")


@app.route('/register', methods=['GET', 'POST'])
def register():
	con = psycopg2.connect(
		dbname=DB_DBNAME,
		user=DB_USER,
		password=DB_PWD,
		host=DB_URL
		)
	if request.method == 'POST':
		name = request.form['name']
		town = request.form['town']
		email = request.form['email']
		password = request.form['password']
		cur = con.cursor()

		cur.execute("INSERT INTO userstable(name,town,email,password) VALUES(%s, %s, %s, %s)",(name,town,email,password))
		con.commit()
		cur.close()
		con.close()
		msg = "Registration Complete. Please Login to your account !"
		return render_template('login.html',msg = msg)

	return render_template('index.html')


@app.route('/users', methods=['GET', 'POST'])
def users():
		con = psycopg2.connect(
		dbname=DB_DBNAME,
		user=DB_USER,
		password=DB_PWD,
		host=DB_URL
		)
		cur = con.cursor()
		cur.execute("SELECT * FROM userstable")
	
		userDetails = cur.fetchall()

		con.commit()
		cur.close()
		con.close()

		return render_template('user.html', userDetails=userDetails)

		
@app.route("/login", methods=['GET', 'POST'])
def login():
	error = ''
	con = psycopg2.connect(
		dbname= DB_DBNAME,
		user=DB_USER,
		password=DB_PWD,
		host=DB_URL
		)
	
    # Check if "username" and "password" POST requests exist (user submitted form)
	if request.method == 'POST' and'email' in request.form and 'password' in request.form:
        # Create variables for easy access
		email = request.form['email']
		password = request.form['password']
		cur = con.cursor()
		
			# Check if account exists using MySQL
		
		cur.execute('SELECT * FROM userstable WHERE email = %s AND password = %s', ( email, password))

		# Fetch one record and return result
		user_var = cur.fetchone()


		# If account exists in accounts table in out database
		if user_var:
			# Create session data, we can access this data in other routes
			session['loggedin'] = True
			session['id'] = user_var[0]
			session['name'] = user_var[1]
			session['email'] = user_var[2]




			
			return redirect('users')

		else:
			error = 'Incorrect email/password!'
		

	return render_template('login.html', error=error)

if __name__ == "__main__":
	app.run(debug=True)


