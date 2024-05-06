import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="tangumaj",
    user="tangumaj",
    password="ardi363puppy")
    
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
