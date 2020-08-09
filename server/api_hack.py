import flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from tweet import TwitterScrapper
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
# from sentiment_analyzer import TweetAnalyzer
# from datetime import datetime

app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///konnect.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class TweetAnalyzer():
    # Function to clean tweets and remove
    def __init__(self):
        return
        # pass

    # def cleanTweet(self, intweet):
    #     return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", intweet).split())

    def sentimentAnalyzer(self, businessID):
        analysis = SentimentIntensityAnalyzer()

        cur_tweets = Business.query.filter_by(id=businessID)[0].tweets
        frating = 0
        count = 0

        for tweet in cur_tweets:
            vs = analysis.polarity_scores(tweet.content)
            crating = (vs['compound'] + 1) * 5/2
            frating += crating
            count += 1
        rating = frating/count
        rating = str(rating)[:3]
        rating = float(rating)
        Business.query.filter_by(id=businessID)[0].rating = rating
        db.session.commit()
        return


class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=True, default='default.jpg')
    rating = db.Column(db.Float, nullable=True)
    address = db.Column(db.Text, nullable=True)
    tags = db.Column(db.Text, nullable=True)
    keywords = db.Column(db.Text, nullable=False)

    tweets = db.relationship('Tweet', backref='biz', lazy=True)

    def __repr__(self):
        return f"Business('{self.name}', '{self.address}', '{self.tags}')"


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Float, nullable=True, default=0.0)
    business_id = db.Column(db.Integer, db.ForeignKey(
        'business.id'), nullable=False)

    def __repr__(self):
        return f"Tweet('{self.id}', '{self.content}')"


class TwitterScrapper:
    def __init__(self):
        auth = tweepy.OAuthHandler(
            "x7DvILXws4xwZRNVMToNp5tje", "nDL7SqsrZACzKTaIA3Ve4qNtTG5KcLAIXIridvPzFy27pBDSCK")
        auth.set_access_token('1603988101-qcdF7E3RPHBxh2Acukidtd2ofxIRyWFxW7bwM2g',
                              'Dfn9uUua9tZye2YZ1xF1XUVdCwve10IFpfvTqp7k9gWvH')
        self.api = tweepy.API(auth)

    # def getTweets(self, biz_id, csvFileName):
    def getTweets(self, biz_id):
        # # csvFile = open(csvFileName, 'w')
        # # csvFile.truncate()
        # # csvWriter = csv.writer(csvFile)
        keyword = Business.query.filter_by(id=biz_id)[0].keywords
        # for tweet in tweepy.Cursor(self.api.search, q="#RateKonnect", count=100, lang="en", since="2017-04-03").items():

        #     print(tweet)

        for tweet in tweepy.Cursor(self.api.search, q="#RateKonnect", count=100, lang="en", since="2017-04-03").items():
            if keyword in tweet.text:
                try:
                    db.session.rollback()
                    usedIds = [i.id for i in Tweet.query.all()]
                    if tweet.id not in usedIds:
                        db.session.add(Tweet(id=tweet.id, name=tweet.user.screen_name,
                                             date_posted=tweet.created_at, content=tweet.text, business_id=biz_id))
                        db.session.commit()
                except:
                    print("error")
                b = 2
        # a = 2
        # return True


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:/bb//mydb.db'

@app.route('/allBusiness', methods=['GET'])
def allBusiness():
    data = []
    a = {
        "name": "",
        "rating": "",
        "address": "",
        "tweets": []
    }
    for i in Business.query.all():
        a = {}
        a["name"] = i.name
        a["rating"] = i.rating
        a["address"] = i.address
        a["tweets"] = []
        for b in i.tweets:
            a["tweets"].append([b.content, b.name])
        data.append(a)
    # return jsonify(users=[i.name for i in Business.query.all()])
    return jsonify(data)


@app.route('/addTweets', methods=['GET'])
def addTweet():
    a = TwitterScrapper()
    for i in Business.query.all():
        a.getTweets(i.id)

    b = TweetAnalyzer()
    for i in Business.query.all():
        b.sentimentAnalyzer(i.id)

    return jsonify(tweets=[i.content for i in Tweet.query.all()])


@app.route('/addBusiness', methods=['POST'])
def addBusiness():
    name = request.json['name']
    rating = request.json['rating']
    address = request.json['address']
    keyword = request.json['keyword']
    business = Business(name=name, rating=rating,
                        address=address, keywords=keyword)
    db.session.add(business)
    db.session.commit()
    return jsonify(users=[i.name for i in Business.query.all()])


@app.route('/removeBusiness', methods=['POST'])
def removeBusiness():
    name = request.json['name']
    a = Business.query.filter_by(name=name).delete()
    print(a)
    # a.execute()
    db.session.commit()
    return jsonify(users=[i.name for i in Business.query.all()])


app.run()
# @app.route('/', methods=['GET'])
# def home():
#     db.session()

#     return

# @app.route('/stuff', methods=['GET'])
# def home():
#     return jsonify(["<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"])


# @app.route('/books', methods=['GET'])
# def all_books():
#     var = name
#     #open csv file
#     #seacrh csv for name
#     list = []

#     return jsonify(db.User.query.all())


# @app.route('/api/v1/resources/books/all', methods=['GET'])
# def api_all():
#     conn = sqlite3.connect('books.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()
#     all_books = cur.execute('SELECT * FROM books;').fetchall()
#     return jsonify(all_books)


# @app.errorhandler(404)
# def page_not_found(e):
#     return "<h1>404</h1><p>The resource could not be found.</p>", 404

# '''
# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_id():
#     # Check if an ID was provided as part of the URL.
#     # If ID is provided, assign it to a variable.
#     # If no ID is provided, display an error in the browser.
#     print (request.args)
#     if 'id' in request.args:
#         id = int(request.args['id'])
#     else:
#         return "Error: No id field provided. Please specify an id."

#     # Create an empty list for our results
#     results = []

#     # Loop through the data and match results that fit the requested ID.
#     # IDs are unique, but other fields might return many results
#     for book in books:
#         if book['id'] == id:
#             results.append(book)

#     # Use the jsonify function from Flask to convert our list of
#     # Python dictionaries to the JSON format.
#     return jsonify(results)
# '''

# @app.route('/api/v1/resources/books', methods=['GET'])
# def api_filter():
#     query_parameters = request.args

#     id = query_parameters.get('id')
#     published = query_parameters.get('published')
#     author = query_parameters.get('author')

#     query = "SELECT * FROM books WHERE"
#     to_filter = []

#     if id:
#         query += ' id=? AND'
#         to_filter.append(id)
#     if published:
#         query += ' published=? AND'
#         to_filter.append(published)
#     if author:
#         query += ' author=? AND'
#         to_filter.append(author)
#     if not (id or published or author):
#         return page_not_found(404)

#     query = query[:-4] + ';'

#     conn = sqlite3.connect('books.db')
#     conn.row_factory = dict_factory
#     cur = conn.cursor()

#     results = cur.execute(query, to_filter).fetchall()

#     return jsonify(results)
