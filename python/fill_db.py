import sqlite3

sqlite_file = 'country_db.sqlite' # name of the sqlite database file

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# Let's fill our countries table
c.execute('''
INSERT INTO countries
  (country, population, area)
VALUES
  ("Switzerland", 8401120, 41285),
  ("Austria", 8794267, 83879),
  ("Germany", 82349400, 357168),
  ("Liechtenstein", 37341, 160)
;''')


# Let's fill our cities table
c.execute('''
INSERT INTO cities
  (city, country_id, population, area)
VALUES
  ("Geneva",  1,  194565,  15.93),
  ("Zürich",  1,  391359,  87.88),
  ("Bern",    1,  130015,  51.62),
  ("Linz",    2,  198181, 196.05),
  ("Graz",    2,  273838, 127.56),
  ("Vienna",  2, 1867960, 414.65),
  ("Hamburg", 3, 1787408, 755.30),
  ("Berlin",  3, 3520031, 891.68),
  ("Munich",  3, 1450381, 310.70)
;''')

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()