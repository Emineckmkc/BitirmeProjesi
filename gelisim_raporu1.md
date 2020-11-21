# BitirmeProjesi
# TÜRKÇE METİNLERDEN DUYGU ANALİZİ

### PROJE ÖZETİ
Bitirme projesinde, Türkçe kelimelerden duygu kütüphanesi oluşturularak, Türkçe metinlerden duygu analizi çalışmalarına katkı sağlamak amaçlanmıştır.
İnsan davranışları, düşünceleri sonucu ortaya çıkan aktivitelerdir. Düşünce kavramı ise insanın bir şahıs, marka, siyasi görüş hakkında veya değerlendirme için düşünme sonucu ulaşılan, düşünmenin ürünü olan görüştür. Düşünceler, duygu içerikli kelimeler barındırır. Bu kelimeler pozitif ya da negatif düşünce belirtmek için kullanılır. Artan verinin internet ile dijital ortama aktarılarak hızla depolanması,büyümesi sayesinde bu büyük veriden ihtiyaç dahilinde anlamlı bilgiler çıkarabilmek günümüzde en popüler konulardan birisidir. Duygu Analizi, bir metnin içerdiği duyguyu keşfedip analiz etme sanatıdır. Bu projede Türkçe tweet paylaşan kullanıcılarının seçilen etiket hakkında atılan tweetleri toplanarak, tweet metnin içerdiği duygu, duygu analizi çalışmasıyla pozitif veya negatif olarak gruplandırılacaktır. Etiket seçimi; Sağlık Bakanlığı'nın pandemi sürecini nasıl yönettiği hakkında Türkçe tweet paylaşan kullanıcıların yorumları olarak belirlenmiştir. (Geçmiş tweetleri toplamak biraz zor parayla satın almak gerekiyor dolayısıyla konu değişebilir). Bu sürecin nasıl yönetildiği hakkında atılan tweetler toplanacak, insanların bu sürecin nasıl yönetildiği hakkındaki görüşlerinin negatif veya pozitif duygu içerikli olma durumları analiz edilecekir. Pandemi süreci insanlar üzerinde derin bir etki yarattı. Somut olarak bu konuyla ilgili insanların görüşlerini bir araya getirmek, bunları analiz etmek değerli olacaktır. 

### PROJE ARKA PLANI
Daha önce birçok kişi Türkçe Metinlerden Duygu Analizi çalışmaları yapmıştır. Bu projeye benzer olan; 2018 yılında BAHÇEŞEHİR ÜNİVERSİTESİ, FEN BİLİMLERİ ENSTİTÜSÜ
MÜHENDİSLİK YÖNETİMİ Bölümü, "Sema YILDIRIM" isimli yüksek lisans öğrencisinin projesidir. Aynı şekilde twitter üzerinden belirli etiketler seçilerek bu etiketler hakkında atılan tweet metinleri toplanarak, Türkçe metinler üzerinden duygu analizi çalışmaları yapılmıştır. Hava değişikliğinin kullanıcılar üzerinde etkisi analiz edilmiş, kış aylarında genelde olumsuz, bahar ve yaz aylarında olumlu paylaşım yaptıkları sonucu çıkarılmıştır. Haftanın günlerine göre insanların hangi duygu yüklü oldukları keşfedilmiştir. Genelde pazartesi günleri olumsuz, çarşamba günleri nötr, hafta sonları ise olumlu duygular içerdikleri sonucuna ulaşılmıştır. Analiz çalışmalarında Türkçe metinler haricinde emojilerde kullanılmıştır. Yapılacak projede emojiler kullanılmayacaktır.

### KULLANILACAK TEKNOLOJİLER
Günümüzde en çok duygu içerikli paylaşımlar içeren platform sosyal medyadır. Bu çalışmada Twitter platformu kullanılacaktır.Türkçe esnek bir dildir ve Twitterda çok fazla krili veri vardır. Temiz veriler elde edebilmek için uzun bir süre Twitter Api'si kullanılarak veriler çekilecektir. Gruplama yöntemleri kullanılacaktır. Kelime yakalama yöntemi; metin sözcüklere göre gruplanacaktır.Metinden dökümandan ya da belgeden özellik çıkartmak için  kelimeler arasındaki uzaklık durumlarını vektörel olarak bulmamıza yarayan algoritma Word2Vec kullanılacaktır. Türkçe cümle parser(ayrıştırıcı) için Zemberek Parser kullanılacaktır. Bu çalışma kapsamında Pyhton programlama dili kullanılacaktır. Veritabanı olarak, SQLite kullanılacaktır. SQLite herhangi bir yazılım veya sunucu gerektirmez, pythonda veritabanı işlemleri için kullanılabilecek bir alternatiftir. NLP bilgileri için Kemal Oflazer'in Turkish Natural Language Processing kitabı kullanılacaktır.

### İŞ BÖLÜMÜ PLANLAMA

![ISBOLUMPLANI-1](https://user-images.githubusercontent.com/55896383/99884269-f598ef80-2c3d-11eb-9a37-ea1cece8e122.jpg)
![ISBOLUMPLANI-2](https://user-images.githubusercontent.com/55896383/99884271-f6ca1c80-2c3d-11eb-8b66-0dcbabf9e38e.jpg)

### Hedeflenen Çıktılar

Öncelikle ilk amaçlanan hedef; Twitterdaki verilere en hızlı sorunsuz erişim sağlamak ve toplanan verilerden temiz veriler elde etmektir. Yüklenen verilerden gereksiz bölümler çıkarıldıktan sonra geriye kalan kelimeler,var olan kayıtlara göre pozitif veya negatif duygu içerikli olmak üzere gruplandırılması hedeflenmiştir.Kişilerin  duygularına göre kullandığı kelimeler; güzel, harika, mükemmel gibi kelimeler pozitif duygu içerek kelimelerdir. Kötü, zayıf, korkunç ise negatif duygu içeren kelimelerdir. Kodlamalar için Windows işletim sistemi kullanılacaktır. Projenin olmazsa olmazı; Türkçe bir mentin içerdiği duygunun doğru keşfedilmesidir.Yapılacak çalışmada, tweet metninin içerdiği duyguyu doğru keşfetmek amaçlanmıştır.



