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

sql2 = "SELECT * FROM spotify WHERE country='US' AND date='2024-04-30' ORDER BY dailyr DESC"

cur2.execute( sql2 )
row2 = cur2.fetchone()

print(row2)

cur3 = conn.cursor()

sql3 = "SELECT * FROM spotify ORDER BY dance DESC"

cur3.execute( sql3 )
row3 = cur3.fetchone()

print(row3)
