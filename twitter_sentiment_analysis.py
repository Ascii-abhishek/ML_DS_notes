import tweepy
from textblob import TextBlob

consumer_key = '8AEcBo5RG7sb7SpjLd5SjtRQO'
consumer_secret = 'flOpBmwoHoA2OKUJiCufToRAfs5WTDCuNh253iyvUnKeuXkfEu'

access_token = '2810602080-hftgtoOP7WPKBuTSU9zlIdwZGPW4UoPWBTZW8nG'
access_token_secret = 'I06GMAHVtp3LNNPIPPYCIudAD0bE6ceL9R8ssppIu4qXL'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment, end='\n\n')
