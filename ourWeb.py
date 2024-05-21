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
        sql = "SELECT * FROM spotify WHERE dance >= %s AND country = US"
        danceInt = random.uniform(0.5, 0.99)
        danceInt = round(danceInt, 1)
        print("danceInt is: ", danceInt)
        cur.execute(sql, [danceInt])
        result = cur.fetchone()
        if result is None: 
            print("No results found for dance value:", danceInt)
        else:
            print("Result found for dance value:", result)
    else:
        sql = "SELECT * FROM spotify WHERE energy >= %s AND country = US"
        energyInt = random.uniform(0.5, .99)
        energyInt = round(energyInt, 1)
        print("energyInt is: ", energyInt)
        cur.execute(sql, [energyInt])
        result = cur.fetchone()
        if result is None: 
            print("No results found for energy value:", energyInt)
        else:
            print("Result found for energy value:", result)
            
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
