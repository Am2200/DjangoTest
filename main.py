import django
import psycopg2

conn = psycopg2.connect("dbname=Test user=postgres password=qwerty")

cur = conn.cursor()

cur.execute("SELECT * FROM company;")
for row in cur:
    print(row)

cur.close()
conn.close()
