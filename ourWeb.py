from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome to Our Spotify Widget."
    message = message + " This text was produced by concatenating strings in Python! Isn't that exciting!!"
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()

    randomInteger = random.randint(1, 2)
    if randomInteger == 1:
        sql = "SELECT * FROM spotify WHERE dance = ?"
        danceInt = random.uniform(0.5, 1.0)
        danceInt = round(danceInt, 1)
        cur.execute(sql, [danceInt])
        result = cur.fetchone()
        if result == None: 
            result == danceInt
    else:
        sql = "SELECT * FROM spotify WHERE energy = %f"
        energyInt = random.uniform(0.5, 1.5)
        cur.execute(sql, [energyInt])
        result = cur.fetchone()
        if result == None: 
            result == energyInt
    return render_template("homepage.html", someText = result[0])

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
    sql = "SELECT * FROM spotify WHERE dance = %s"
    
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
    



if __name__ == '__main__':
    my_port = 5227
    app.run(host='0.0.0.0', port = my_port) 
