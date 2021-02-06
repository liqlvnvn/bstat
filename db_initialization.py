import sqlite3

conn = sqlite3.connect("player_database.db")

# Create cursor
c = conn.cursor()

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

# Commit changes
conn.commit()

# Close sqlite connection
conn.close()

