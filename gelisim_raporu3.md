# TÜRKÇE METİNLERDEN DUYGU ANALİZİ

## DÜZELTMELER

### Veri Seti Hazırlama :

Twitter API'si kullanılarak python ile toplanan veriler , etiketlenirken sürekli tekrarlayan tweetler olduğu farkedildi. Tüm tweet metinleri bir dizide tutuldu. Yeni gelen tweet metni bu dizinin içinde yok ise csv dosyasına kaydedildi. Bu sayede benzersiz tweet metinleri elde edildi.
 
### Veri Ön İşleme :

Toplanan veriler içinde; tutarsız, tekrarlayan ve eksik veriler mevcut. Daha iyi sonuçlar elde edebilmek için veri ön işleme yapıldı. İnsan dili verileriyle çalışmak için Python programlama dili ile yazılmış, doğal dil işlemenin bir kütüphanesi olan NLTK kullanıldı. Ön işlemenin en önemli parçalarından biri, işe yaramaz verileri filterelemektir. Doğal dil işlemede, anlamsız sözcükler durdurma sözcükleri olarak adlandırılır. NLTK kütüphanesinde Türkçe 53 tane durdurma sözcüğü mevcuttur. Toplanan veriseti içinde durdurma sözcükleri çıkarıldı. Noktalama işaretleri kaldırıldı. Hastag,url,simge, emojiler, semboller vb. karakterlerin anlamı yoktur dolayısıyla bunlar silindi. Tüm harfler küçük harflere çevrildi. Bütün bunlara rağmen yine de çok fazla kirli veri (anlamsız kelimeler) vardı. Manuel olarak okunarak çıkarıldı.

### Verileri Etiketleme :

Ön işlemden geçen veriler  manuel olarak okunarak etiketlendi. Manuel olarak etiketlemenin çok zaman alıcı olması gibi zorluğu oldu. Verilerin olduğu csv dosyasında bazı satırlar boştu. Bunu düzeltmek için NotePad++ kullanıldı. Satır işlemlerinden boş satırlar kaldırıldı. 

### Metinlerin Vektöre Dönüştürülmesi :

Etiketli verilerin, vektöre dönüştürülmesi gerekir. Toplanan veri setini csv dosyasından okundu. 
<ol>
<li> Girdiler(X) : Cümleler, </li>
<li> Çıktı(Etiket)(Y) : Cümlenin sonundaki etiketler, </li> </ol>

şeklinde ayrıldı. Etiketler, Sckit-Learn kütüphanesinin parçalarından olan Label Encoding, ile metin verileri sayısala dönüştürüldü. Makine öğrenmesi yalnızca sayısal verileri kabul eder. Projede, kullanılmayacak kadar az eğitim verisi mevcut. Çözmek istenen problemle birlikte, kelime düğümlerini öğrenmek yerine önceden hesaplanmış bir gömme alanından yüklendi. Açık kaynaklı bir örnek olarak Türkçe dilinde yazılmış tüm wikipedia  makalelerinden eğitilmiş hazır bir model indirildi. Büyük metinleri belirli algoritmalar kullanarak uzaklık ve kelime anatolojisi tarafından oldukça başarılı olan Gensim kütüphanesinin KeyedVectors modülü ile indirilen eğitilmiş model pythona yüklendi. KeyedVectors modülünde; varlıklar ve vektörler arasında bir eşleşme söz konusudur. Cümlelerde en çok geçen kelimenin işleme alınmasını ile girdiler yani cümlelerdeki kelimeler tam sayılara çevrildi. Keras, genelde tüm bağımsız belgelerin aynı uzunlukta olmasını gerektirir. Fakat cümleler farklı uzunluktadır. Bu sorunu çözmek için, pad_sequences kullanıldı.
Kerasın sıralı katmanlarından oluşan Sequential modeli, LSTM (Uzun-kısa vadeli hafıza ağları) katmanı da eklenerek  model oluşturuldu. Keras, derin öğrenme modelinin metinsel özeti için bir yol sağlar. Derin öğrenme modelinin metinsel özeti yazdırıldı. Model oluştuktan sonra, veriler %80 eğitim verisi ve %20 test verisi olarak ayrıldı. Model, girdileri ve etiketleri verilerel fit edildi. Sadece X(Girdi) verilerek, Y(Etiket)  tahmin etmesi için predict yapıldı. Gerçek ve tahmin değerleri arasında yer alan ilişkiyi inceleyebilmek için scikit-learn kütüphanesinin classification_report metriği ve karmaşıklık matrisi kullanıldı. 

## KAYNAKLAR 

