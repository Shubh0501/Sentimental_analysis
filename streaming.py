import tweepy
import json
import csv
import urllib

# Authentication details. 
consumer_key = "LCah7GfN6Jncjak2skDX4xYY5"
consumer_secret = "A2N8QOlfcY7VIkTYJCMAMzz3VnKhwDGW40T6UaScutqBSCLmXh"
access_token = "873157993566810112-4qGuQQZf8Toz9fkNYogJHk2wvwHSzY5"
access_token_secret = "Lkb92LyjlwPkAY8vsa4TmwbuZj4TWZLwzb2Fx6JYWSPoo"

accountvar = raw_input("Enter the hashtag to be searched : ")  #Search query goes here

outputfilecsv = accountvar+"_stream.csv"
fc = csv.writer(open(outputfilecsv, 'wb'))
fc.writerow(["created_at","screen_name","tweet_text","time_zone"])

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Twitter returns data in JSON format - we need to decode it first
        
        decoded = json.loads(data)
        try:
            print decoded['entities']['media'][0]['media_url']
    
                       
                        
        except (NameError, KeyError,AttributeError):
                        #we dont want to have any entries without the media_url so lets do nothing
             pass
        
        print '%s @%s: %s %s\n' % (decoded['created_at'],decoded['user']['screen_name'],decoded['text'].encode('ascii', 'ignore'),decoded['user']['time_zone'])
        fc.writerow([decoded['created_at'],decoded['user']['screen_name'],decoded['text'].encode('ascii', 'ignore'),decoded['user']['time_zone']])      

         #got media_url - means add it to the output
        
        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print "Showing all new tweets for %s"%accountvar

   
    stream = tweepy.Stream(auth, l)
    stream.filter(track=[accountvar])
