import sqlite3


# Create connection
conn = sqlite3.connect('app.db')
cur = conn.cursor()

# Create table
sql = '''CREATE TABLE IF NOT EXISTS category (
    category_id INTEGER PRIMARY KEY,
    category_name  TEXT NOT NULL
)'''
cur.execute(sql)

# Insert rows
cur.execute('''INSERT INTO category (category_name)
VALUES ('technology')''')
cur.execute('''INSERT INTO category (category_name)
VALUES ('e-commerce')''')
cur.execute('''INSERT INTO category (category_name)
VALUES ('gaming')''')

cur.execute('''UPDATE category
SET category_name = 'online shop'
WHERE category_id = 2;''')

# Commit changes
conn.commit()

# Make a query here
cur.execute('''SELECT * FROM category''')
categories = cur.fetchall()
for c in categories:
    print(c)

# Close connection
conn.close()