Create table if not exists userstables (
	id serial PRIMARY KEY,
	name VARCHAR ( 50 ) UNIQUE NOT NULL,
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
  	town VARCHAR ( 50 ) NOT NULL,
  	password VARCHAR ( 50 ) NOT NULL
);

