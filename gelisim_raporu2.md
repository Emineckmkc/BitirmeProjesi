# TÜRKÇE METİNLERDEN DUYGU ANALİZİ
### DÜZELTMELER - İŞ PLANI

![isplani](https://user-images.githubusercontent.com/55896383/103463778-12960780-4d40-11eb-8c8e-e02ff1ce7fca.jpeg)

### KAYNAKLAR
- Yıldırım,  S.,  Salman,  Y.  B. & Ayvaz,  S. (2019). Türkçe  Duygu  Kütüphanesi  Geliştirme:  Sosyal  Medya Verileriyle Duygu Analizi Çalışması. Avrupa Bilim ve Teknoloji Dergisi, (16), 51-60.  

- Tweepy. Tweepy. Web. 01 Aralık 2020.
- Oflazer, Kemal, Saraçlar, Murat. Turkish Natural Language Processing. Springer,2018
- "COVID-19 SÜRECİNDE TWITTER MESAJLARININ DUYGU ANALİZİ". Researchgate. Web. 11 Aralık 2020
- KELİME GÖSTERİLİMLERİ. Maliayas. Web. 24.11.2020

### ZORLUKLAR
Belirli parametreler vererek filtrelenebilen (örn, 'korona'), sonrasında bu filtrelenmiş tweetleri sürekli olarak alabilen bir apiye ihtiyaç duyuldu. Twitter'ın resmi  api'lerini kullanarak ücretsiz veri toplamak mümkündür. Twitterın bu amaçla sunduğu iki adet hizmet bulunmaktadır. Rest Api; twittera istekde bulunulur,cevap hazır olduğunda döner.Aynı istek tekrar sorulmak istendiğinde istek tekrar hazırlanır. Stream Api; hazırlanan istek twitter'ın sorgu havuzuna kaydedilir. Cevaba uygun bir durum olduğunda direkt cevap döner. Bağlantı kapanmadığı için tekrar bağlanma maliyetine bağlı gecikmeler yaşanmaz. Python ile twitterdan veri çekmek için tweepy kütüphanesi kullanıldı.Tweepy, pythonun twitter platformu ile iletişim kurmasını sağlayan açık kaynaklı bir kütüphanedir. Tweepy ve twitter'ın apisini kullanmanın bazı sorunları var. Arama apisinin en büyük dezavantajlarından biri son yedi gün içinde yazılmış tweetlere erişebilmektir. Bitirme tezi için çalışılacak konu sağlık bakanlığının pandemi sürecini nasıl yönettiği ile ilgili atılan tweet metinlerinden duygu analizi yapmaktı, fakat 2020 mart ayından itibaren olan eski verilere erişmek son 7 gün kısıtlaması yüzünden büyük bir darboğaz oluşturdu. Geçmiş verilere erişmek biraz maliyetli, dolayısıyla tweepy kullanarak 03 Aralık 2020 tarihinde 'korona' etiketli tweet metinleri toplanmaya başlandı. Tweetlerle ilgili metodlarda bir Tweet JSON dönecektir.Status nesnesi nesnelerin yapısını ve bazı özniteliklerini gösterir. Durum nesnesindeki özniteliklerin listesi içinden tweetin oluşturulma tarihi, retweet sayısı ve tweet metni kullanıldı.CSV dosyasına kaydederken Türkçe karakter sorunu ile karşılaşıldı. İki kez (utf * 8)
kullanıldığı halde dosyaya Türkçe karakterler kaydedilirken sorun yaşandı. Tweepy ile Türkçe Tweetleri kaydederken tek bir kez (utf * 8) kullanılmasıyla sorun çözüldü.

![1](https://user-images.githubusercontent.com/55896383/103465566-09139c00-4d4e-11eb-9f4e-f8bb8b577aac.PNG)

Veriler çekilirken günde üç defa belirli aralıklarla çekiliyordu. Dolayısıyla veriler çekilirken ortada zaman kavramı yoktu. Verileri kayıt yaparken verilen başlangıç tairihi ile bitiş tarihi arasındaki tweetler çekildi. Bu sayede yedi gün içindeki tüm tweetler programın haftada bir kez çalıştırılmasıyla toplandı.
Tweepy api kullanarak tweet çekme işlemlerinde, çok karakterleri tweetler çekilemiyordu. Çünkü twitter apisi 140 karakterden sonra kesiliyor. Genişletilmiş modu kullanıldı. Ama yinede sorun devam etti genişletilmiş modunda sınırı var, 280 karakterden sonra kesiliyor. Bu sorun, eğer tweet metnin boyutu 280 karakterden daha fazla ise gelen tweet metninin ilk 280 karakterini ve sonraki karakterleri birleştirilerek çözüldü.