- FRANÇOIS, CHOLLET.Deep Learning with Python.f America, 2018
- Keras. keras.io. Web. 11 Mart 2021.
- akoksal-Turkish-Word2Vec. github. Web. 9.04.2021
- Word Embedding and Word2Vec.towardsdatascience.Web. 8.04.2021
- Word2vec. wikipedia. Web 3 Mart 2021.
- "COVID-19 SÜRECİNDE TWITTER MESAJLARININ DUYGU ANALİZİ". Researchgate. Web. 12 Mart 2021
- gensim.radimrehurek. Web. 18.03.2021

## ZORLUKLAR 
Öncelikle projede Derin öğrenme kütüphanesi kullanılırken, aktivasyon hatası ile karşılaşıldı.

![1](https://user-images.githubusercontent.com/55896383/115898572-600cc080-a466-11eb-9c8d-765e6d7dc51f.PNG)


<ol>
<li> from tensorflow.keras.layers import InputSpec </li>
<li> from keras import activations, initializers, regularizers, constraints </li> </ol> yazılarak sorun çözüldü.
Kelime düğümlerini öğrenmek için, cümleleri list olarak tutup,  Word2Vec'e cümleler verildi. Word2Vec girdi olarak list of list alıyor. Girdi, çıktı ve gizli katmandan oluşan bu yapay sinir ağında kelime vektörlerini oluştururken, pencere genişliği ve gömme boyutu gibi hiper parametreler kullanıldı.Pencere genişliği hedef kelimenin sağında ve solunda  kaç kelime olması gerektiğibi belirtirken, gömme boyutu gizli katmandaki nören sayıyısına denk geliyor. Model oluşturuldu, fakat veri az olduğu için başarılı sonuçlar elde edilmedi.


![2](https://user-images.githubusercontent.com/55896383/115910580-ad445e80-a475-11eb-8087-4d8c2eb95535.PNG)


Bunun yerine, vektörler bir KeyedVector örneği olarak ; açık kaynaklı olarak Türkçe dilinde yazılmış tüm wikipedia makalelerinden eğitilmiş bir model indirilerek, kodla pythona yüklendi.


![3](https://user-images.githubusercontent.com/55896383/115911731-1d9faf80-a477-11eb-8834-81ddb9fb802d.PNG)

Kelime gömme, aynı anlama sahip elimelerin benzer bir gösterime sahip olduğu metin için öğrenilmiş bir temsildir. Üç tane parametre ile oluşturuldu.
<ol>
<li>input_dim: Sözlüğün uzunluğudur. 
<li>output_dim: Gömmek istediğimiz boyutların sayısıdır.Her kelime için vektör uzunluğudur.
<li> input_length: Maximum belgenin uzunluğudur. </ol>

![4](https://user-images.githubusercontent.com/55896383/115913077-cf8bab80-a478-11eb-84d2-e0124fbf8ba3.PNG)

![5](https://user-images.githubusercontent.com/55896383/115913329-22fdf980-a479-11eb-8d4e-cfcde2bede18.PNG)

Modeli eğitirken, tüm veri setini 10 sefer yenileniyor. Ve her 64 örnekte bir adım atılıyor.

![image](https://user-images.githubusercontent.com/55896383/115913745-a9b2d680-a479-11eb-8210-eaef606e82e7.png)


Train ve test split yaklaşımında modelde kullanılacak veri seti train ve test seti olarak ikiye ayrılıyor. %80 train, %20 test. Train seti üzerinden model kuruluyor ve test seti üzerinden modelin performansı değerlendiriyor. Veri setinde bir sınıf diğerinden fazla ise aşırı öğrenme oluyor. Projede amaç, mümkün olduğunca doğru şekilde modelin performansını değerlendirmek. Dolayısıyla bu noktada train ve test spit yaklaşımı eksik kalıyor. İlerlyen çalışmalarda k-fold kullanılacaktır.



 
 







## ARAÇLAR 
Doğal dil işleme kütüphanesi olan NLTK kullanıldı.Kelimeleri vektör uzayında ifade etmeye çalışan danışmansız ve tahmin temelli bir model olan Wor2vec kullanıldı. Metin madenciliği kelimeler arasında uzaklık durumunu vektörel olarak bulmamıza yarayan algoritmalar bütünüdür. Metin madenciği konusunda oldukça yetenekli ve performanslı, doğal dil işleme için açık kaynaklı bir kütüphane olan Gensim kütüphanesi kullanıldı. Modelleri tanımlamayı ve eğitmeyi çok kolay hale getiren Derin öğrenme kütüphanesi Keras kullanıldı. Veri bilimi ve makine öğrenmesi için en yaygın kullanılan Python paketlerinden Scikit-learn kullanıldı.
