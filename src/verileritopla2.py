

 #-*- coding:utf-8 -*-
import tweepy
import datetime
import csv
import locale
locale.setlocale(locale.LC_ALL, "Turkish")

consumer_key = "v82KsiNCel4vLMk7JD3m7QlwV"
consumer_secret = "qHKuzPkmrE8n1phVhnBqcdKOyRf6aADFcZmVF2iUceC9niNTwA"
access_token = "1072416826351599616-pkGKlU9nnjF3MDnpVQdpUutsIiBdBy"
access_token_secret = "9JHbOp5jod79sSFjuE4dyes3W40yxis8A75vMkIpRGuyi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

csvFile = open('korona312.csv', 'a', encoding='utf-8')
csvWriter = csv.writer(csvFile)


tweet_max_boyut = 280

startsince = '2020-12-28'
endUntil = '2021-01-2'


to_tweet = []

for status in tweepy.Cursor(api.search,
                 q="korona",                
                 since =startsince, until=endUntil,languages='Turkish',
                 tweet_mode='extended').items(99999):
    
     if len(status.full_text) > tweet_max_boyut:

         cut = status.full_text[:tweet_max_boyut]     
         status.full_text = status.full_text[tweet_max_boyut:]
         to_tweet.append(cut+status.full_text)
               
         for x in to_tweet:
               csvWriter.writerow([status.created_at ,status.retweet_count, x])
                 
     else:
    
         print ("Text:", status.full_text)
         csvWriter.writerow([status.created_at ,status.retweet_count, status.full_text])
                 
    
       

