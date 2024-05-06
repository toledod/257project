import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="toledod",
    user="toledod",
    password="mask777glass")

if conn is not None:
    print( "Connection Worked!" )
else:
    print( "Problem with Connection" )
    
cur = conn.cursor()

sql = """DROP TABLE IF EXISTS spotify;
CREATE TABLE spotify (
  name text,
  artists text,
  dailyr int,
  movement real,
  wmovement real,
  country text,
  date date,
  pop real,
  expl text,
  timems real,
  dance real,
  energy real,
  acousticness real, 
  tempo real
);"""

cur.execute( sql )
print("hit execute")
