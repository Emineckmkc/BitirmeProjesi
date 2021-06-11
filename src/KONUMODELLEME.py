# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:54:13 2021

@author: Emine
"""
#verileri depolamak ve işlemek için kütüphaneler,görselleştirmek için kullanılan kütüphaneler
import pandas as pd
import matplotlib.pyplot as plt

#stop-words
from nltk.corpus import stopwords
#Burada nltk kütüphanesinde bulunan Türkçe stopword'leri bir değişkene atıyoruz.
stopWords = set(stopwords.words('turkish'))
import pyLDAvis
import pyLDAvis.sklearn

from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

#verinin tanımlanması
input_file = 'toplamexcel.csv'
data = pd.read_csv(input_file, delimiter=";", decimal=",")
data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
print('Toplam {} tweet'.format(len(data)))
print(data.columns)
data.head()

#veriye ön bakış
data.info()


#etiketlerin elde edilmesi
etiket_ = Counter(data['etiket']).keys()
print(etiket_)

#etiketlerin içerisindeki veri sayıları
sum_ = Counter(data['etiket']).values()
print(sum_)


#elde edilen etiketlerin ve içerdiği sayıları görselleştirmek için dataframe yapısına çeviriyoruz.
df = pd.DataFrame(zip(etiket_,sum_), columns = ['etiket', 'Toplam'])


#etiketlerin görselleştirilmesi - çubuk grafiği
df.plot(x = 'etiket' , y = 'Toplam',kind = 'bar', legend = False, grid = True, figsize = (15,5))
plt.title('Etiket Sayılarının Görselleştirilmesi', fontsize = 20)
plt.xlabel('Etiketler', fontsize = 15)
plt.ylabel('Toplam', fontsize = 15);
plt.show()

#etiketlerin görselleştirilmesi - pasta grafiği
fig, ax = plt.subplots(figsize=(15, 10))
ax.pie(df.Toplam, labels =df.etiket, autopct = '%1.1f%%',  startangle = 90 )
ax.axis('equal')
plt.show()

docs = data['tweet  ']
#stopword'leri kaldırıyoruz 
def temizle(values):
    filtered_words = [word for word in values.split() if word not in stopWords]
    not_stopword_doc = " ".join(filtered_words)
    return not_stopword_doc

docs = docs.map(lambda x: temizle(x))
data['tweet  '] = docs
print(data.head(20))


#vectorizer nesnesi, metni vektör formuna dönüştürmek için kullanılacaktır.
vectorizer = CountVectorizer(max_df=0.95, min_df=30)
#dönüşümü uygula
tf = vectorizer.fit_transform(data['tweet  '])
#matristeki her bir sütunun hangi kelimeyi temsil ettiğini söyler
tf_feature_names = vectorizer.get_feature_names()

from sklearn.decomposition import LatentDirichletAllocation

#modelin oluşturulması
model_lda = LatentDirichletAllocation(n_components=10,max_iter=5,random_state=0).fit(tf)

def SampiyonKelimeler(model_lda, feature_names, word):
    topic_kelimeler = {}
    for i, topic in enumerate(model_lda.components_):
         topic_kelimeler["Topic %d kelime" % (i)]= ['{}'.format(feature_names[i])
                        for i in topic.argsort()[:-word - 1:-1]]
         topic_kelimeler["Topic %d ağırlık" % (i)]= ['{:.1f}'.format(topic[i])
                        for i in topic.argsort()[:-word - 1:-1]]
    return pd.DataFrame(topic_kelimeler)

SampiyonKelimeler(model_lda, tf_feature_names, 10)


data = pyLDAvis.sklearn.prepare(model_lda, tf, vectorizer)
pyLDAvis.display(data)
