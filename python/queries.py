import sqlite3

sqlite_file = 'country_db.sqlite' # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Print all countries
c.execute('''
SELECT
  cities.*,
  countries.country, countries.area
FROM cities
INNER JOIN countries on countries.country_id = cities.country_id
;''')

all_rows = c.fetchall()
print("All countries: ")
for row in all_rows:
    print(row)


# Find id of a city
c.execute('''
SELECT
  city_id
FROM
  cities
WHERE
  city = "Zürich"
;''')

id_zurich = c.fetchone()
print("ID of Zürich: ", id_zurich[0])

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()