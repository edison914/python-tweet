# !!START
from flask import Flask, render_template, redirect
from .config import Config
from .tweets import tweets
from random import choice
from .forms.form import TweetForm
from datetime import date

app = Flask(__name__)

app.config.from_object(Config)
# !!END




# print(random_tweet)

@app.route('/')
def index():
    random_tweet = choice(tweets)
    return render_template('index.html', tweet=random_tweet)

@app.route('/feed')
def feed():
    return render_template('feed.html', tweets=tweets)

@app.route('/new', methods= ['GET', 'POST'])
def new_tweet():
    form = TweetForm()
    if form.validate_on_submit():
        new_tweet = {
            'id':len(tweets)+1,
            'author': form.data['author'],
            'date': date.today(),
            'tweet': form.data['tweet'],
            'likes': 0
        }

        tweets.append(new_tweet)
        print(new_tweet)

        return redirect('/feed', 302)
    if form.errors:
        return form.errors
    return render_template('new_tweet.html', form = form )
