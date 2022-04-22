import sqlite3


# Create connection
conn = sqlite3.connect('app.db')
cur = conn.cursor()

# Create table
sql = '''CREATE TABLE IF NOT EXISTS customer (
    customer_id INTEGER PRIMARY KEY,
    first_name  TEXT,
    last_name   TEXT,
    email       TEXT
)'''
cur.execute(sql)

# Insert rows
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('John', 'Smith', 'john.smith@esmartdata.org')''')
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('Joe', 'Doe', 'joe.doe@esmartdata.org')''')
cur.execute('''INSERT INTO customer (first_name, last_name, email)
VALUES ('Mike', 'Smith', 'mike.smith@esmartdata.org')''')

# Make a query here
cur.execute('''SELECT * FROM customer''')
result = cur.fetchall()
print(result)

cur.execute('''SELECT COUNT(*) FROM customer''')
print(cur.fetchall()[0][0])

# Commit changes
conn.commit()

# Close connection
conn.close()