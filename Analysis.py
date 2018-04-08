#python Sentimental Analysis

import csv
import tweepy
from textblob import TextBlob
import nltk

nltk.download('averaged_perceptron_tagger')
consumer_key = "LCah7GfN6Jncjak2skDX4xYY5"
consumer_secret = "A2N8QOlfcY7VIkTYJCMAMzz3VnKhwDGW40T6UaScutqBSCLmXh"
access_token = "873157993566810112-4qGuQQZf8Toz9fkNYogJHk2wvwHSzY5"
access_token_secret = "Lkb92LyjlwPkAY8vsa4TmwbuZj4TWZLwzb2Fx6JYWSPoo"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

savefile = csv.writer(open("animalrescuefiltered.csv", "w"))
savefile.writerow(["TWEETS", "SENTIMENTS ATTACHED"])


tweet_s = open("#animalrescue2.csv")

for tweet in tweet_s:
    
    analysis = TextBlob(tweet)
   # print(analysis.tags)
    
    #print(analysis.noun_phrases)
    print(analysis.sentiment)
    savefile.writerow([tweet, analysis.sentiment])
