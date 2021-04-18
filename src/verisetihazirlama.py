
 #-*- coding:utf-8 -*-
import tweepy
import csv
import locale
locale.setlocale(locale.LC_ALL, "Turkish")
consumer_key = "vdRk3b1NYDyKktFscyxn5LlLy"
consumer_secret = "StQafrPKHedWOKz5j0Eb4EgL6gZ3o1tE6tw91dPxjI05cZYL2q"
access_token = "1072416826351599616-xPctnCFfAjS1zr2DplUGZEJef8X3eV"
access_token_secret = "SawkFaezzt0zRfH7MM8vEIo2jhplXIdiep5QMspeEkmLW"

try:
 auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
 auth.set_access_token(access_token, access_token_secret)
 api = tweepy.API(auth,wait_on_rate_limit=True)
except tweepy.TweepError:
 print ('Authentication Error')
 
csvFile = open('Nisan13.csv', 'a', encoding='utf-8')
csvWriter = csv.writer(csvFile)

startsince = '2021-04-13'
endUntil = '2021-04-14'

tweet_max_boyut = 280

total_tweets=[]

for status in tweepy.Cursor(api.search,
                 q="korona",                
                 since =startsince, until=endUntil,languages='Turkish',
                 tweet_mode='extended').items(99999):
     
             if len(status.full_text) > tweet_max_boyut:
                
                united_tweet = []
                cut = status.full_text[:tweet_max_boyut]     
                status.full_text = status.full_text[tweet_max_boyut:]
                united_tweet.append(cut+status.full_text)
               
                for x in united_tweet:
                    
                         if x not in total_tweets:
                          csvWriter.writerow([status.created_at ,status.retweet_count, x])
                          total_tweets.append(x)
                 
             else:
    
                 print ("Text:", status.full_text)
                 if status.full_text not in total_tweets:
                   csvWriter.writerow([status.created_at ,status.retweet_count, status.full_text])
                   total_tweets.append(status.full_text)
