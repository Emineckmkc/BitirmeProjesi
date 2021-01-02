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

csvFile = open('korona13.csv', 'a', encoding='utf-8')
csvWriter = csv.writer(csvFile)

startsince = '2020-12-13'
endUntil = '2020-12-15'
b=1



for status in tweepy.Cursor(api.search,
                 q="korona",                
                 since =startsince, until=endUntil,languages='Turkish',
                 tweet_mode='extended').items(99999):
            b+=1
            print(b)
            print ("Text:", status.full_text)
            csvWriter.writerow([status.created_at ,status.retweet_count, status.full_text])
                 
csvFile.close()
       


        
