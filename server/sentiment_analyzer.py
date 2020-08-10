from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from database import db, Tweet, Business
import re


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
