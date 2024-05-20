from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome to Our Spotify Widget."
    message = message + " This text was produced by concatenating strings in Python! Isn't that exciting!!"
    return render_template("homepage.html", someText = message)

@app.route('/month')
def month():
    return render_template("month.html")

@app.route('/day')
def day():
    return render_template("day2.html")

@app.route('/surprise')
def surprise():
    return render_template("surprise.html")
    



if __name__ == '__main__':
    my_port = 5227
    app.run(host='0.0.0.0', port = my_port) 
