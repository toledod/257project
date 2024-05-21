from flask import Flask
from flask import render_template
import random

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
        sql = "SELECT * FROM spotify WHERE dance = %s"
        danceInt = random.random()
        cur.execute(sql, [danceInt])
        result = cur5.fetchone()
    else:
        sql = "SELECT * FROM spotify WHERE energy = %s"
        energyInt = random.random()
        cur.execute(sql, [energyInt])
        result = cur.fetchone()
    return render_template("homepage.html", someText = result)

@app.route('/month')
def month():
    return render_template("month.html")

@app.route('/day')
def day():
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
        cities_from_state = cur5.fetchone()
    else:
        sql = "SELECT * FROM spotify WHERE energy = %s"
        energyInt = random.random()
        cur.execute(sql, [energyInt])
        cities_from_state = cur.fetchone()

    return render_template("surprise.html")

@app.route('/about')
def about():
    return render_template("about.html")
    



if __name__ == '__main__':
    my_port = 5227
    app.run(host='0.0.0.0', port = my_port) 
