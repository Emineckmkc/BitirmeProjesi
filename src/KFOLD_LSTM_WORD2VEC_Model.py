# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 13:38:02 2021

@author: Emine
"""
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

#csv 
import csv

# data visualisation and manipulation
import numpy as np

from matplotlib import pyplot as plt
#stop-words
from nltk.corpus import stopwords
stopWords = set(stopwords.words('turkish'))

#keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.embeddings import Embedding


#sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.model_selection import StratifiedKFold


cumleler=[]
etiketler=[]
temp=[]

#reading file 
with open('TOPLAM.csv',newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:

         str2= row[0]
         str3= str2.split()
         str4= str3[0:-1]
         #add the last word of the line to the tags
         etiketler.append(str3[-1])

         #check the stop words, remove if any
         temp = []
         for w in str4:
            if w not in stopWords:      
             temp.append(w)
         cumleler.append(temp)


 #Convert labels to numbers
le = LabelEncoder()
Y = le.fit_transform(etiketler)



from gensim.models import KeyedVectors
w2vModel = KeyedVectors.load_word2vec_format('trmodel', binary=True)

#metinlerde en çok geçen  kelimenin işleme alınmasını sağlayalım
num_max =  30
# tokinizer nesnesini oluştur
tk=Tokenizer(num_words=num_max)

# giriş verisine göre tokinizer sınıfının ayarlanması
tk.fit_on_texts(cumleler)
X = tk.texts_to_sequences(cumleler)

#Çoğu algoritma giriş verilerinin sabit uzunlukta olmasını bekler. 
#Bu durumlarda tokenizer’ın padding metodunu kullanırız.
# her bir giriş verisininin uzunluğu yalnızca 15 olsun
maxlentweet = 22
X = pad_sequences(X, maxlen=maxlentweet)

#create a embedding layer using Google pre triained word2vec (50000 words)
#The Embedding layer takes at least two arguments: the number of possible tokens (here, 1,000: 1 + maximum word index)
# and the dimensionality of the embeddings (here, 64).

lstm_out = 22
num_classes = 3
batch_size = 64 
EPOCHS = 10
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=0)
cvscores = []
for train, test in kfold.split(X, Y):
    embedding_layer = Embedding(input_dim=w2vModel.wv.syn0.shape[0], 
                            output_dim=w2vModel.wv.syn0.shape[1], 
                            weights=[w2vModel.wv.syn0],
                            input_length=maxlentweet)


    print('Embedding_layer input_dim: ',str(w2vModel.wv.syn0.shape[0]))
    print('Embedding_layer output_dim: ',str(w2vModel.wv.syn0.shape[1]))
    print('Embedding_layer input_length: ',str(X.shape[1]))

    # create model
    model = Sequential()
    model.add(embedding_layer)
    model.add(LSTM(units=lstm_out,recurrent_dropout=0.5))
    model.add(Dense(num_classes, activation='softmax'))
  #  model.add(Dropout(0.5))
    # Compile model
    model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    # Fit the model
    model.fit(X[train], Y[train], verbose=1,epochs= EPOCHS, batch_size=batch_size )
    # evaluate the model
    scores = model.evaluate(X[test], Y[test], verbose=0)
    print("Test Accuracy: %.2f%%" % (scores[1] * 100))
    cvscores.append(scores[1] * 100)
print("%.2f%% (+/- %.2f%%)" % (np.mean(cvscores), np.std(cvscores)))


plt.figure(figsize=(15,10))

plt.plot((scores[1] * 100)) 

plt.title("Test Accuracy")

plt.ylabel('Accuracy')
plt.xlabel('Epoch')

plt.show()
