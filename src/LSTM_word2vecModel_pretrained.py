# -*- coding: utf-8 -*-
"""
@author: Emine
"""
from keras.models import Sequential
from keras.layers.core import Dense
from keras.layers.embeddings import Embedding
from keras.layers.core import Dropout
from keras.layers import Flatten

#csv 
import csv

#numpy
import numpy as np
#matplotlib
import matplotlib.pyplot as plt
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
         #liste türünde gelen cümleyi stringe çevir.
         strcumle= row[0]
         #String halinde olan cümleyi kelime keliime parçala.
         kelimeler= strcumle.split()
         #son kelimeye(*n, *p ,*nt yani etiketler) kadar olanları al.
         metin= kelimeler[0:-1]
         #satırın son kelimesini etiketlere ekle
         etiketler.append(kelimeler[-1])

        #durak kelimeleri kontrol et, varsa kaldır
         temp = []
         for w in metin:
            if w not in stopWords:
             temp.append(w)
         cumleler.append(temp)


#Etiketleri sayılara dönüştür.
le = LabelEncoder()
etiketler = le.fit_transform(etiketler)


# indirilen hazır word2vec ile eğitilmiş modeli yükle.
from gensim.models import KeyedVectors
w2vModel = KeyedVectors.load_word2vec_format('trmodel', binary=True)

#metinlerde en çok geçen 30 kelimenin işleme alınmasını sağlayalım
num_max = 30
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


embedding_layer = Embedding(input_dim=w2vModel.wv.syn0.shape[0], 
                            output_dim=w2vModel.wv.syn0.shape[1], 
                            weights=[w2vModel.wv.syn0],
                            input_length=maxlentweet)

print('Embedding_layer input_dim: ',str(w2vModel.wv.syn0.shape[0]))
print('Embedding_layer output_dim: ',str(w2vModel.wv.syn0.shape[1]))
print('Embedding_layer input_length: ',str(X.shape[1]))

lstm_out = 22
num_classes = 3

model = Sequential()
model.add(embedding_layer)
model.add(LSTM(units=lstm_out,recurrent_dropout=0.5))
model.add(Flatten())
model.add(Dense(num_classes, activation='softmax'))
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model.summary())


#split dataset
X_train, X_test, Y_train, Y_test = train_test_split(X, etiketler, test_size=0.2, random_state=0)

#fit model
batch_size = 64
EPOCHS = 10
history=model.fit(X_train, Y_train, verbose=1,epochs= EPOCHS, batch_size=batch_size, validation_split = 0.1 )


score, acc = model.evaluate(X_test, Y_test, verbose = 1, batch_size=batch_size)
y_pred = model.predict(X_test)

scores = model.evaluate(X_test, Y_test, verbose=0)
print("Test Accuracy: %.2f%%" % (scores[1] * 100))

y_pred = model.predict(X_test, batch_size=batch_size, verbose=1)
y_pred2 = np.argmax(y_pred, axis=1)


print(classification_report(Y_test, y_pred2))

print('------------confusion_matrix-------------------')
print(confusion_matrix(Y_test, y_pred2, labels=[0, 1, 2]))

#--------------------------------Verisetini Örnekleme----------------------------

from imblearn.over_sampling import RandomOverSampler
rus = RandomOverSampler(random_state = 0,sampling_strategy='minority')

x_rus, y_rus = rus.fit_resample(X, etiketler)
x_train, x_test, y_train, y_test = train_test_split(x_rus, y_rus, test_size = 0.25, random_state = 42)


model2 = Sequential()
model2.add(embedding_layer)
model2.add(LSTM(units=lstm_out,dropout = 0.2,recurrent_dropout=0.5))
model2.add(Dense(num_classes, activation='softmax'))
model2.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
print(model2.summary())
history2 = model2.fit(x_train, y_train, validation_split=0.20, epochs=10,batch_size=64)

score, acc = model2.evaluate(x_test, y_test, verbose = 1, batch_size=64)
y_pred = model2.predict(x_test)

scores = model2.evaluate(x_test, y_test, verbose=0)
print("Test Accuracy: %.2f%%" % (scores[1] * 100))

y_pred = model2.predict(x_test, batch_size=64, verbose=1)
y_pred2 = np.argmax(y_pred, axis=1)


print(classification_report(y_test, y_pred2))

print('------------confusion_matrix-------------------')
print(confusion_matrix(y_test, y_pred2, labels=[0, 1, 2]))




plt.figure(figsize = (15,10))
plt.plot(history2.history['accuracy'])
plt.plot(history2.history['val_accuracy'])
plt.legend(['Train2', 'Test2','Train1', 'Test1'], loc='upper left')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')


