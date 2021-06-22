import psycopg2
from flask import Flask,render_template, redirect, url_for,flash,request


app = Flask(__name__) #creating the Flask class object



@app.route('/home', methods=['GET', 'POST'])
def home():
        con = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="yatin123",
    host="postgres.co6j0vfxv1vw.us-east-2.rds.amazonaws.com",
    port='5432'
        )

        #cur = con.cursor()
        #cur.execute("CREATE TABLE users(id serial PRIMARY KEY, name varchar, email varchar, town VARCHAR)")


        #con.commit()
        #cur.close()
        #con.close()
        if request.method == 'POST':
                name = request.form['name']
                town = request.form['town']
                email = request.form['email']
                cur = con.cursor()

                cur.execute("INSERT INTO users(name,town,email) VALUES(%s, %s, %s)",(name,town,email))
                con.commit()
                cur.close()
                con.close()
                flash('Vendor Created Successfully',"success")
        return redirect(url_for('home'))

			
	return render_template('index.html')	

	





