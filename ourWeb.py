from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    message = "Welcome to My Independent Assignment Webpage."
    message = message + " This text was produced by concatenating strings in Python! Isn't that exciting!!"
    return render_template("homepage.html", someText = message)

if __name__ == '__main__':
    my_port = 5227
    app.run(host='0.0.0.0', port = my_port) 
