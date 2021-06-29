from flask import Flask
from flask import render_template
from config import Config

app = Flask(__name__)
app.config.from_object(Config)



# Selects the page for which a function is to be defined. Right now there will only be one page in your website.

@app.route('/')

def hello():

    return "<h1>Hello World!</h1>" \
           "\nThis is my introduction to Flask!" \
           "\nI can write a lot of things on this page.\nLet's get started!"


@app.route('/index')
def index():
    user = {'username': 'Andrew'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Jose'},
            'body': 'I love spagetti!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
# The above function returns the HTML code to be displayed on the page

@app.route("/hi/")
def who():
    return "Who are you?"


@app.route("/hi/<username>")
def greet(username):
    return f"Hi there, {username}!"


if __name__ == '__main__':

   app.run()