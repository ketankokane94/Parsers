
import tweepy
import csv

#Variables that contains the user credentials to access Twitter API 
access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

#use variables to access twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#This is a basic listener that just prints received tweets to stdout.
class CustomStreamListener(tweepy.StreamListener):        
    def on_status(self, status):
        print(status.text)
        with open('tweets.csv','a') as f:   
            writer=csv.writer(f)
            writer.writerow([status.author.screen_name,  status.text])
        return True
    
    def on_error(self, status_code):
        print(status_code)
        return True

    def on_timeout(self):
        return True
        
streamingAPI = tweepy.streaming.Stream(auth, CustomStreamListener())
streamingAPI.filter(track=['BNP','Paribas'])