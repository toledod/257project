from flask import Flask
from flask import render_template
import random
import psycopg2

app = Flask(__name__)
#starting webpage
@app.route('/')
def pickSongForHome():
    #function gets song to display
    #on homepage from a big fetch list
    #to keep a variety of songs
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()
    # pick a number 1 or 2, this will deicde if we get a song based off of dancablity (1) or energy (2)
    randomInteger = random.randint(1, 2)
    if randomInteger == 1:
        sql = "SELECT * FROM spotify WHERE dance >= %s AND country = 'US' AND EXTRACT(YEAR FROM date) = 2024 AND EXTRACT(MONTH FROM date) BETWEEN 2 AND 4"
        danceInt = random.uniform(0.0, 0.9)
        cur.execute(sql, [danceInt])
        result = cur.fetchmany(20)
        val = random.randint(0, 19)

    else:
        sql = "SELECT * FROM spotify WHERE energy >= %s AND country = 'US' AND EXTRACT(YEAR FROM date) = 2024 AND EXTRACT(MONTH FROM date) BETWEEN 2 AND 4"
        
        energyInt = random.uniform(0.0, 0.9)
        cur.execute(sql, [energyInt])
        result = cur.fetchmany(20)
        val = random.randint(0, 19)

    return render_template("homepage.html", someTitle = result[val][0], someArtist = result[val][1])

@app.route('/month/<month>')
def month(month):
    #month makes a request to sql with information
    #about the month picked
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()
    sql = "SELECT name, artists, date, pop FROM spotify WHERE EXTRACT(MONTH FROM date) = %s AND country = 'US' ORDER BY pop DESC, date DESC"
    cur.execute(sql, [month])
    table = cur.fetchall()

    
    return render_template("month.html", tablefetch = table)






@app.route('/day/<month>/<day>')
def day(month, day):
    
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()
    sql = "SELECT * FROM spotify WHERE EXTRACT(DAY FROM date) = %s AND EXTRACT(MONTH FROM date) = %s AND country = 'US' ORDER BY dailyr DESC"
    cur.execute(sql, [day, month])
    
    topSong = cur.fetchone()
    #checking to make sure our fetch
    #got something, and using valid to
    #tell our html file if it has something to display
    if topSong == None:
        songName = "Data Not"
        songArtist = "Found"
        valid = 0
    else:
        songName = topSong[0]
        songArtist = topSong[1]
        valid = 1
    
    
    return render_template("day2.html", songName = songName, songArtist = songArtist, dayNum = day, monthNum = month, valid = valid)

@app.route('/surprise')
def surprise():
    #similar to the main menu, surprise
    #finds a random song and displays it.
    conn = psycopg2.connect(
        host="localhost",
        port=5432,   
        database="toledod",
        user="toledod",
        password="mask777glass")
    
    cur = conn.cursor()

    randomInteger = random.randint(1, 4)
    if randomInteger == 1:
        sql = "SELECT * FROM spotify WHERE country = 'US' AND EXTRACT(YEAR FROM date) = 2024 AND EXTRACT(MONTH FROM date) = 1 ORDER BY dance DESC"
        cur.execute(sql)
        result = cur.fetchmany(30)
        val = random.randint(0, 29)

    elif randomInteger == 2:
        sql = "SELECT * FROM spotify WHERE country = 'US' AND EXTRACT(YEAR FROM date) = 2024 AND EXTRACT(MONTH FROM date) = 2 ORDER BY energy DESC"
        cur.execute(sql)
        result = cur.fetchmany(30)
        val = random.randint(0, 29)
        
    elif randomInteger == 3:
        sql = "SELECT * FROM spotify WHERE country = 'US' AND EXTRACT(YEAR FROM date) = 2024 AND EXTRACT(MONTH FROM date) = 3 ORDER BY energy DESC"
        cur.execute(sql)
        result = cur.fetchmany(30)
        val = random.randint(0, 29)
        
    else:
        sql = "SELECT * FROM spotify WHERE country = 'US' AND EXTRACT(YEAR FROM date) = 2024 EXTRACT(MONTH FROM date) = 4 ORDER BY energy DESC"
        cur.execute(sql)
        result = cur.fetchmany(30)
        val = random.randint(0, 29)

    

    #if fetch comes back empty, run surprise again (rarely will happen)
    if(result == None):
        surprise()
    else:
         return render_template("surprise.html", someTitle = result[val][0], someArtist = result[val][1], someRank = result[val][2], 
                          explict = result[val][8], popScore = result[val][7], someDate = result[val][6] )


@app.route('/about')
def about():
    return render_template("about.html")
    





if __name__ == '__main__':
    my_port = 5227
    app.run(host='0.0.0.0', port = my_port) 
