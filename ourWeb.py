from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()
    pickSong()

@app.route('/month')
def month():
    return render_template("month.html")

@app.route('/day')
def day():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()
    # sql = "SELECT * FROM spotify WHERE AND EXTRACT(DAY FROM date) = %s AND EXTRACT(MONTH FROM date) = %s"
    # cur.execute(sql, [energyInt])
    
    return render_template("day2.html")

@app.route('/surprise')
def surprise():
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()

    randomInteger = random.randint(1, 2)
    if randomInteger == 1:
        sql = "SELECT * FROM spotify WHERE dance = %s"
        danceInt = random.random()
        cur.execute(sql, [danceInt])
        result = cur.fetchone()
    else:
        sql = "SELECT * FROM spotify WHERE energy = %s"
        energyInt = random.random()
        cur.execute(sql, [energyInt])
        result = cur.fetchone()

    return render_template("surprise.html")

@app.route('/about')
def about():
    return render_template("about.html")
    




def pickSong():
    # pick a number 1 or 2, this will deicde if we get a song based off of dancablity (1) or energy (2)
    randomInteger = random.randint(1, 2)
    if randomInteger == 1:
        sql = "SELECT * FROM spotify WHERE dance >= %s AND country = 'US' AND EXTRACT(YEAR FROM date) = 2024 AND EXTRACT(MONTH FROM date) BETWEEN 2 AND 4"
        danceInt = random.uniform(0.0, 0.967)
        cur.execute(sql, [danceInt])
        result = cur.fetchmany(20)
        val = random.randint(0, 19)

    else:
        sql = "SELECT * FROM spotify WHERE energy >= %s AND country = 'US' AND EXTRACT(YEAR FROM date) = 2024 AND EXTRACT(MONTH FROM date) BETWEEN 2 AND 4"
        
        energyInt = random.uniform(0.0, .963)
        cur.execute(sql, [energyInt])
        result = cur.fetchmany(20)
        val = random.randint(0, 19)

    return render_template("homepage.html", someTitle = result[val][0], someArtist = result[val][1])


if __name__ == '__main__':
    my_port = 5227
    app.run(host='0.0.0.0', port = my_port) 
