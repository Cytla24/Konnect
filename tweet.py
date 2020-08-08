import tweepy
import csv
from Database import db, Tweet, Business

class TwitterScrapper:
    def __init__(self):
        auth = tweepy.OAuthHandler("x7DvILXws4xwZRNVMToNp5tje", "nDL7SqsrZACzKTaIA3Ve4qNtTG5KcLAIXIridvPzFy27pBDSCK")
        auth.set_access_token('1603988101-qcdF7E3RPHBxh2Acukidtd2ofxIRyWFxW7bwM2g',
                              'Dfn9uUua9tZye2YZ1xF1XUVdCwve10IFpfvTqp7k9gWvH')
        self.api = tweepy.API(auth)

    # def getTweets(self, biz_id, csvFileName):
    def getTweets(self, biz_id):
        # csvFile = open(csvFileName, 'w')
        # csvFile.truncate()
        # csvWriter = csv.writer(csvFile)
        
        keyword = Business.query.filter_by(id=biz_id).keywords
        
        for tweet in tweepy.Cursor(self.api.search, q="#RateKonnect", count=100, lang="en", since="2017-04-03").items():
            if keyword in tweet:
                db.session.add(Tweet(id=tweet.id, name=tweet.user.screen_name, date_posted=tweet.created_at, content=tweet.text, business_id=biz
                                     _id))
       
