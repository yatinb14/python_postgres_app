import psycopg2
from flask import Flask,render_template, redirect, url_for,flash,request,session


app = Flask(__name__) #creating the Flask class object
app.secret_key = 'your secret key'



@app.route('/', methods=['GET', 'POST'])
def home():
		con = psycopg2.connect(
		dbname="postgres",
		user="postgres",
		password="yatin123",
		host="postgres.co6j0vfxv1vw.us-east-2.rds.amazonaws.com"
		)

		#cur = con.cursor()
		#cur.execute("CREATE TABLE userstable(id serial PRIMARY KEY, name varchar, email varchar, town VARCHAR)")


		#con.commit()
		#cur.close()
		#con.close()
		print("Successfully connected!")
		return "<h1>hello, this is our Demo web page</h1>";

		



@app.route('/register', methods=['GET', 'POST'])
def register():
	con = psycopg2.connect(
		dbname="postgres",
		user="postgres",
		password="yatin123",
		host="postgres.co6j0vfxv1vw.us-east-2.rds.amazonaws.com"
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
		dbname="postgres",
		user="postgres",
		password="yatin123",
		host="postgres.co6j0vfxv1vw.us-east-2.rds.amazonaws.com"
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
		dbname="postgres",
		user="postgres",
		password="yatin123",
		host="postgres.co6j0vfxv1vw.us-east-2.rds.amazonaws.com"
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


