import sqlite3

sqlite_file = 'country_db.sqlite' # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Creating a new SQLite table for countries
c.execute('''
CREATE TABLE countries (
  country_id integer PRIMARY KEY,
  country text UNIQUE NOT NULL,
  population integer,
  area real
);''')

# Creating a new SQLite table for cities
c.execute('''
CREATE TABLE cities (
  city_id integer PRIMARY KEY,
  city text UNIQUE NOT NULL,
  country_id integer NOT NULL,
  population real,
  area real,
  FOREIGN KEY(country_id) REFERENCES countries(country_id)
);''')

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()