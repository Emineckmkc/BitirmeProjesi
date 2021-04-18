# BitirmeProjesi
# DÜZELTMELER
## Veriseti Hazırlama :

Twitter API'si kullanılarak python ile toplanan veriler , etiketlenirken sürekli tekrarlayan tweetler olduğu farkedildi. Tüm tweet metinleri bir dizide tutuldu. Yeni gelen tweet metni bu dizinin içinde yok ise csv dosyasına kaydedildi.
 
## Veri Ön İşleme :

Toplanan veriler içinde; tutarsız, tekrarlayan ve eksik veriler mevcut. Daha iyi sonuçlar elde edebilmek için veri ön işleme yapıldı. İnsan dili verileriyle çalışmak için Python programlama dili ile yazılmış, doğal dil işlemenin bir kütüphanesi olan NLTK kullanıldı. Ön işlemenin en önemli parçalarından biri, işe yaramaz verileri filterelemektir. Doğal dil işlemede, anlamsız sözcükler durdurma sözcükleri olarak adlandırılır. NLTK kütüphanesinde Türkçe 53 tane durdurma sözcüğü mevcuttur. Toplanan veriseti içinde durdurma szöcükleri çıkarıldı. Noktalama işaretleri kaldırıldı. Hastag,url,simge, emojiler, semboller vb. karakterlerin anlamı yoktur dolayısıyla bunlar silindi.

## Verileri Etiketleme :
Veriler manuel olarak etiketlendi.
negatif:(*n)
positif *p, 
NotePad++,  adından da anlaşılacağı gibi düzenleme konusunda gelişmiş özelliklere sahip bir programdır. 
