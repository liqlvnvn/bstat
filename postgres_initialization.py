import psycopg2


conn = psycopg2.connect(
    host="localhost",
    database="bstat",
    user="postgres"
    #password=""
    )

c = conn.cursor()

# execute a statement
print('PostgreSQL database version:')
c.execute('SELECT version()')

# display the PostgreSQL database server version
db_version = c.fetchone()
print(db_version)

# Create players table
c.execute('''
    CREATE TABLE players (
    number integer,
    first_name_ru text,
    last_name_ru text,
    mid_name_ru text,
    first_name_en text,
    last_name_en text,
    mid_name_en text,
    height integer,
    weight integer,
    birthday_day integer,
    birthday_month integer,
    birthday_year integer
    )
''')

c.commit()
# close the communication with the PostgreSQL
c.close()
