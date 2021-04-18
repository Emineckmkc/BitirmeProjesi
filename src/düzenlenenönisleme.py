# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 17:26:07 2021

@author: Emine
"""

# -*- coding: utf-8 -*-

import re
re.compile('<title>(.*)</title>')
import string
import csv
from nltk.corpus import stopwords
stopWords = set(stopwords.words('turkish'))

#yeni dosyaya kayit
csvFile = open('korona20.csv', 'a', encoding='utf-8')
csvWriter = csv.writer(csvFile)

#emoji,hastag,url kaldir.

def text_cleanup(text):
    text = re.sub('&amp','&', text) 
    text = re.sub('['+string.punctuation+']','',text) 
    text = re.sub(r'http\S+','',text)
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F" 
        u"\U0001F300-\U0001F5FF" 
        u"\U0001F680-\U0001F6FF"  
        u"\U0001F1E0-\U0001F1FF"   
                           "]+", flags=re.UNICODE)
    text = re.sub(emoji_pattern,'',text)
     
    return [word.lower() for word in text if word not in stopWords]
data=[]
with open('Şubat3-5.csv',newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:  
        if(row.__len__()==3):
           data.append(row[2]) 
           
    for x in data:  
  
       text= str.join('',text_cleanup(x))
       print(text+",")
       csvWriter.writerow([text])
  