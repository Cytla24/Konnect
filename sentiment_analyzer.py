from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from database import db, Tweet, Business
import re


class TweetAnalyzer(): # Function to clean tweets and remove
    def __init__(self):
        pass

    def cleanTweet(self, intweet):
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", intweet).split())

    def sentimentAnalyzer(self, businessID):
		analysis = SentimentIntensityAnalyzer()

		cur_tweets = Business.query.filter_by(id=businessID).tweets
		frating = 0
		count = 0

		for tweet in cur_tweets:
			vs = analysis.polarity_scores(tweet)
			crating = (vs['compound'] + 1) * 5/2
			frating += crating
			count += 1
		return frating/count
