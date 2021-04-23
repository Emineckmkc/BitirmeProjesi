# -*- coding: utf-8 -*-
"""
@author: Emine
"""
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.embeddings import Embedding
from keras.layers.core import Dropout

#csv 
import csv

#numpy
import numpy as np

#stop-words
from nltk.corpus import stopwords
stopWords = set(stopwords.words('turkish'))

#keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM

#sklearn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report


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
etiketler = le.fit_transform(etiketler)



from gensim.models import KeyedVectors
w2vModel = KeyedVectors.load_word2vec_format('trmodel', binary=True)

#metinlerde en çok geçen 10000 kelimenin işleme alınmasını sağlayalım
num_max =  10000
# tokinizer nesnesini oluştur
tk=Tokenizer(num_words=num_max)

# giriş verisine göre tokinizer sınıfının ayarlanması
tk.fit_on_texts(cumleler)
X = tk.texts_to_sequences(cumleler)

#Çoğu algoritma giriş verilerinin sabit uzunlukta olmasını bekler. 
#Bu durumlarda tokenizer’ın padding metodunu kullanırız.
# her bir giriş verisininin uzunluğu yalnızca 15 olsun
maxlentweet = 15
X = pad_sequences(X, maxlen=maxlentweet)


embedding_layer = Embedding(input_dim=w2vModel.wv.syn0.shape[0], 
                            output_dim=w2vModel.wv.syn0.shape[1], 
                            weights=[w2vModel.wv.syn0],
                            input_length=maxlentweet)


print('Embedding_layer input_dim: ',str(w2vModel.wv.syn0.shape[0]))
print('Embedding_layer output_dim: ',str(w2vModel.wv.syn0.shape[1]))
print('Embedding_layer input_length: ',str(X.shape[1]))

lstm_out = 20
num_classes = 3

model = Sequential()
model.add(embedding_layer)

model.add(LSTM(units=lstm_out,recurrent_dropout=0.1))
model.add(Dense(num_classes, activation='softmax'))


model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())


#split dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, etiketler, test_size=0.2, random_state=0)

#fit model
batch_size = 64
EPOCHS = 10
model.fit(X_train, Y_train, verbose=1,epochs= EPOCHS, batch_size=batch_size, validation_split = 0.1 )


score, acc = model.evaluate(X_test, Y_test, verbose = 2, batch_size=batch_size)
y_pred = model.predict(X_test)

scores = model.evaluate(X_test, Y_test, verbose=0)
print("Test Accuracy: %.2f%%" % (scores[1] * 100))

y_pred = model.predict(X_test, batch_size=5, verbose=1)
y_pred2 = np.argmax(y_pred, axis=1)


print(classification_report(Y_test, y_pred2))

print('------------confusion_matrix-------------------')
print(confusion_matrix(Y_test, y_pred2, labels=[0, 1, 2]))


