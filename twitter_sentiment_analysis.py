import tweepy
from textblob import TextBlob

# Twitter api Authentication keys 
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#funtion to set negative/positive labels
def pol_label(ana,threshold = 0):
	if ana.sentiment[0]>threshold:
		return "Positive"
	else:
		return "negative"


# tweet search
public_tweets = api.search('airindia')

# writing to csv file
with open("tweets.csv",'wb') as csv_file:
		csv_file.write('tweet,sentiment_label\n')
		for tweet in public_tweets:

			analysis = TextBlob(tweet.text)
			csv_file.write('%s,%s\n'%(tweet.text.encode('utf8'),pol_label(analysis)))