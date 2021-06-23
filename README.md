### First create postgres db in aws.
1) Create user and databse name ```postgres``` and password ```india123```

  
  
  
### After creating postgres db.Login to ubuntu and run some commands.
  ```
  - apt-get update -y 
  - apt-get install python3 python3-pip git 
  - apt-get install postgresql libpq-dev postgresql-client postgresql-client-common
  
  
  ```


### Then clone code ,go inside python_postgres_app folder, install libraries from _requirements.txt_, also you need to pass environment vars.
```
- git clone https://github.com/yatinb14/python_postgres_app.git
- cd python_postgres_app/
- pip3 install -r requirements.txt
- export DB_USER=postgres
- export DB_PWD=india123
- export DB_URL=<postgres_db_endpoint>
- export DB_DBNAME=postgres

```

### Create a table by logging into postgres
```
- psql -h <postgres_db_endpoint> -U postgres -W --dbname postgres
- After this it will ask you for password. Enter password which you have created
  while making postgres db in aws.In my case , it is india123.
- Run command  ***\i userstable.sql*** 
- When you run query Select * from userstable; You will get output like this.

 id | name | email | town | password
----+------+-------+------+----------
(0 rows)
```

### Last step is to run our code
```
- export FLASK_APP=app.py
- export FLASK_ENV=development
- flask run --host 0.0.0.0 --port 8000

```
**It will give the output like**

 Serving Flask app 'app.py' (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on all addresses.
   WARNING: This is a development server. Do not use it in a production deployment.
 * Running on http://172.31.44.4:5001/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 122-780-811

**You can check that app is running on your ```publicip:portnumber/login or publicip:portnumber/register``` eg: http://64.65.222.37:8000/login**

