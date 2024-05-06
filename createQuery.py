import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="tangumaj",
    user="tangumaj",
    password="ardi363puppy")
    
cur = conn.cursor()

sql = "SELECT * FROM spotify WHERE country='US'"
    
cur.execute( sql )

row = cur.fetchone()

if row == None:
    print("Not found, please look for another city")
else:
    print(row)

cur2 = conn.cursor()

sql2 = "SELECT * FROM spotify WHERE country='US' ORDER BY dailyr DESC"

cur2.execute( sql2 )
row2 = cur2.fetchone()

print(row2)
