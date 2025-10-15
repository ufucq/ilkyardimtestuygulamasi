# --- DATA ---
tests = {
        "Test 1": {
            "questions": [
                {
                    "question": "1. Olay yerinde, hasta/yaralının hayatının kurtarılması veya durumunun daha da kötüleşmesini engellemek amacıyla ilaçsız olarak yapılan müdahaleye ne denir?",
                    "options": ["A. Acil tedavi", "B. Acil müdahale", "C. İlkyardım", "D. Temel yaşam desteği"],
                    "answer": "C. İlkyardım",
                    "explanation": "'İlkyardım', olay yerinde, tıbbi yardım gelene kadar hayatı kurtarmak veya durumun daha da kötüleşmesini önlemek için yapılan ilaçsız uygulamalardır.",
                    "wrong_explanations": {
                        "A. Acil tedavi": "Acil tedavi, sağlık profesyonelleri tarafından hastane veya ambulans gibi ortamlarda ilaç ve tıbbi ekipman kullanılarak yapılan müdahaledir.",
                        "B. Acil müdahale": "Acil müdahale, genellikle profesyonel ekiplerin yaptığı daha kapsamlı bir müdahaledir ve ilk yardımı da içerebilir, ancak ilk yardımın kendisi değildir.",
                        "D. Temel yaşam desteği": "Temel yaşam desteği, solunumu veya kalbi durmuş bir kişiye yapılan özel bir ilk yardım uygulamasıdır ve daha genel bir kavram olan ilk yardımın bir parçasıdır."
                    }
                },
                {
                    "question": "2. Aşağıdakilerden hangisi hayat kurtarma zincirine ait değildir?",
                    "options": ["A. Sağlık kuruluşuna haber verilmesi", "B. Hastane acil servislerinde müdahale yapılması", "C. Olay yerinde temel yaşam desteği yapılması", "D. Yoğun bakım ünitelerinde yapılan tedavi"],
                    "answer": "D. Yoğun bakım ünitelerinde yapılan tedavi",
                    "explanation": "Hayat kurtarma zinciri; 1. Sağlık kuruluşuna haber verilmesi, 2. Olay yerinde temel yaşam desteği, 3. Ambulans ekiplerince müdahale, 4. Hastane acil servislerinde müdahale halkalarından oluşur. Yoğun bakım ünitelerindeki tedavi bu zincirin bir parçası değildir.",
                    "wrong_explanations": {
                        "A. Sağlık kuruluşuna haber verilmesi": "Sağlık kuruluşuna haber verilmesi, hayat kurtarma zincirinin ilk ve en önemli halkalarından biridir.",
                        "B. Hastane acil servislerinde müdahale yapılması": "Hastane acil servislerinde yapılan müdahale, hayat kurtarma zincirinin dördüncü halkasıdır.",
                        "C. Olay yerinde temel yaşam desteği yapılması": "Olay yerinde temel yaşam desteği yapılması, hayat kurtarma zincirinin ikinci halkasıdır."
                    }
                },
                {
                    "question": "3. Aşağıdakilerden hangisi ilk yardımın öncelikli amaçlarından değildir?",
                    "options": ["A. Hayati tehlikeyi ortadan kaldırmak", "B. İyileşmeyi kolaylaştırmak", "C. Yaşamsal fonksiyonların sürdürülmesini sağlamak", "D. Acil ilaç tedavisine başlamak"],
                    "answer": "D. Acil ilaç tedavisine başlamak",
                    "explanation": "İlk yardımın öncelikli amaçları; hayati tehlikeyi ortadan kaldırmak, yaşamsal fonksiyonların sürdürülmesini sağlamak ve iyileşmeyi kolaylaştırmaktır. İlaç tedavisi ilk yardımın amaçlarından biri değildir.",
                    "wrong_explanations": {
                        "A. Hayati tehlikeyi ortadan kaldırmak": "Hayati tehlikeyi ortadan kaldırmak, ilk yardımın en temel ve öncelikli amacıdır.",
                        "B. İyileşmeyi kolaylaştırmak": "İyileşmeyi kolaylaştırmak, ilk yardımın amaçlarından biridir. Örneğin, bir yarayı temiz tutmak enfeksiyonu önleyerek iyileşmeyi kolaylaştırır.",
                        "C. Yaşamsal fonksiyonların sürdürülmesini sağlamak": "Yaşamsal fonksiyonların (solunum, dolaşım) sürdürülmesini sağlamak, ilk yardımın en kritik amaçlarındandır."
                    }
                },
                {
                    "question": "4. Aşağıdakilerden hangisi vücudu oluşturan sistemlerden değildir?",
                    "options": ["A. Dolaşım sistemi", "B. Solunum sistemi", "C. Omurga sistemi", "D. Hareket sistemi"],
                    "answer": "C. Omurga sistemi",
                    "explanation": "Vücudu oluşturan ana sistemler; hareket, dolaşım, sinir, solunum, boşaltım ve sindirim sistemleridir. Omurga, hareket sisteminin bir parçasıdır ancak tek başına bir sistem değildir.",
                    "wrong_explanations": {
                        "A. Dolaşım sistemi": "Dolaşım sistemi, kan, kalp ve damarlardan oluşur ve vücudun temel sistemlerinden biridir.",
                        "B. Solunum sistemi": "Solunum sistemi, akciğerler ve solunum yollarından oluşur ve vücudun temel sistemlerinden biridir.",
                        "D. Hareket sistemi": "Hareket sistemi, kemikler, eklemler ve kaslardan oluşur ve vücudun temel sistemlerinden biridir."
                    }
                },
                {
                    "question": "5. Kalp atımlarının atardamar duvarına yaptığı basıncın damar duvarında parmak uçlarıyla hissedilmesine ne ad verilir?",
                    "options": ["A. Tansiyon", "B. Nabız", "C. Kan basıncı", "D. Vücut ısısı"],
                    "answer": "B. Nabız",
                    "explanation": "Nabız, kalp atımlarının atardamar duvarına yaptığı basıncın parmak uçlarıyla hissedilmesidir. Yetişkin bir kişide normal nabız sayısı dakikada 60-100 arasındadır.",
                    "wrong_explanations": {
                        "A. Tansiyon": "Tansiyon, kanın damar duvarına yaptığı basıncın genel adıdır ve bir aletle ölçülür. Nabız ise bu basıncın parmakla hissedilen şeklidir.",
                        "C. Kan basıncı": "Kan basıncı, tansiyon ile aynı anlama gelir ve nabızdan farklı bir kavramdır.",
                        "D. Vücut ısısı": "Vücut ısısı, vücudun sıcaklık derecesidir ve bir termometre ile ölçülür."
                    }
                },
                {
                    "question": "6. Aşağıdakilerden hangisi hasta/yaralının değerlendirilmesinin amaçlarından değildir?",
                    "options": ["A. Güvenli bir müdahale sağlanması", "B. İlk yardım önceliklerinin belirlenmesi", "C. Yapılacak ilk yardım yönteminin belirlenmesi", "D. Hasta/yaralının tedavi edilmesi"],
                    "answer": "D. Hasta/yaralının tedavi edilmesi",
                    "explanation": "Hasta/yaralının değerlendirilmesinin amaçları; hastalık ya da yaralanmanın ciddiyetini değerlendirmek, ilk yardım önceliklerini belirlemek, yapılacak ilk yardım yöntemini belirlemek ve güvenli bir ilk yardım uygulaması sağlamaktır. Tedavi etmek, ilk yardımın değil, acil tedavinin amacıdır.",
                    "wrong_explanations": {
                        "A. Güvenli bir müdahale sağlanması": "Güvenli bir müdahale sağlanması, hem ilk yardımcı hem de hasta/yaralı için ortamın güvenli hale getirilmesini içerir ve değerlendirmenin bir parçasıdır.",
                        "B. İlk yardım önceliklerinin belirlenmesi": "Hasta/yaralının durumunun ciddiyetine göre hangi müdahalenin önce yapılacağını belirlemek, değerlendirmenin temel amaçlarındandır.",
                        "C. Yapılacak ilk yardım yönteminin belirlenmesi": "Değerlendirme sonucunda elde edilen bilgilere göre en uygun ilk yardım yöntemi seçilir."
                    }
                },
                {
                    "question": "7. Bilinci kapalı hasta/yaralıda, hava yolu açıklığının sağlanmasında dikkat edilmesi gereken ilkyardım uygulaması aşağıdakilerden hangisidir?",
                    "options": ["A. Ağız içi kontrolü bebeklerde işaret parmağı ile yapılmalı", "B. Ağız içinde gözle görülen bir cisim varsa çıkartılmalı", "C. Baş geri.çene yukarı pozisyonu verilerek ağız içi kontrolü", "D. Ağız içine hiçbir şekilde parmak sokulmamalı"],
                    "answer": "B. Ağız içinde gözle görülen bir cisim varsa çıkartılmalı",
                    "explanation": "Bilinci kapalı bir kişide hava yolu açıklığı sağlanırken, öncelikle ağız içi kontrol edilmelidir. Eğer gözle görülebilen bir yabancı cisim varsa, bu cisim dikkatlice çıkarılmalıdır. Bu, hava yolunun tıkanmasını önlemek için kritik bir adımdır.",
                    "wrong_explanations": {
                        "A. Ağız içi kontrolü bebeklerde işaret parmağı ile yapılmalı": "Bebeklerde ağız içi kontrolü, kör dalışa neden olabileceği için işaret parmağı ile değil, serçe parmağı ile yapılmalıdır.",
                        "C. Baş geri.çene yukarı pozisyonu verilerek ağız içi kontrolü": "Ağız içi kontrolü, baş geri-çene yukarı pozisyonu verilmeden önce yapılmalıdır.",
                        "D. Ağız içine hiçbir şekilde parmak sokulmamalı": "Eğer ağız içinde gözle görülen bir cisim varsa, bu cisim dikkatlice çıkarılmalıdır. Ancak kör dalış yapılmamalıdır."
                    }
                },
                {
                    "question": "8. Hasta/yaralının ağız içi kontrolü ne zaman yapılır?",
                    "options": ["A. Baş geri.çene yukarı pozisyonu vermeden hemen önce", "B. Bilinç kontrolünden hemen önce", "C. Suni solunumdan sonra", "D. İkinci değerlendirmeden sonra"],
                    "answer": "A. Baş geri.çene yukarı pozisyonu vermeden hemen önce",
                    "explanation": "Hava yolu açıklığını sağlamak için baş geri-çene yukarı pozisyonu verilmeden hemen önce ağız içi kontrol edilmelidir. Bu, hava yolunu tıkayabilecek herhangi bir yabancı cismin (örneğin, takma diş, kan, kusmuk) temizlenmesini sağlar.",
                    "wrong_explanations": {
                        "B. Bilinç kontrolünden hemen önce": "Bilinç kontrolü, herhangi bir müdahaleden önce ilk yapılması gereken işlemdir.",
                        "C. Suni solunumdan sonra": "Suni solunumdan sonra değil, önce ağız içi kontrol edilmelidir.",
                        "D. İkinci değerlendirmeden sonra": "Ağız içi kontrolü, ilk değerlendirmenin bir parçasıdır ve ikinci değerlendirmeden çok önce yapılır."
                    }
                },
                {
                    "question": "9. Aşağıdakilerden hangisi otomatik eksternal defibrilatör (OED-kullanımı ile ilgili doğru bir ifadedir?",
                    "options": ["A. Metal zeminde kullanılır", "B. Islak zeminde kullanılır", "C. Gebelerde kullanılır", "D. 13 günlük bir bebekte kullanılır"],
                    "answer": "C. Gebelerde kullanılır",
                    "explanation": "OED (Otomatik Eksternal Defibrilatör), hamilelerde güvenle kullanılabilir. Ancak metal ve ıslak zeminlerde kullanılmamalıdır. Ayrıca, 1 yaşından küçük bebeklerde kullanımı önerilmez.",
                    "wrong_explanations": {
                        "A. Metal zeminde kullanılır": "OED, elektrik şoku verdiği için metal zeminde kullanılmaz. Hasta iletken olmayan bir yüzeye alınmalıdır.",
                        "B. Islak zeminde kullanılır": "OED, elektrik şoku verdiği için ıslak zeminde kullanılmaz. Hasta kuru bir zemine alınmalı ve göğsü kurulanmalıdır.",
                        "D. 13 günlük bir bebekte kullanılır": "OED, 1 yaşından küçük bebeklerde kullanılmaz. Sadece 1 yaşından büyük çocuklar ve yetişkinler için uygundur."
                    }
                },
                {
                    "question": "10. Kalp masajı uygulaması ile ilgili aşağıdakilerden hangisi yanlıştır?",
                    "options": ["A. Yetişkinlerde kalp masajı iki elle yapılır", "B. Bebeklerde kalp masajı iki elle yapılır", "C. Çocuklarda kalp masajı tek elle yapılır", "D. Bebeklerde kalp masajı orta ve yüzük parmağı île yapılır"],
                    "answer": "B. Bebeklerde kalp masajı iki elle yapılır",
                    "explanation": "Bebeklerde (0-1 yaş) kalp masajı iki parmakla (orta ve yüzük parmağı) yapılır. İki elle kalp masajı yetişkinlerde uygulanır. Çocuklarda (1-8 yaş) ise tek elle yapılır.",
                    "wrong_explanations": {
                        "A. Yetişkinlerde kalp masajı iki elle yapılır": "Bu ifade doğrudur. Yetişkinlerde kalp masajı iki elin topuğu kullanılarak yapılır.",
                        "C. Çocuklarda kalp masajı tek elle yapılır": "Bu ifade doğrudur. Çocuklarda (1-8 yaş) kalp masajı tek elin topuğu ile yapılır.",
                        "D. Bebeklerde kalp masajı orta ve yüzük parmağı île yapılır": "Bu ifade doğrudur. Bebeklerde (0-1 yaş) kalp masajı, iki meme başının altındaki hattın ortasına orta ve yüzük parmağı kullanılarak yapılır."
                    }
                },
                {
                    "question": "11. Tam tıkanma yaşayan hasta yaralıya uygulanacak ilk yardım uygulaması hangisidir?",
                    "options": ["A. Hasta öksürmeye teşvik edilir", "B. Heimlich manevrası uygulanır", "C. Havaya bakması sağlanır", "D. Rentek manevrası uygulanır"],
                    "answer": "B. Heimlich manevrası uygulanır",
                    "explanation": "Tam tıkanıklık, kişinin nefes alamadığı, konuşamadığı ve öksüremediği durumdur. Bu durumda, hava yolunu açmak için Heimlich manevrası (karına bası) uygulanır.",
                    "wrong_explanations": {
                        "A. Hasta öksürmeye teşvik edilir": "Öksürmeye teşvik etme, kısmi tıkanıklık durumunda yapılır. Tam tıkanıklıkta kişi öksüremez.",
                        "C. Havaya bakması sağlanır": "Havaya bakmak, hava yolu tıkanıklığını gidermede etkili bir yöntem değildir.",
                        "D. Rentek manevrası uygulanır": "Rentek manevrası, araç içindeki yaralıyı omuriliğe zarar vermeden çıkarmak için kullanılan bir tekniktir. Hava yolu tıkanıklığı ile bir ilgisi yoktur."
                    }
                },
                {
                    "question": "12. Çocuklarda yapılacak temel yaşam desteği uygulama sırala ması aşağıdakilerden hangisinde doğru olarak verilmiştir?",
                    "options": ["A. Hava yolu açıklığı / Bilinç kontrolü/ Soluk / Kalp masajı", "B. Bilinç kontrolü/ Soluk / Hava yolu açıklığı / Kalp masajı", "C. Bilinç kontrolü/ Hava yolu açıklığı / Kalp masajı/ Soluk", "D. Bilinç kontrolü/Hava yolu açıklığı / Bak.Dinle.Hisset/ Soluk / Kalp masajı"],
                    "answer": "D. Bilinç kontrolü/Hava yolu açıklığı / Bak.Dinle.Hisset/ Soluk / Kalp masajı",
                    "explanation": "Çocuklarda temel yaşam desteği (TYD) uygulama sırası şu şekildedir: 1. Bilinç kontrolü, 2. Hava yolu açıklığının sağlanması, 3. Solunumun değerlendirilmesi (Bak-Dinle-Hisset), 4. Kurtarıcı soluk, 5. Kalp masajı.",
                    "wrong_explanations": {
                        "A. Hava yolu açıklığı / Bilinç kontrolü/ Soluk / Kalp masajı": "Sıralama yanlıştır. Önce bilinç kontrolü yapılmalıdır.",
                        "B. Bilinç kontrolü/ Soluk / Hava yolu açıklığı / Kalp masajı": "Sıralama yanlıştır. Soluk vermeden önce hava yolu açıklığı sağlanmalı ve solunum değerlendirilmelidir.",
                        "C. Bilinç kontrolü/ Hava yolu açıklığı / Kalp masajı/ Soluk": "Sıralama yanlıştır. Kalp masajından önce solunum değerlendirilmeli ve gerekirse kurtarıcı soluk verilmelidir."
                    }
                },
                {
                    "question": "13. Yetişkin hasta/yaralıda kalp masajı uygulanacak bölge aşağıdakilerden hangisidir?",
                    "options": ["A. Göğüs kemiğinin alt ve üst ucu tespit edilerek alt yarısına", "B. Göğüs kemiğinin alt ve üst ucu tespit edilerek üst yarısına", "C. Göğüs kemiğinin ortasına", "D. Göğüs kemiğinin üst noktasının 3 parmak altına"],
                    "answer": "A. Göğüs kemiğinin alt ve üst ucu tespit edilerek alt yarısına",
                    "explanation": "Yetişkinlerde kalp masajı, göğüs kemiğinin (iman tahtası) alt ve üst ucu tespit edildikten sonra, alt yarısının ortasına uygulanır.",
                    "wrong_explanations": {
                        "B. Göğüs kemiğinin alt ve üst ucu tespit edilerek üst yarısına": "Kalp masajı göğüs kemiğinin üst yarısına değil, alt yarısına uygulanır.",
                        "C. Göğüs kemiğinin ortasına": "Göğüs kemiğinin tam ortası değil, alt yarısının ortası hedeflenmelidir.",
                        "D. Göğüs kemiğinin üst noktasının 3 parmak altına": "Bu, doğru bir yer belirleme yöntemi değildir."
                    }
                },
                {
                    "question": "14. Bebeklerde ve çocuklarda temel yaşam desteği uygulama sırası hangisinde doğru verilmiştir?",
                    "options": ["A. 80 kalp basısı. 2 solunum", "B. 2 solunum.100 kalp basısı", "C. 2 solunum. 30 kalp basısı", "D. 2 solunum. 5 kalp basısı"],
                    "answer": "C. 2 solunum. 30 kalp basısı",
                    "explanation": "Bebeklerde ve çocuklarda temel yaşam desteği, 30 kalp masajı ve 2 kurtarıcı solunum döngüsü şeklinde uygulanır.",
                    "wrong_explanations": {
                        "A. 80 kalp basısı. 2 solunum": "Kalp masajı sayısı 30 olmalıdır.",
                        "B. 2 solunum.100 kalp basısı": "Kalp masajı sayısı 30 olmalıdır.",
                        "D. 2 solunum. 5 kalp basısı": "Kalp masajı sayısı 30 olmalıdır."
                    }
                },
                {
                    "question": "15. Aşağıdakilerden hangisi şok çeşitlerindendir?",
                    "options": ["A. Kardiyojenik şok", "B. Toksikşok", "C. Anaflaktik şok", "D. Hepsi"],
                    "answer": "D. Hepsi",
                    "explanation": "Şok, yaşamsal organlara yeterli kan gitmemesi sonucu ortaya çıkan bir durumdur. Çeşitleri arasında kalp kökenli (kardiyojenik), sıvı kaybına bağlı (hipovolemik), zehirlenmeye bağlı (toksik) ve alerjiye bağlı (anafilaktik) şok bulunur.",
                    "wrong_explanations": {
                        "A. Kardiyojenik şok": "Kardiyojenik şok bir şok çeşididir, ancak hepsi doğru olduğu için bu seçenek eksiktir.",
                        "B. Toksikşok": "Toksik şok bir şok çeşididir, ancak hepsi doğru olduğu için bu seçenek eksiktir.",
                        "C. Anaflaktik şok": "Anaflaktik şok bir şok çeşididir, ancak hepsi doğru olduğu için bu seçenek eksiktir."
                    }
                },
                {
                    "question": "16. Aşağıdakilerden hangisi damar tipine göre kanamalar arasında yer alır?",
                    "options": ["A. Dış kanama", "B. Kılcal damar kanaması", "C. İç kanama", "D. Doğal deliklerden olan kanama"],
                    "answer": "B. Kılcal damar kanaması",
                    "explanation": "Kanamalar, kanın aktığı damar tipine göre atardamar, toplardamar ve kılcal damar kanaması olarak üçe ayrılır. Dış kanama, iç kanama ve doğal deliklerden olan kanamalar ise kanın vücut içinde veya dışında olmasına göre yapılan bir sınıflandırmadır.",
                    "wrong_explanations": {
                        "A. Dış kanama": "Dış kanama, kanın vücut dışına aktığı kanama türüdür, damar tipine göre bir sınıflandırma değildir.",
                        "C. İç kanama": "İç kanama, kanın vücut içine aktığı kanama türüdür, damar tipine göre bir sınıflandırma değildir.",
                        "D. Doğal deliklerden olan kanama": "Doğal deliklerden olan kanama, kanın kulak, burun, ağız gibi doğal deliklerden aktığı kanama türüdür, damar tipine göre bir sınıflandırma değildir."
                    }
                },
                {
                    "question": "17. Aşağıdakilerden hangisi dış kanamalarda yapılması gereken ilkyardım uygulamaları arasında yer almaz?",
                    "options": ["A. Kanayan yer üzerine temiz bir bezle bastırılır", "B. Gerekirse bandaj ile sararak basınç uygulanır", "C. Kanamayı azaltmak için kanayan bölgeye buz konulur", "D. Kanayan yere en yakın basınç noktasına baskı uygulanır"],
                    "answer": "C. Kanamayı azaltmak için kanayan bölgeye buz konulur",
                    "explanation": "Dış kanamalarda kanamayı durdurmak için kanayan yer üzerine temiz bir bezle bastırılır, gerekirse bandajla sarılır ve kanayan bölge kalp seviyesinden yukarıda tutulur. Kanama durmazsa en yakın basınç noktasına baskı uygulanır. Buz uygulaması, kanamayı durdurmak için doğrudan bir yöntem değildir ve donma riski nedeniyle önerilmez.",
                    "wrong_explanations": {
                        "A. Kanayan yer üzerine temiz bir bezle bastırılır": "Bu, dış kanamalarda yapılması gereken temel ilk yardım uygulamalarından biridir.",
                        "B. Gerekirse bandaj ile sararak basınç uygulanır": "Kanayan yer üzerine bezle yapılan baskı yetersiz kalırsa, bandaj ile sararak basınç uygulamak doğru bir yöntemdir.",
                        "D. Kanayan yere en yakın basınç noktasına baskı uygulanır": "Diğer yöntemler başarısız olduğunda, kanamayı kontrol altına almak için en yakın basınç noktasına baskı uygulamak gerekir."
                    }
                },
                {
                    "question": "18. Aşağıdaki durumlardan hangisinde boğucu sargı (turnike-uygulanmaz?",
                    "options": ["A. Çok sayıda yaralı bulunduğu ortamda tek ilk yardımcı varsa", "B. Akrep veya yılan sokması varsa", "C. Uzuv kopması varsa", "D. Yaralı güç koşullarda başka bir yere taşınacaksa"],
                    "answer": "B. Akrep veya yılan sokması varsa",
                    "explanation": "Turnike (boğucu sargı), uzuv kopması, çok sayıda yaralının olduğu ve tek ilkyardımcının bulunduğu ortamlar gibi durumlarda kanamayı durdurmak için kullanılır. Ancak akrep veya yılan sokmalarında zehrin vücuda yayılmasını hızlandırabileceği için turnike uygulanmaz.",
                    "wrong_explanations": {
                        "A. Çok sayıda yaralı bulunduğu ortamda tek ilk yardımcı varsa": "Bu durumda, tüm yaralılara müdahale edebilmek için kanaması olan yaralıya turnike uygulanabilir.",
                        "C. Uzuv kopması varsa": "Uzuv kopması, turnike uygulamasının en önemli endikasyonlarından biridir.",
                        "D. Yaralı güç koşullarda başka bir yere taşınacaksa": "Yaralının taşınması sırasında kanama kontrolü zorlaşacağı için turnike uygulanabilir."
                    }
                },
                {
                    "question": "19. Aşağıdakilerden hangisi yaralanmalarda yapılan ilk yardım uygulamalarından biridir?",
                    "options": ["A. Kanama durdurulmalıdır", "B. Yara yeri alkolle yıkanmalıdır", "C. Yaradaki yabancı cisim çıkarılmalıdır", "D. Hasta/yaralıya ağızdan yiyecek/içecek verilmelidir"],
                    "answer": "A. Kanama durdurulmalıdır",
                    "explanation": "Yaralanmalarda ilk yardımın önceliği, kanamayı durdurarak hayatı tehdit eden durumu ortadan kaldırmaktır. Yara yeri alkolle yıkanmamalı, yabancı cisim çıkarılmamalı ve ağızdan yiyecek/içecek verilmemelidir.",
                    "wrong_explanations": {
                        "B. Yara yeri alkolle yıkanmalıdır": "Alkol, dokulara zarar verebilir ve iyileşmeyi geciktirebilir. Yara, temiz su veya serum fizyolojik ile temizlenmelidir.",
                        "C. Yaradaki yabancı cisim çıkarılmalıdır": "Yaradaki yabancı cisim, kanamayı durduran bir tampon görevi görüyor olabilir. Bu nedenle, yabancı cisimler sadece sağlık profesyonelleri tarafından çıkarılmalıdır.",
                        "D. Hasta/yaralıya ağızdan yiyecek/içecek verilmelidir": "Yaralının bilinci kapalı olabilir veya cerrahi bir müdahale gerekebilir. Bu nedenle, ağızdan bir şey verilmemelidir."
                    }
                },
                {
                    "question": "20. Aşağıdakilerden hangisi kafatası ve omurga yaralanmalarında yapılacak olan ilk yardım uygulamalarından biri değildir?",
                    "options": ["A. Bilinç kontrolü yapılmalı", "B. Herhangi bir tehlike varsa düz pozisyonda sürüklenme", "C. Şok pozisyonu verilmeli", "D. Tıbbi yardım istenmeli"],
                    "answer": "C. Şok pozisyonu verilmeli",
                    "explanation": "Kafatası ve omurga yaralanmalarında, sinir sistemine zarar verme riski nedeniyle hasta/yaralı mümkün olduğunca az hareket ettirilmelidir. Şok pozisyonu, bacakların 30 cm yukarı kaldırılmasını içerir ve bu hareket omurgaya zarar verebilir. Bu nedenle, bu tür yaralanmalarda şok pozisyonu verilmez.",
                    "wrong_explanations": {
                        "A. Bilinç kontrolü yapılmalı": "Bilinç kontrolü, yaralının durumunu değerlendirmek için yapılması gereken temel bir adımdır.",
                        "B. Herhangi bir tehlike varsa düz pozisyonda sürüklenme": "Eğer olay yerinde bir tehlike varsa (örneğin, yangın, patlama riski), yaralıyı güvenli bir yere taşımak için düz pozisyonda sürükleme yöntemi kullanılabilir.",
                        "D. Tıbbi yardım istenmeli": "Kafatası ve omurga yaralanmaları ciddi yaralanmalardır ve mutlaka tıbbi yardım (112) istenmelidir."
                    }
                }
            ]
        },
        "Test 2": {
            "questions": [
                {
                    "question": "1-Aşağıdakilerden hangisi kan şekerinin düşme nedenlerinden değildir?",
                    "options": ["A.Şeker hastalığı tedavisine bağlı", "B.Uzun süre aç kalma", "C.Aşırı yemek yeme", "D.Uzun süre yapılan egzersizler"],
                    "answer": "C.Aşırı yemek yeme",
                    "explanation": "Aşırı yemek yeme, kan şekerinin yükselmesine neden olur, düşmesine değil. Diğer seçenekler kan şekerinin düşme nedenleridir.",
                    "wrong_explanations": {
                        "A.Şeker hastalığı tedavisine bağlı": "Şeker hastalığı tedavisinde kullanılan bazı ilaçlar kan şekerini düşürebilir.",
                        "B.Uzun süre aç kalma": "Uzun süre aç kalmak, vücudun enerji için glikoz kullanamamasına ve kan şekerinin düşmesine neden olur.",
                        "D.Uzun süre yapılan egzersizler": "Uzun süreli egzersizler, vücudun glikoz kullanımını artırarak kan şekerinin düşmesine yol açabilir."
                    }
                },
                {
                    "question": "2-Hayat kurtarma zincirinin dördüncü halkası aşağıdakilerden hangisidir?",
                    "options": ["A.Sağlık kuruluşuna haber verilmesi", "B.Acil servislerde müdahale yapılması", "C.Ambulans ekiplerince müdahaleler yapılması", "D.Olay yerinde temel yaşam desteği yapılması"],
                    "answer": "C.Ambulans ekiplerince müdahaleler yapılması",
                    "explanation": "Hayat kurtarma zincirinin halkaları sırasıyla; 1. Sağlık kuruluşuna haber verilmesi, 2. Olay yerinde temel yaşam desteği, 3. Ambulans ekiplerince müdahaleler yapılması, 4. Hastane acil servislerinde müdahale yapılmasıdır.",
                    "wrong_explanations": {
                        "A.Sağlık kuruluşuna haber verilmesi": "Bu, hayat kurtarma zincirinin birinci halkasıdır.",
                        "B.Acil servislerde müdahale yapılması": "Bu, hayat kurtarma zincirinin dördüncü halkasıdır.",
                        "D.Olay yerinde temel yaşam desteği yapılması": "Bu, hayat kurtarma zincirinin ikinci halkasıdır."
                    }
                },
                {
                    "question": "3-İlk yardımın temel uygulamaları aşağıdakilerden hangisinde doğru olarak verilmiştir?",
                    "options": ["A.Bildirme- kurtarma-taşıma", "B.Koruma- bildirme- kurtarma", "C.Tedavi-koruma-taşıma", "D.Tedavi- bildirme- kurtarma"],
                    "answer": "B.Koruma- bildirme- kurtarma",
                    "explanation": "İlk yardımın temel uygulamaları Koruma, Bildirme ve Kurtarma (KBK) olarak sıralanır.",
                    "wrong_explanations": {
                        "A.Bildirme- kurtarma-taşıma": "Taşıma, ilk yardımın temel uygulamalarından biri değildir, kurtarma aşamasının bir parçası olabilir.",
                        "C.Tedavi-koruma-taşıma": "Tedavi ve taşıma, ilk yardımın temel uygulamaları arasında yer almaz.",
                        "D.Tedavi- bildirme- kurtarma": "Tedavi, ilk yardımın değil, acil tedavinin amacıdır."
                    }
                },
                {
                    "question": "4-Aşağıda yer alan sistem ve yapı eşleştirmelerinden hangisi yanlış verilmiştir?",
                    "options": ["A.Solunum sistemi-akciğerler", "B.Sindirim sistemi-bağırsaklar", "C.Hareket sistemi-kemikler", "D.Sinir sistemi-kaslar"],
                    "answer": "D.Sinir sistemi-kaslar",
                    "explanation": "Sinir sistemi, beyin, omurilik ve sinirlerden oluşur. Kaslar ise hareket sisteminin bir parçasıdır.",
                    "wrong_explanations": {
                        "A.Solunum sistemi-akciğerler": "Solunum sistemi akciğerler ile doğru eşleştirilmiştir.",
                        "B.Sindirim sistemi-bağırsaklar": "Sindirim sistemi bağırsaklar ile doğru eşleştirilmiştir.",
                        "C.Hareket sistemi-kemikler": "Hareket sistemi kemikler ile doğru eşleştirilmiştir."
                    }
                },
                {
                    "question": "5-Aşağıdakilerden hangisi ilk yardımda yaşam bulgusu değerlendirilmesinde yer almaz?",
                    "options": ["A.Bilinç", "B.Solunum", "C.Işık refleksi", "D.Vücut ısısı"],
                    "answer": "C.Işık refleksi",
                    "explanation": "İlk yardımda yaşam bulguları değerlendirilirken bilinç, solunum, nabız (dolaşım) ve vücut ısısı kontrol edilir. Işık refleksi, nörolojik bir değerlendirme olup ilk yardımın temel yaşam bulguları arasında yer almaz.",
                    "wrong_explanations": {
                        "A.Bilinç": "Bilinç, yaşam bulgularının en önemlilerinden biridir.",
                        "B.Solunum": "Solunum, yaşam bulgularının en önemlilerinden biridir.",
                        "D.Vücut ısısı": "Vücut ısısı, yaşam bulgularının en önemlilerinden biridir."
                    }
                },
                {
                    "question": "6-İlkyardımcı yalnız ise bilinci kapalı bir hasta/yaralıya yapacağı ilk uygulama aşağıdakilerden hangisidir?",
                    "options": ["A.Ağız içini kontrol etmek", "B.Baş geri çene yukarı yöntemi ile soluk yolunu açmak", "C.112'ye haber vermek", "D.İki kurtarıcı soluk vermek"],
                    "answer": "C.112'ye haber vermek",
                    "explanation": "İlkyardımcı yalnız ise ve bilinci kapalı bir hasta/yaralı ile karşılaştığında, öncelikle 112'yi aramalı ve yardım çağırmalıdır. Diğer uygulamalar daha sonra yapılmalıdır.",
                    "wrong_explanations": {
                        "A.Ağız içini kontrol etmek": "Ağız içi kontrolü, hava yolu açıklığını sağlamak için önemlidir ancak 112'yi aramadan önce yapılmamalıdır.",
                        "B.Baş geri çene yukarı yöntemi ile soluk yolunu açmak": "Baş geri çene yukarı yöntemi, hava yolu açıklığını sağlamak için önemlidir ancak 112'yi aramadan önce yapılmamalıdır.",
                        "D.İki kurtarıcı soluk vermek": "Kurtarıcı soluk vermek, temel yaşam desteğinin bir parçasıdır ancak 112'yi aramadan önce yapılmamalıdır."
                    }
                },
                {
                    "question": "7-Bak-dinle-hisset yönteminde aşağıdakilerden hangisi yer almaz?",
                    "options": ["A.Şah damarından nabız kontrolü yapmak", "B.Göğüs kafesinin hareketlerini izlemek", "C.Hasta/yaralının soluk alıp verişini dinlemek", "D.Hasta/yaralının soluğunu yanağımızda hissetmeye çalışmak"],
                    "answer": "A.Şah damarından nabız kontrolü yapmak",
                    "explanation": "Bak-dinle-hisset yöntemi, solunumun varlığını değerlendirmek için kullanılır. Bu yöntemde göğüs kafesinin hareketleri izlenir, soluk alıp verişi dinlenir ve yanağımızda soluk hissedilmeye çalışılır. Şah damarından nabız kontrolü ise dolaşımın değerlendirilmesi için yapılır.",
                    "wrong_explanations": {
                        "B.Göğüs kafesinin hareketlerini izlemek": "Bu, bak-dinle-hisset yönteminin bir parçasıdır.",
                        "C.Hasta/yaralının soluk alıp verişini dinlemek": "Bu, bak-dinle-hisset yönteminin bir parçasıdır.",
                        "D.Hasta/yaralının soluğunu yanağımızda hissetmeye çalışmak": "Bu, bak-dinle-hisset yönteminin bir parçasıdır."
                    }
                },
                {
                    "question": "8-Aşağıdakilerden hangisi ciddi yaralanmalar arasında yer almaz?",
                    "options": ["A.Kas veya kemiğin göründüğü yaralar", "B.İnsan veya hayvan ısırıkları", "C.Yabancı cisim saplanmış olan yaralar", "D.Kanaması durdurulabilen yaralar"],
                    "answer": "D.Kanaması durdurulabilen yaralar",
                    "explanation": "Ciddi yaralanmalar, genellikle hayatı tehdit eden veya kalıcı hasara yol açabilecek yaralanmalardır. Kanaması durdurulabilen yaralar, genellikle ciddi yaralanma kategorisine girmez.",
                    "wrong_explanations": {
                        "A.Kas veya kemiğin göründüğü yaralar": "Kas veya kemiğin göründüğü yaralar, açık ve derin yaralanmalar olduğu için ciddi kabul edilir.",
                        "B.İnsan veya hayvan ısırıkları": "İnsan veya hayvan ısırıkları, enfeksiyon riski ve doku hasarı nedeniyle ciddi yaralanma olarak kabul edilir.",
                        "C.Yabancı cisim saplanmış olan yaralar": "Yabancı cisim saplanmış yaralar, iç organlara zarar verme riski taşıdığı için ciddi yaralanmalardır."
                    }
                },
                {
                    "question": "9-Yaşam kurtarmak amacı ile hava yolu açıklığı sağlandıktan sonra, solunumu ve/veya kalbi durmuş kişiye yapay solunum ile akciğerlerine oksijen gitmesini, dış kalp masajı ile de kalpten kan pompalanmasını sağlamak üzere yapılan ilaçsız müdahalelerdir. ifadesi aşağıdakilerden hangisini tanımlamaktadır?",
                    "options": ["A.İlk yardım", "B.Temel yaşam desteği", "C.Acil yardım", "D.Acil tedavi"],
                    "answer": "B.Temel yaşam desteği",
                    "explanation": "Verilen tanım, solunumu ve/veya kalbi durmuş kişiye yapılan yapay solunum ve dış kalp masajı gibi ilaçsız müdahaleleri kapsayan Temel Yaşam Desteği'ne aittir.",
                    "wrong_explanations": {
                        "A.İlk yardım": "İlk yardım, olay yerinde yapılan genel ve ilaçsız müdahalelerin tümünü kapsar. Temel yaşam desteği, ilk yardımın bir alt dalıdır.",
                        "C.Acil yardım": "Acil yardım, genellikle profesyonel sağlık ekipleri tarafından yapılan daha kapsamlı müdahaleleri ifade eder.",
                        "D.Acil tedavi": "Acil tedavi, sağlık profesyonelleri tarafından ilaç ve tıbbi ekipman kullanılarak yapılan müdahaledir."
                    }
                },
                {
                    "question": "10-Temel yaşam desteği ile ilgili olarak aşağıdakilerden hangi yanlıştır?",
                    "options": ["A.0-28 günlük bebeklerde temel yaşam desteği uygulaması yapılmaz", "B.Bilinci ve solunumu olan hastaya uygulanmaz", "C.OED cihazı ile şok verildikten hemen sonra göğüs basısına devam edilir", "D.Solunumu ve kalbi durmuş kişilere yapılır"],
                    "answer": "A.0-28 günlük bebeklerde temel yaşam desteği uygulaması yapılmaz",
                    "explanation": "0-28 günlük bebeklerde de temel yaşam desteği uygulaması yapılır. Diğer seçenekler temel yaşam desteği ile ilgili doğru ifadelerdir.",
                    "wrong_explanations": {
                        "B.Bilinci ve solunumu olan hastaya uygulanmaz": "Temel yaşam desteği, bilinci ve solunumu durmuş kişilere uygulanır.",
                        "C.OED cihazı ile şok verildikten hemen sonra göğüs basısına devam edilir": "OED ile şok verildikten sonra kesintisiz göğüs basısına devam edilmelidir.",
                        "D.Solunumu ve kalbi durmuş kişilere yapılır": "Temel yaşam desteği, solunumu ve kalbi durmuş kişilere uygulanır."
                    }
                },
                {
                    "question": "11-Çocuklarda dış kalp masajı ile ilgili aşağıda verilenlerden hangisi doğrudur?",
                    "options": ["A.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır, dakikada 80 bası", "B.Göğüs kemiği 4 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'ü kadar bası uygulanır dakikada 80 bası", "C.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır, dakikada 100 bası", "D.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'si kadar bası uygulanır, dakikada 100 bası"],
                    "answer": "C.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır, dakikada 100 bası",
                    "explanation": "Çocuklarda dış kalp masajı, göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır ve dakikada 100 bası yapılmalıdır.",
                    "wrong_explanations": {
                        "A.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır, dakikada 80 bası": "Dakikada 80 bası değil, 100 bası yapılmalıdır.",
                        "B.Göğüs kemiği 4 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'ü kadar bası uygulanır dakikada 80 bası": "Göğüs kemiği 5 cm inecek şekilde ve dakikada 100 bası yapılmalıdır.",
                        "D.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'si kadar bası uygulanır, dakikada 100 bası": "Göğüs yüksekliğinin 1/3'ü değil, 1/3'ü kadar bası uygulanmalıdır.",
                        "D.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'si kadar bası uygulanır, dakikada 100 bası": "Göğüs yüksekliğinin 1/3'ü değil, 1/3'ü kadar bası uygulanmalıdır."
                    }
                },
                {
                    "question": "12-Aşağıdakilerden hangisi tam tıkanmanın belirtilerindendir?",
                    "options": ["A.Nefes alabilir", "B.Rengi morarmıştır", "C.Öksürebilir", "D.Konuşabilir"],
                    "answer": "B.Rengi morarmıştır",
                    "explanation": "Tam tıkanma durumunda kişi nefes alamaz, konuşamaz ve öksüremez. Rengi morarmıştır çünkü oksijen alamamaktadır.",
                    "wrong_explanations": {
                        "A.Nefes alabilir": "Nefes alabiliyorsa bu kısmi tıkanmadır.",
                        "C.Öksürebilir": "Öksürebiliyorsa bu kısmi tıkanmadır.",
                        "D.Konuşabilir": "Konuşabiliyorsa bu kısmi tıkanmadır."
                    }
                },
                {
                    "question": "13-İlk yardımcının yetişkin bir hasta/yaralıya uygulayacağı kalp masajı ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
                    "options": ["A.Tek el ile göğüs kemiği 2-3 cm. aşağı inecek şekilde bası uygulamak", "B.Tek elin orta ve yüzük parmağı ile göğüs kemiği 3 cm. aşağı inecek şekilde bası uygulamak", "C.İki el ile göğüs kemiği 5 cm. aşağı inecek şekilde bası uygulamak", "D.İki el ile göğüs kemiği 3 cm. aşağı inecek şekilde bası uygulamak"],
                    "answer": "C.İki el ile göğüs kemiği 5 cm. aşağı inecek şekilde bası uygulamak",
                    "explanation": "Yetişkinlerde kalp masajı, göğüs kemiği 5 cm aşağı inecek şekilde iki el ile uygulanır.",
                    "wrong_explanations": {
                        "A.Tek el ile göğüs kemiği 2-3 cm. aşağı inecek şekilde bası uygulamak": "Tek el ile kalp masajı çocuklarda uygulanır ve bası derinliği 5 cm olmalıdır.",
                        "B.Tek elin orta ve yüzük parmağı ile göğüs kemiği 3 cm. aşağı inecek şekilde bası uygulamak": "Bu teknik bebeklerde kullanılır ve bası derinliği 4 cm olmalıdır.",
                        "D.İki el ile göğüs kemiği 3 cm. aşağı inecek şekilde bası uygulamak": "Bası derinliği 5 cm olmalıdır."
                    }
                },
                {
                    "question": "14-Suni solunum ile ilgili aşağıda verilen şıklardan hangisi doğrudur?",
                    "options": ["A.Bebek ve çocuklarda verilen her solunum sonrası bak-dinle-hisset yapılır", "B.Yetişkinlerde verilen her solunum sonrası bak-dinle- hisset yapılır", "C.Bebeklerde temel yaşam desteğine 5 solunum ile başlanır", "D.Bebeklerde ağız ve buruna birlikte solunum verilir"],
                    "answer": "D.Bebeklerde ağız ve buruna birlikte solunum verilir",
                    "explanation": "Bebeklerde suni solunum yapılırken, ilkyardımcı ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir ve her biri 1 saniyeden uzun süren 2 kurtarıcı soluk verir.",
                    "wrong_explanations": {
                        "A.Bebek ve çocuklarda verilen her solunum sonrası bak-dinle-hisset yapılır": "Her solunum sonrası değil, 30 kalp masajı sonrası 2 solunum verilir.",
                        "B.Yetişkinlerde verilen her solunum sonrası bak-dinle- hisset yapılır": "Yetişkinlerde de her solunum sonrası değil, 30 kalp masajı sonrası 2 solunum verilir.",
                        "C.Bebeklerde temel yaşam desteğine 5 solunum ile başlanır": "Bebeklerde temel yaşam desteğine 2 kurtarıcı soluk ile başlanır."
                    }
                },
                {
                    "question": "15-Zehirlenme ile gelişen şok çeşidi aşağıdakilerden hangisidir?",
                    "options": ["A.Kardiyojenik şok", "B.Hipovolemik şok", "C.Nörolojik şok", "D.Toksikşok"],
                    "answer": "D.Toksikşok",
                    "explanation": "Zehirlenme ile gelişen şok çeşidi toksik şoktur. Kardiyojenik şok kalp yetmezliğine, hipovolemik şok sıvı kaybına, nörojenik şok ise sinir sistemi hasarına bağlı gelişir.",
                    "wrong_explanations": {
                        "A.Kardiyojenik şok": "Kardiyojenik şok, kalp yetmezliğine bağlı olarak gelişen şoktur.",
                        "B.Hipovolemik şok": "Hipovolemik şok, vücuttaki sıvı kaybına bağlı olarak gelişen şoktur.",
                        "C.Nörolojik şok": "Nörolojik şok, sinir sistemi hasarına bağlı olarak gelişen şoktur."
                    }
                },
                {
                    "question": "16-Aşagıdakilerden hangisi vücutta kanın aktığı bölge tipine göre kanamalar arasında yer alır?",
                    "options": ["A.Kılcal damar kanaması", "B.Doğal deliklerden olan kanama", "C.Toplardamar kanaması", "D.Atardamar kanaması"],
                    "answer": "D.Atardamar kanaması",
                    "explanation": "Kanamalar, kanın aktığı damar tipine göre atardamar, toplardamar ve kılcal damar kanaması olarak sınıflandırılır. Atardamar kanamaları, kalp atımı ile uyumlu olarak kesik kesik ve fışkırır tarzda olur.",
                    "wrong_explanations": {
                        "A.Kılcal damar kanaması": "Kılcal damar kanamaları, sızıntı şeklinde ve kolayca durdurulabilen kanamalardır.",
                        "B.Doğal deliklerden olan kanama": "Doğal deliklerden olan kanama, kanın vücudun doğal açıklıklarından (burun, kulak vb.) gelmesidir ve damar tipine göre bir sınıflandırma değildir.",
                        "C.Toplardamar kanaması": "Toplardamar kanamaları, koyu renkli ve sürekli akan kanamalardır."
                    }
                },
                {
                    "question": "17-Dış kanamalarda yapılacak ilk yardım uygulamaları ile ilgili aşağıdakilerden hangisi doğru bir ifade değildir?",
                    "options": ["A.Kanayan yer üzerine temiz bir bezle bastırılır.", "B.Kanayan yere en yakın basınç noktasına baskı uygulanır", "C.Kanayan bölge aşağıda tutulur.", "D.Gerekirse bandaj ile sararak basınç uygulanır."],
                    "answer": "C.Kanayan bölge aşağıda tutulur.",
                    "explanation": "Dış kanamalarda kanayan bölge kalp seviyesinden yukarıda tutulmalıdır. Kanayan bölgenin aşağıda tutulması kan kaybını artırır.",
                    "wrong_explanations": {
                        "A.Kanayan yer üzerine temiz bir bezle bastırılır.": "Bu, dış kanamalarda yapılması gereken temel ilk yardım uygulamalarından biridir.",
                        "B.Kanayan yere en yakın basınç noktasına baskı uygulanır": "Diğer yöntemler başarısız olduğunda, kanamayı kontrol altına almak için en yakın basınç noktasına baskı uygulamak gerekir.",
                        "D.Gerekirse bandaj ile sararak basınç uygulanır.": "Kanayan yer üzerine bezle yapılan baskı yetersiz kalırsa, bandaj ile sararak basınç uygulamak doğru bir yöntemdir."
                    }
                },
                {
                    "question": "18-Taş, yumruk ya da sopa gibi etkenlerin şiddetli olarak çarpması sonucu oluşan yaralar aşağıdakilerden hangisidir?",
                    "options": ["A.Ezikli yaralar", "B.Kesik yaralar", "C.Parçalı yaralar", "D.Delici yaralar"],
                    "answer": "A.Ezikli yaralar",
                    "explanation": "Ezikli yaralar, genellikle künt travma sonucu oluşan, doku ezilmesi ve morarma ile karakterize yaralardır. Taş, yumruk veya sopa gibi etkenler bu tür yaralanmalara neden olur.",
                    "wrong_explanations": {
                        "B.Kesik yaralar": "Kesik yaralar, kesici aletlerle oluşan, düzgün kenarlı yaralardır.",
                        "C.Parçalı yaralar": "Parçalı yaralar, doku kaybının olduğu, düzensiz kenarlı yaralardır.",
                        "D.Delici yaralar": "Delici yaralar, sivri uçlu cisimlerle oluşan, derinliği fazla olan yaralardır."
                    }
                },
                {
                    "question": "19-Aşağıdakilerden hangisi delici göğüs yaralanmalarında yapılacak ilk yardım uygulamalarından biridir?",
                    "options": ["A.Hasta/yaralıya ağızdan yiyecek-içecek verilir.", "B.Hasta/yaralının bilinci açıksa koma pozisyonu verilir.", "C.Dışarı çıkan organlar içeri sokulmaya çalışılır.", "D.Yara üzeri plastik poşet, naylon vb. sarılmış bir bezle kapatılır"],
                    "answer": "D.Yara üzeri plastik poşet, naylon vb. sarılmış bir bezle kapatılır",
                    "explanation": "Delici göğüs yaralanmalarında, yara üzerine plastik poşet veya naylon gibi hava geçirmeyen bir malzeme ile kapatılarak hava giriş çıkışı engellenir. Bu, akciğerin çökmesini (pnömotoraks) önlemeye yardımcı olur.",
                    "wrong_explanations": {
                        "A.Hasta/yaralıya ağızdan yiyecek-içecek verilir.": "Delici göğüs yaralanmalarında, yaralıya ağızdan hiçbir şey verilmemelidir.",
                        "B.Hasta/yaralının bilinci açıksa koma pozisyonu verilir.": "Koma pozisyonu, bilinci kapalı olan ve solunumu olan hastalara verilir. Delici göğüs yaralanmalarında genellikle yarı oturur pozisyon verilir.",
                        "C.Dışarı çıkan organlar içeri sokulmaya çalışılır.": "Dışarı çıkan organlar asla içeri sokulmaya çalışılmamalıdır. Bu, daha fazla hasara ve enfeksiyona neden olabilir."
                    }
                },
                {
                    "question": "20-Aşağıdakilerden hangisi kafatası ve omurga yaralanmalarında görülen belirtiler arasında yer almaz?",
                    "options": ["A.Denge kaybı", "B.Cilt ve tırnaklarda kısa süreli kiraz kırmızısı renk değişimi", "C.Sarsıntı, bilinç düzeyinde değişmeler", "D.Baş ya da bel kemiğinde şekil bozukluğu"],
                    "answer": "B.Cilt ve tırnaklarda kısa süreli kiraz kırmızısı renk değişimi",
                    "explanation": "Kafatası ve omurga yaralanmalarında denge kaybı, sarsıntı, bilinç düzeyinde değişmeler ve baş ya da bel kemiğinde şekil bozukluğu gibi belirtiler görülebilir. Cilt ve tırnaklarda kısa süreli kiraz kırmızısı renk değişimi ise karbonmonoksit zehirlenmesi gibi durumlarda görülen bir belirtidir.",
                    "wrong_explanations": {
                        "A.Denge kaybı": "Denge kaybı, kafatası ve omurga yaralanmalarında görülebilen bir belirtidir.",
                        "C.Sarsıntı, bilinç düzeyinde değişmeler": "Sarsıntı ve bilinç düzeyinde değişmeler, kafatası ve omurga yaralanmalarında görülebilen ciddi belirtilerdir.",
                        "D.Baş ya da bel kemiğinde şekil bozukluğu": "Baş ya da bel kemiğinde şekil bozukluğu, omurga yaralanmalarının açık bir işaretidir."
                    }
                }
            ]
        },
        "Test 3": {
            "questions": [
                {
                    "question": "1-Aşağıdakilerden hangisi yaraların ortak belirtilerinden değildir?",
                    "options": ["A.Kanama", "B.Ödem", "C.Ağrı", "D.Yara kenarlarının ayrılması"],
                    "answer": "D.Yara kenarlarının ayrılması",
                    "explanation": "Yaraların ortak belirtileri kanama, ödem (şişlik) ve ağrıdır. Yara kenarlarının ayrılması, yaranın tipine göre değişen bir durumdur ve tüm yaralarda görülmez.",
                    "wrong_explanations": {
                        "A.Kanama": "Kanama, yaralanmaların en yaygın belirtilerinden biridir.",
                        "B.Ödem": "Ödem (şişlik), yaralanma bölgesinde doku sıvısının birikmesi sonucu oluşur.",
                        "C.Ağrı": "Ağrı, yaralanmanın şiddetine göre değişmekle birlikte, tüm yaralarda görülen bir belirtidir."
                    }
                },
                {
                    "question": "2-Hayat kurtarma zincirinin Birinci halkası aşağıdakilerden hangisidir?",
                    "options": ["A.Sağlık kuruluşuna haber verilmesi", "B.Acilservislerde müdahale yapılması", "C.Ambulans ekiplerince müdahaleler yapılması", "D.Olay yerinde temel yaşam desteği yapılması"],
                    "answer": "A.Sağlık kuruluşuna haber verilmesi",
                    "explanation": "Hayat kurtarma zincirinin birinci halkası, olay yerinde sağlık kuruluşuna (112) haber verilmesidir. Bu, hızlı ve etkili tıbbi yardımın ulaşmasını sağlar.",
                    "wrong_explanations": {
                        "B.Acilservislerde müdahale yapılması": "Acil servislerde müdahale, hayat kurtarma zincirinin dördüncü halkasıdır.",
                        "C.Ambulans ekiplerince müdahaleler yapılması": "Ambulans ekiplerince müdahaleler, hayat kurtarma zincirinin üçüncü halkasıdır.",
                        "D.Olay yerinde temel yaşam desteği yapılması": "Olay yerinde temel yaşam desteği yapılması, hayat kurtarma zincirinin ikinci halkasıdır."
                    }
                },
                {
                    "question": "3-Kısa süreli yüzeysel ve geçici bilinç kaybına ne denir?",
                    "options": ["A.Havale", "B.Bayılma", "C.Koma", "D.Sıcak çarpması"],
                    "answer": "B.Bayılma",
                    "explanation": "Bayılma, genellikle kısa süreli, yüzeysel ve geçici bilinç kaybıdır. Beyne giden kan akışının geçici olarak azalması sonucu oluşur.",
                    "wrong_explanations": {
                        "A.Havale": "Havale, beyindeki elektriksel aktivitenin ani ve kontrolsüz boşalması sonucu oluşan bir durumdur ve genellikle kasılmalarla seyreder.",
                        "C.Koma": "Koma, uzun süreli ve derin bilinç kaybı durumudur.",
                        "D.Sıcak çarpması": "Sıcak çarpması, vücut ısısının tehlikeli derecede yükselmesi sonucu oluşan ciddi bir durumdur ve bilinç kaybına yol açabilir ancak tanımı farklıdır."
                    }
                },
                {
                    "question": "4-Yetişkin bir hasta/yaralıya yapılacak temel yaşam desteği uygulaması sırası ve sayıları aşağıdakilerden hangisinde doğru olarak verilmiştir?",
                    "options": ["A.30 kalp masajı-2 soluk", "B.5 soluk-30 kalp masajı", "C.2 soluk -15 kalp masajı", "D.15 kalp masajı-5 soluk"],
                    "answer": "A.30 kalp masajı-2 soluk",
                    "explanation": "Yetişkinlerde temel yaşam desteği (TYD) uygulaması 30 kalp masajı ve 2 kurtarıcı soluk şeklinde bir döngü ile yapılır.",
                    "wrong_explanations": {
                        "B.5 soluk-30 kalp masajı": "Soluk sayısı 2, kalp masajı sayısı 30 olmalıdır.",
                        "C.2 soluk -15 kalp masajı": "Kalp masajı sayısı 30 olmalıdır.",
                        "D.15 kalp masajı-5 soluk": "Kalp masajı sayısı 30, soluk sayısı 2 olmalıdır."
                    }
                },
                {
                    "question": "5-Aşağıdakilerden hangisi cilt yolu zehirlenmelerinden değildir?",
                    "options": ["A.Zirai ilaçlar", "B.Böcek sokmaları", "C. Klor", "D. İlaç enjeksiyonları"],
                    "answer": "C. Klor",
                    "explanation": "Klor, solunum yoluyla zehirlenmeye neden olan bir maddedir. Zirai ilaçlar, böcek sokmaları ve ilaç enjeksiyonları ise cilt yoluyla zehirlenmeye neden olabilir.",
                    "wrong_explanations": {
                        "A.Zirai ilaçlar": "Zirai ilaçlar, cilt yoluyla emilerek zehirlenmeye neden olabilir.",
                        "B.Böcek sokmaları": "Böcek sokmaları, cilt yoluyla zehirin vücuda girmesine neden olur.",
                        "D. İlaç enjeksiyonları": "İlaç enjeksiyonları, ilacın doğrudan cilt altına veya kas içine verilmesiyle cilt yoluyla zehirlenmeye neden olabilir."
                    }
                },
                {
                    "question": "6-Kalp krizinde aşağıdaki belirtilerden hangisi görülmez?",
                    "options": ["A.Nefes alıp vermekle ağrının şekli ve şiddeti değişir", "B.Ağrı göğüs veya mide boşluğunun olduğu bölgede sıklıkla kravat bölgesinde görülür", "C.Ağrı uzun sürelidir", "D.Hasta ciddi bir ölüm korkusu ve sıkıntı hisseder"],
                    "answer": "A.Nefes alıp vermekle ağrının şekli ve şiddeti değişir",
                    "explanation": "Kalp krizi ağrısı genellikle nefes alıp vermekle değişmez. Ağrı göğüs veya mide boşluğunun olduğu bölgede, sıklıkla kravat bölgesinde görülür, uzun sürelidir ve hasta ciddi bir ölüm korkusu ve sıkıntı hisseder.",
                    "wrong_explanations": {
                        "B.Ağrı göğüs veya mide boşluğunun olduğu bölgede sıklıkla kravat bölgesinde görülür": "Bu, kalp krizinin tipik bir belirtisidir.",
                        "C.Ağrı uzun sürelidir": "Kalp krizi ağrısı genellikle uzun süreli ve geçmeyen bir ağrıdır.",
                        "D.Hasta ciddi bir ölüm korkusu ve sıkıntı hisseder": "Ölüm korkusu ve sıkıntı hissi, kalp krizinin önemli belirtilerindendir."
                    }
                },
                {
                    "question": "7- Aşağıdakilerden hangisi 2.derece yanıkda yapılan ilkyardım uygulamalarından değildir?",
                    "options": ["A.Yanık bölgeler birlikte bandaj yapılmalıdır", "B.Yüzük saat gibi eşyalar çıkartılmalıdır", "C.Takılan yerler varsa kesilmelidir", "D.Yanık üzeri temiz bir bezle örtülmelidir"],
                    "answer": "A.Yanık bölgeler birlikte bandaj yapılmalıdır",
                    "explanation": "İkinci derece yanıklarda, yanık bölgeler ayrı ayrı bandajlanmalıdır. Birlikte bandajlamak, enfeksiyon riskini artırabilir ve iyileşmeyi zorlaştırabilir. Diğer seçenekler doğru ilk yardım uygulamalarıdır.",
                    "wrong_explanations": {
                        "B.Yüzük saat gibi eşyalar çıkartılmalıdır": "Yanık bölgesinde şişlik oluşabileceği için yüzük, saat gibi eşyalar çıkartılmalıdır.",
                        "C.Takılan yerler varsa kesilmelidir": "Yanık bölgesine yapışan giysiler kesilerek çıkarılmalıdır, çekilerek çıkarılmamalıdır.",
                        "D.Yanık üzeri temiz bir bezle örtülmelidir": "Yanık üzeri enfeksiyonu önlemek için temiz bir bezle örtülmelidir."
                    }
                },
                {
                    "question": "8-Trafik kazası sonucu oluşan yaralanmada hasta yaralının hangi durumda mutlaka araçtan çıkartılması gerekir?",
                    "options": ["A.Yaralının solunumu durmuşsa", "B.Yaralı sıkışmışsa", "C.Yaralının bilinci açık ön kolunda kırık varsa", "D.Yaralının bilinci yok solunumu varsa"],
                    "answer": "D.Yaralının bilinci yok solunumu varsa",
                    "explanation": "Trafik kazalarında yaralıyı araçtan çıkarmak genellikle risklidir ve omurilik yaralanmasına neden olabilir. Ancak, yaralının bilinci yok ve solunumu varsa, hava yolunun tıkanma riski nedeniyle araçtan çıkarılması gerekebilir. Diğer durumlarda, yaralının araç içinde sabitlenmesi ve profesyonel yardım beklenmesi daha güvenlidir.",
                    "wrong_explanations": {
                        "A.Yaralının solunumu durmuşsa": "Solunumu durmuş bir yaralıya araç içinde temel yaşam desteği uygulanabilir, ancak omurilik yaralanması riski nedeniyle araçtan çıkarmak son çare olmalıdır.",
                        "B.Yaralı sıkışmışsa": "Yaralı sıkışmışsa, araçtan çıkarmak daha fazla yaralanmaya neden olabilir. Profesyonel kurtarma ekipleri beklenmelidir.",
                        "C.Yaralının bilinci açık ön kolunda kırık varsa": "Bilinci açık ve sadece ön kolunda kırık olan bir yaralı, omurilik yaralanması riski taşımadığı için araç içinde sabitlenerek yardım beklenmelidir."
                    }
                },
                {
                    "question": "9-Hasta ya da yaralının ilk değerlendirilmesinde sıralama ne şekilde olmalıdır?",
                    "options": ["A.Bilinç Kontrolü/Solunum Değerlendirilmesi/Hava Yolu Açıklığının Değerlendirilmesi/Dolaşımın Değerlendirilmesi", "B. Bilinç Kontrolü/ Hava Yolu Açıklığının Değerlendirilmesi/Solunum Değerlendirilmesi/Dolaşımın Değerlendirilmesi", "C. Hava Yolu Açıklığının Değerlendirilmesi /Bilinç Kontrolü/Solunum Değerlendirilmesi /Dolaşımın Değerlendirilmesi", "D. Bilinç Kontrolü/Solunum Değerlendirilmesi/ Dolaşımın Değerlendirilmesi /Hava Yolu Açıklığının Değerlendirilmesi"],
                    "answer": "B. Bilinç Kontrolü/ Hava Yolu Açıklığının Değerlendirilmesi/Solunum Değerlendirilmesi/Dolaşımın Değerlendirilmesi",
                    "explanation": "Hasta/yaralının ilk değerlendirilmesinde ABC (Airway-Solunum Yolu, Breathing-Solunum, Circulation-Dolaşım) sırası takip edilir. Bu nedenle doğru sıralama Bilinç Kontrolü, Hava Yolu Açıklığının Değerlendirilmesi, Solunum Değerlendirilmesi ve Dolaşımın Değerlendirilmesidir.",
                    "wrong_explanations": {
                        "A.Bilinç Kontrolü/Solunum Değerlendirilmesi/Hava Yolu Açıklığının Değerlendirilmesi/Dolaşımın Değerlendirilmesi": "Hava yolu açıklığı, solunumdan önce değerlendirilmelidir.",
                        "C. Hava Yolu Açıklığının Değerlendirilmesi /Bilinç Kontrolü/Solunum Değerlendirilmesi /Dolaşımın Değerlendirilmesi": "Bilinç kontrolü, hava yolu açıklığından önce yapılmalıdır.",
                        "D. Bilinç Kontrolü/Solunum Değerlendirilmesi/ Dolaşımın Değerlendirilmesi /Hava Yolu Açıklığının Değerlendirilmesi": "Hava yolu açıklığı, solunum ve dolaşımdan önce değerlendirilmelidir."
                    }
                },
                {
                    "question": "10-Aşağıdakilerden hangisi yılan sokmalarında uygulanacak ilkyardım basamaklarından değildir?",
                    "options": ["A. Yara suyla yıkanır", "B. Turnike uygulanır", "C. Yaraya yakın bölgede baskı yapabilecek eşyalar çıkartılır", "D. Soğuk uygulama yapılır"],
                    "answer": "B. Turnike uygulanır",
                    "explanation": "Yılan sokmalarında turnike uygulanması, zehrin vücutta daha hızlı yayılmasına neden olabilir ve doku hasarını artırabilir. Bu nedenle yılan sokmalarında turnike uygulanmaz.",
                    "wrong_explanations": {
                        "A. Yara suyla yıkanır": "Yılan sokması bölgesini suyla yıkamak, zehrin bir kısmını temizlemeye yardımcı olabilir.",
                        "C. Yaraya yakın bölgede baskı yapabilecek eşyalar çıkartılır": "Yılan sokması bölgesinde şişlik oluşabileceği için baskı yapabilecek eşyalar (yüzük, bilezik vb.) çıkartılmalıdır.",
                        "D. Soğuk uygulama yapılır": "Soğuk uygulama, ağrıyı ve şişliği azaltmaya yardımcı olabilir."
                    }
                },
                {
                    "question": "11-Aşağıdakilerden hangisi Baş boyun yada omurga yaralanmalarında şüphelenilen hastalarda uygulanan sedyeye yerleştirme tekniğidir?",
                    "options": ["A.Rentek", "B.Altınbeşik", "C.Omuzda taşıma", "D.Kütük yuvarlama tekniği"],
                    "answer": "D.Kütük yuvarlama tekniği",
                    "explanation": "Kütük yuvarlama tekniği, baş, boyun ve omurga yaralanmalarından şüphelenilen hastalarda omurga eksenini bozmadan sedyeye yerleştirme tekniğidir.",
                    "wrong_explanations": {
                        "A.Rentek": "Rentek manevrası, trafik kazalarında yaralıyı araçtan çıkarmak için kullanılan bir yöntemdir.",
                        "B.Altınbeşik": "Altınbeşik yöntemi, bilinci açık, yürüyebilen veya kısa mesafede taşınması gereken hafif yaralılar için kullanılan bir taşıma yöntemidir.",
                        "C.Omuzda taşıma": "Omuzda taşıma, genellikle bilinci açık ve hafif yaralılar için kullanılan bir taşıma yöntemidir."
                    }
                },
                {
                    "question": "12-Aşağıdakilerden hangisi dış kanamalarda ilk yapılacak olan ilkyardım uygulamasıdır?",
                    "options": ["A. Bandaj ile sararak basınç uygulanır", "B. Kanayan bölge yukarı kaldırılır", "C.Kanayan yer üzerine temiz bir bez ile bastırılır", "D.Kanayan bölge dışarıda kalacak şekilde hastanın üstü örtülür"],
                    "answer": "C.Kanayan yer üzerine temiz bir bez ile bastırılır",
                    "explanation": "Dış kanamalarda ilk yapılacak olan ilkyardım uygulaması, kanayan yer üzerine temiz bir bez ile bastırmaktır. Bu, kanamayı durdurmak için en hızlı ve etkili yöntemdir.",
                    "wrong_explanations": {
                        "A. Bandaj ile sararak basınç uygulanır": "Bandaj ile sararak basınç uygulamak, ilk baskıdan sonra kanama durmazsa yapılan bir sonraki adımdır.",
                        "B. Kanayan bölge yukarı kaldırılır": "Kanayan bölgeyi yukarı kaldırmak, kan akışını yavaşlatmaya yardımcı olur ancak ilk müdahale değildir.",
                        "D.Kanayan bölge dışarıda kalacak şekilde hastanın üstü örtülür": "Bu, hastayı sıcak tutmak için yapılan bir uygulamadır, kanamayı durdurmak için değildir."
                    }
                },
                {
                    "question": "13-Aşağıdakilerden hangisi delici göğüs yaralanmalarında yapılacak ilkyardım uygulamalarından değildir?",
                    "options": ["A. Yaşam bulguları değerlendirilir", "B. Yara üzeri plastik poşet naylon vb sarılmış bir bezle kapatılır", "C.Hasta yaralının bilinci açıksa şok pozisyonu verilir", "D. Tıbbi yardım istenir"],
                    "answer": "C.Hasta yaralının bilinci açıksa şok pozisyonu verilir",
                    "explanation": "Delici göğüs yaralanmalarında, yaralının bilinci açık olsa bile şok pozisyonu verilmez. Çünkü şok pozisyonu, bacakların yukarı kaldırılmasını gerektirir ve bu durum göğüs yaralanmalarında solunumu zorlaştırabilir. Genellikle yarı oturur pozisyon tercih edilir.",
                    "wrong_explanations": {
                        "A. Yaşam bulguları değerlendirilir": "Yaşam bulgularının değerlendirilmesi, her türlü acil durumda yapılması gereken temel bir adımdır.",
                        "B. Yara üzeri plastik poşet naylon vb sarılmış bir bezle kapatılır": "Delici göğüs yaralanmalarında, hava girişini engellemek için yara hava geçirmeyen bir malzeme ile kapatılmalıdır.",
                        "D. Tıbbi yardım istenir": "Delici göğüs yaralanmaları ciddi durumlardır ve mutlaka tıbbi yardım istenmelidir."
                    }
                },
                {
                    "question": "14-İlkyardımcı ilk muayene ile hasta yaralının yaşam belirtilerinin varlığını güvence altına aldıktan sonra hangi aşamaya geçmelidir?",
                    "options": ["A.2.değerlendirme yapmalı", "B. Koma pozisyonu verilir", "C.Kalp masajı yapmalı", "D.2 kurtarıcı soluk vermeli"],
                    "answer": "A.2.değerlendirme yapmalı",
                    "explanation": "İlk muayenede yaşam belirtileri güvence altına alındıktan sonra, yaralının durumunu daha detaylı anlamak ve diğer yaralanmaları tespit etmek için ikinci değerlendirme yapılmalıdır.",
                    "wrong_explanations": {
                        "B. Koma pozisyonu verilir": "Koma pozisyonu, bilinci kapalı ancak solunumu olan hastalara verilir. Bu, yaşam belirtileri güvence altına alındıktan sonraki bir adımdır, ancak ikinci değerlendirmeden önce değildir.",
                        "C.Kalp masajı yapmalı": "Kalp masajı, kalbi durmuş hastalara yapılır. Yaşam belirtileri güvence altına alındıysa kalp masajına gerek yoktur.",
                        "D.2 kurtarıcı soluk vermeli": "Kurtarıcı soluk, solunumu durmuş hastalara verilir. Yaşam belirtileri güvence altına alındıysa kurtarıcı soluğa gerek yoktur."
                    }
                },
                {
                    "question": "15-Sıvı eksikliği olan hasta ve yaralıda görülen şok çeşidi aşağıdakilerden hangisidir?",
                    "options": ["A. Kardiyojenik şok", "B.Hipovolemik şok", "C.Nörolojik şok", "D.Toksikşok"],
                    "answer": "B.Hipovolemik şok",
                    "explanation": "Hipovolemik şok, vücuttaki kan veya sıvı hacminin yetersiz kalması sonucu oluşan şok türüdür. Bu durum, ciddi kan kaybı, yanıklar veya şiddetli kusma/ishal gibi nedenlerle ortaya çıkabilir.",
                    "wrong_explanations": {
                        "A. Kardiyojenik şok": "Kardiyojenik şok, kalbin yeterince kan pompalayamaması sonucu oluşan şoktur.",
                        "C.Nörolojik şok": "Nörolojik şok, sinir sistemi hasarına bağlı olarak damarların genişlemesi sonucu oluşan şoktur.",
                        "D.Toksikşok": "Toksik şok, enfeksiyon veya zehirlenme sonucu oluşan şoktur."
                    }
                },
                {
                    "question": "16-Bebeklerde yapılacak temel yaşam desteği uygulama sırası ne şekilde olmalıdır?",
                    "options": ["A.Hava yolu açıklığı sağlanması/bilinç kontrolü/soluk verilmesi/kalp masajı", "B.Bilinç kontrolü/Hava yolu açıklığı sağlanması/ kalp masajı soluk verilmesi", "C. Bilinç kontrolü//soluk verilmesi /Hava yolu açıklığı sağlanması/ kalp masajı", "D.Bilinç kontrolü/hava yolu açıklığı sağlanması/bakdinle hisset/soluk verilmesi/kalp masajı"],
                    "answer": "D.Bilinç kontrolü/hava yolu açıklığı sağlanması/bakdinle hisset/soluk verilmesi/kalp masajı",
                    "explanation": "Bebeklerde temel yaşam desteği (TYD) uygulama sırası şu şekildedir: 1. Bilinç kontrolü, 2. Hava yolu açıklığının sağlanması, 3. Solunumun değerlendirilmesi (Bak-Dinle-Hisset), 4. Kurtarıcı soluk, 5. Kalp masajı.",
                    "wrong_explanations": {
                        "A.Hava yolu açıklığı sağlanması/bilinç kontrolü/soluk verilmesi/kalp masajı": "Sıralama yanlıştır. Önce bilinç kontrolü yapılmalıdır.",
                        "B.Bilinç kontrolü/Hava yolu açıklığı sağlanması/ kalp masajı soluk verilmesi": "Sıralama yanlıştır. Soluk vermeden önce solunum değerlendirilmelidir.",
                        "C. Bilinç kontrolü//soluk verilmesi /Hava yolu açıklığı sağlanması/ kalp masajı": "Sıralama yanlıştır. Hava yolu açıklığı solunumdan önce sağlanmalıdır."
                    }
                },
                {
                    "question": "17- Bebeklerde dış kalp masajı aşağıdaki tekniklerin hangisi ile uygulanır?",
                    "options": ["A. Bir elin topuğu ile", "B. Tek parmak ile", "C. İki parmak ile", "D. İki elin topuğu ile"],
                    "answer": "C. İki parmak ile",
                    "explanation": "Bebeklerde dış kalp masajı, iki meme başının altındaki hattın ortasına iki parmak ile uygulanır.",
                    "wrong_explanations": {
                        "A. Bir elin topuğu ile": "Bir elin topuğu ile kalp masajı çocuklarda uygulanır.",
                        "B. Tek parmak ile": "Tek parmak ile kalp masajı yapılmaz.",
                        "D. İki elin topuğu ile": "İki elin topuğu ile kalp masajı yetişkinlerde uygulanır."
                    }
                },
                {
                    "question": "18- Aşağıdakilerden hangisi göze toz gibi küçük madde kaçması durumunda yapılacak ilkyardım uygulamalarından biri değildir?",
                    "options": ["A.Göze hiçbir şekilde dokunulmaz", "B.Hastaya gözünü kırpıştırması söylenir", "C.Nemli temiz bir bez ile çıkartılmaya çalışılır", "D.Göz ışığa doğru çevrilir ve alt göz kapağının içine bakılır"],
                    "answer": "A.Göze hiçbir şekilde dokunulmaz",
                    "explanation": "Göze toz gibi küçük madde kaçması durumunda, göze dokunulmadan hastanın gözünü kırpıştırması söylenir. Eğer çıkmazsa, nemli temiz bir bezle çıkartılmaya çalışılır veya göz ışığa doğru çevrilerek alt göz kapağının içine bakılır. Ancak göze hiçbir şekilde dokunulmaz ifadesi yanlıştır, çünkü temizleme işlemi yapılabilir.",
                    "wrong_explanations": {
                        "B.Hastaya gözünü kırpıştırması söylenir": "Bu, göze yabancı cisim kaçtığında ilk yapılması gerekenlerden biridir.",
                        "C.Nemli temiz bir bez ile çıkartılmaya çalışılır": "Eğer kırpıştırmakla çıkmazsa, nazikçe nemli bir bezle çıkarmaya çalışılabilir.",
                        "D.Göz ışığa doğru çevrilir ve alt göz kapağının içine bakılır": "Bu, yabancı cismin yerini tespit etmek için yapılan bir uygulamadır."
                    }
                },
                {
                    "question": "19-Bebeklerde dış kalp masajı ile ilgili aşağıda verilenlerden hangisi doğrudur?",
                    "options": ["A.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'ü kadar bası uygulanır, dakikada 80 bası", "B.Göğüs kemiği 4 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'ü kadar bası uygulanır dakikada 100 bası", "C.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır, dakikada 80 bası", "D.Göğüs kemiği 4 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'si kadar bası uygulanır, dakikada 100 bası"],
                    "answer": "D.Göğüs kemiği 4 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'si kadar bası uygulanır, dakikada 100 bası",
                    "explanation": "Bebeklerde dış kalp masajı, göğüs kemiği 4 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır ve dakikada 100 bası yapılmalıdır.",
                    "wrong_explanations": {
                        "A.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'ü kadar bası uygulanır, dakikada 80 bası": "Bası derinliği 4 cm, bası sayısı 100 olmalıdır.",
                        "B.Göğüs kemiği 4 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/2'ü kadar bası uygulanır dakikada 100 bası": "Göğüs yüksekliğinin 1/3'ü kadar bası uygulanmalıdır.",
                        "C.Göğüs kemiği 5 cm inecek şekilde yandan bakıldığında göğüs yüksekliğinin 1/3'ü kadar bası uygulanır, dakikada 80 bası": "Bası derinliği 4 cm, bası sayısı 100 olmalıdır."
                    }
                },
                {
                    "question": "20-Aşağıdakilerden hangisi sıcak çarpması belirtilerinden değildir?",
                    "options": ["A. Bulantı kusma", "B.Deride soğukluk hissi", "C.Adele krampları", "D.Davranış bozukluğu"],
                    "answer": "B.Deride soğukluk hissi",
                    "explanation": "Sıcak çarpmasında vücut ısısı yükseldiği için deride sıcaklık ve kuruluk hissedilir. Deride soğukluk hissi, genellikle şok veya hipotermi gibi durumlarda görülür.",
                    "wrong_explanations": {
                        "A. Bulantı kusma": "Bulantı ve kusma, sıcak çarpmasının yaygın belirtilerindendir.",
                        "C.Adele krampları": "Adele krampları, sıcak çarpmasının belirtilerinden biridir.",
                        "D.Davranış bozukluğu": "Davranış bozukluğu, sıcak çarpmasının ciddi belirtilerinden biridir."
                    }
                }
            ]
        },
        "Test 4": {
            "questions": [
                {
                    "question": "1- Hayat kurtarma zincirinin ikinci halkası nedir?",
                    "options": ["A. Sağlık kuruluşuna haber verme", "B. Olay yerinde yapılan temel yaşam desteği", "C. Ambulans ekiplerince yapılan müdahale", "D. Hastane acil servislerinde müdahale"],
                    "answer": "B. Olay yerinde yapılan temel yaşam desteği",
                    "explanation": "Hayat kurtarma zincirinin ikinci halkası, olay yerinde yapılan temel yaşam desteğidir. Bu, solunumu ve/veya kalbi durmuş kişiye yapılan ilk müdahaledir.",
                    "wrong_explanations": {
                        "A. Sağlık kuruluşuna haber verme": "Bu, hayat kurtarma zincirinin birinci halkasıdır.",
                        "C. Ambulans ekiplerince yapılan müdahale": "Bu, hayat kurtarma zincirinin üçüncü halkasıdır.",
                        "D. Hastane acil servislerinde müdahale": "Bu, hayat kurtarma zincirinin dördüncü halkasıdır."
                    }
                },
                {
                    "question": "2-Hasta/yaralının ilk değerlendirmesi aşamasında aşağıdakilerden hangisi öncelikle yapılmalıdır?",
                    "options": ["A.Solunum değerlendirmesi", "B.Ağız içi kontrolü", "C.Bilinç durumunun değerlendirilmesi", "D.Kanamanın değerlendirilmesi"],
                    "answer": "C.Bilinç durumunun değerlendirilmesi",
                    "explanation": "Hasta/yaralının ilk değerlendirmesinde öncelikle bilinç durumu kontrol edilmelidir. Bilinç durumu, diğer yaşamsal fonksiyonların değerlendirilmesi için bir ön koşuldur.",
                    "wrong_explanations": {
                        "A.Solunum değerlendirmesi": "Solunum değerlendirmesi, bilinç kontrolünden sonra yapılır.",
                        "B.Ağız içi kontrolü": "Ağız içi kontrolü, hava yolu açıklığını sağlamak için yapılır ve bilinç kontrolünden sonra gelir.",
                        "D.Kanamanın değerlendirilmesi": "Kanamanın değerlendirilmesi, dolaşım değerlendirmesinin bir parçasıdır ve bilinç kontrolünden sonra yapılır."
                    }
                },
                {
                    "question": "3-Nabız sayısı ile ilgili aşağıda verilen bilgilerden hangisi doğrudur?",
                    "options": ["A. Çocuklarda 140 - 150 dk", "B. Bebeklerde 100-140 dk", "C. Gençlerde 40 - 60 dk", "D. Yetişkinlerde 50 - 100 dk"],
                    "answer": "B. Bebeklerde 100-140 dk",
                    "explanation": "Bebeklerde normal nabız sayısı dakikada 100-140 arasındadır. Çocuklarda 80-100, gençlerde 60-100, yetişkinlerde ise 60-100 arasındadır.",
                    "wrong_explanations": {
                        "A. Çocuklarda 140 - 150 dk": "Çocuklarda normal nabız sayısı 80-100 arasındadır.",
                        "C. Gençlerde 40 - 60 dk": "Gençlerde normal nabız sayısı 60-100 arasındadır.",
                        "D. Yetişkinlerde 50 - 100 dk": "Yetişkinlerde normal nabız sayısı 60-100 arasındadır."
                    }
                },
                {
                    "question": "4- Vücut dokuları için gerekli olan oksijen, besin hormon vb. elemanlar taşıyan ve yeniden geriye toplayan sistem hangisidir?",
                    "options": ["A.Sinir sistemi", "B.Solunum sistemi", "C.Dolaşım sistemi", "D.Boşaltım sistemi"],
                    "answer": "C.Dolaşım sistemi",
                    "explanation": "Dolaşım sistemi, kalp, kan damarları ve kandan oluşur. Vücut dokularına oksijen, besin ve hormonları taşır, atık maddeleri ise uzaklaştırır.",
                    "wrong_explanations": {
                        "A.Sinir sistemi": "Sinir sistemi, vücudun iç ve dış ortamla iletişimini sağlayan, koordinasyon ve kontrolü sağlayan sistemdir.",
                        "B.Solunum sistemi": "Solunum sistemi, vücuda oksijen alıp karbondioksit veren sistemdir.",
                        "D.Boşaltım sistemi": "Boşaltım sistemi, vücuttaki atık maddeleri uzaklaştıran sistemdir."
                    }
                },
                {
                    "question": "5- Yapay solunum ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
                    "options": ["A.Bebeklerde temel yaşam desteğine 2 kurtarıcı soluk ile başlanır.", "B. Yetişkinlerde hasta yaralının göğsünü yükseltmeye yarayacak kadar soluk verilir.", "C. Çocuklarda soluk yoksa burun kapatılarak ağızdan 2 soluk verilir.", "D. Bebek çocuk yetiştinlerde her biri en az 5 saniye süren 2 soluk verilir."],
                    "answer": "D. Bebek çocuk yetiştinlerde her biri en az 5 saniye süren 2 soluk verilir.",
                    "explanation": "Yapay solunumda verilen her soluk 1 saniye sürmelidir, 5 saniye değil. Diğer seçenekler yapay solunum ile ilgili doğru ifadelerdir.",
                    "wrong_explanations": {
                        "A.Bebeklerde temel yaşam desteğine 2 kurtarıcı soluk ile başlanır.": "Bu ifade doğrudur. Bebeklerde TYD 2 kurtarıcı soluk ile başlar.",
                        "B. Yetişkinlerde hasta yaralının göğsünü yükseltmeye yarayacak kadar soluk verilir.": "Bu ifade doğrudur. Yetişkinlerde göğsün yükselmesini sağlayacak kadar soluk verilir.",
                        "C. Çocuklarda soluk yoksa burun kapatılarak ağızdan 2 soluk verilir.": "Bu ifade doğrudur. Çocuklarda soluk yoksa burun kapatılarak ağızdan 2 soluk verilir."
                    }
                },
                {
                    "question": "6- Aşağıdakilerden hangisi ABC nin C sini ifade eder?",
                    "options": ["A.Dolaşımın değerlendirilmesi", "B.Bak dinle hisset ile solunumun değerlendirilmesi", "C. Havayolu açıklığının değerlendirilmesi", "D.Ağız içi kontrolü sağlanması"],
                    "answer": "A.Dolaşımın değerlendirilmesi",
                    "explanation": "ABC, ilk yardımda temel yaşam desteği basamaklarını ifade eder. A: Airway (Hava yolu açıklığı), B: Breathing (Solunum), C: Circulation (Dolaşım). Bu nedenle C, dolaşımın değerlendirilmesini ifade eder.",
                    "wrong_explanations": {
                        "B.Bak dinle hisset ile solunumun değerlendirilmesi": "Bu, B (Breathing) aşamasında yapılan bir değerlendirmedir.",
                        "C. Havayolu açıklığının değerlendirilmesi": "Bu, A (Airway) aşamasında yapılan bir değerlendirmedir.",
                        "D.Ağız içi kontrolü sağlanması": "Ağız içi kontrolü, hava yolu açıklığının sağlanması aşamasında yapılan bir işlemdir."
                    }
                },
                {
                    "question": "7-Aşağıdakilerden hangisi otomatik eksternal defibrilatör (OED-kullanımı ile ilgili doğru bir ifadedir?",
                    "options": ["A.OED'lerin sesli ve görsel komutları yerine getirildiği takdirde hastaya zarar vermez.", "B.2 aylık bebeklerde kullanılmaz", "C.Gebelerde kullanılmaz", "D.Kalp pili olan hastalarda kullanılmaz"],
                    "answer": "A.OED'lerin sesli ve görsel komutları yerine getirildiği takdirde hastaya zarar vermez.",
                    "explanation": "OED cihazları, sesli ve görsel komutlarla kullanıcıyı yönlendirir ve bu komutlara uyulduğu takdirde hastaya zarar vermez. Cihaz, sadece şok gerektiren durumlarda şok verir.",
                    "wrong_explanations": {
                        "B.2 aylık bebeklerde kullanılmaz": "OED, 1 yaşından küçük bebeklerde kullanılmaz, ancak 2 aylık bebeklerde özel pedlerle kullanılabilir.",
                        "C.Gebelerde kullanılmaz": "OED, gebelerde güvenle kullanılabilir.",
                        "D.Kalp pili olan hastalarda kullanılmaz": "Kalp pili olan hastalarda da OED kullanılabilir, ancak pedlerin kalp pilinin üzerine gelmemesine dikkat edilmelidir."
                    }
                },
                {
                    "question": "8- 5 aylık hastada dış kalp masajı nereye uygulanır?",                    "options": ["A.Göğüs kemiğinin 1/5 alt kısmına", "B.Göğüs kemiğinin üst ve alt ucu tespit edilerek alt yarısına", "C.Göğüs kemiğinin 1/3 üst kısmına", "D.İki meme başının birleştirildiği hayali çizginin orta noktasının bir parmak altına"],
                    "answer": "D.İki meme başının birleştirildiği hayali çizginin orta noktasının bir parmak altına",
                    "explanation": "Bebeklerde (0-1 yaş) dış kalp masajı, iki meme başının birleştirildiği hayali çizginin orta noktasının bir parmak altına uygulanır.",
                    "wrong_explanations": {
                        "A.Göğüs kemiğinin 1/5 alt kısmına": "Bu, bebeklerde kalp masajı için doğru bir yer değildir.",
                        "B.Göğüs kemiğinin üst ve alt ucu tespit edilerek alt yarısına": "Bu, yetişkinlerde kalp masajı için doğru bir yerdir.",
                        "C.Göğüs kemiğinin 1/3 üst kısmına": "Bu, bebeklerde kalp masajı için doğru bir yer değildir."
                    }
                },
                {
                    "question": "9- Aşağıdakilerden hangisi bebek hastada Temel Yaşam Desteği uygulaması için doğru bir ifadedir?",
                    "options": ["A.Bebeklerde sadece dış kalp masajı yapılır", "B.Bebeklerde 15 kalp masajı, 5 suni solunum yapılır", "C.İlkyardımcı suni solunum vermek için, ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir", "D.İlkyardımcı bilinci ve solunumu olmayan bebeğin temel yaşam desteğine dış kalp masajı ile başlar sonra suni solunum verir"],
                    "answer": "C.İlkyardımcı suni solunum vermek için, ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir",
                    "explanation": "Bebeklerde suni solunum yapılırken, ilkyardımcı ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir ve her biri 1 saniyeden uzun süren 2 kurtarıcı soluk verir.",
                    "wrong_explanations": {
                        "A.Bebeklerde sadece dış kalp masajı yapılır": "Bebeklerde hem dış kalp masajı hem de suni solunum yapılır.",
                        "B.Bebeklerde 15 kalp masajı, 5 suni solunum yapılır": "Bebeklerde 30 kalp masajı ve 2 suni solunum yapılır.",
                        "D.İlkyardımcı bilinci ve solunumu olmayan bebeğin temel yaşam desteğine dış kalp masajı ile başlar sonra suni solunum verir": "Bebeklerde temel yaşam desteğine 2 kurtarıcı soluk ile başlanır, sonra kalp masajı yapılır."
                    }
                },
                {
                    "question": "10-İlkyardımcı bilinci kapalı Yetişkin hasta/yaralı ile karşılaştığında yalnız ise 112 yi ne zaman aramalıdır?",
                    "options": ["A.Bak dinle hisset yöntemi ile solunum kontrolü yaptıktan sonra", "B.Baş geri çene yukarı pozisyonu verdikten sonra", "C.Temel yaşam desteği uygulamasının 5 tur tekrarından sonra", "D.Temel yaşam desteği uygulamaktan yorulduğu zaman"],
                    "answer": "C.Temel yaşam desteği uygulamasının 5 tur tekrarından sonra",
                    "explanation": "Yetişkinlerde ilkyardımcı yalnız ise, bilinci kapalı hasta/yaralı ile karşılaştığında, temel yaşam desteği uygulamasının 5 tur tekrarından sonra 112'yi aramalıdır. Bu, kesintisiz kalp masajı ve suni solunumun önemini vurgular.",
                    "wrong_explanations": {
                        "A.Bak dinle hisset yöntemi ile solunum controlü yaptıktan sonra": "Solunum kontrolü sonrası hemen 112 aranmaz, temel yaşam desteği başlanır.",
                        "B.Baş geri çene yukarı pozisyonu verdikten sonra": "Hava yolu açıldıktan sonra hemen 112 aranmaz, temel yaşam desteği başlanır.",
                        "D.Temel yaşam desteği uygulamaktan yorulduğu zaman": "Yorulmak bir kriter değildir, 5 tur sonrası aranmalıdır."
                    }
                },
                {
                    "question": "11-Bilinci kapalı çocuk hasta/yaralı ile karşılaşan ilkyardımcı yalnız ise 112 yi ne zaman aramalıdır?",
                    "options": ["A. Bak dinle hisset yöntemi ile solunum kontrolü yaptıktan sonra", "B. Baş geri çene yukarı pozisyonundan sonra", "C. 5 tur Temel yaşam desteği uyguladıktan sonra", "D. Bilinç kontrolünden hemen sonra."],
                    "answer": "C. 5 tur Temel yaşam desteği uyguladıktan sonra",
                    "explanation": "Çocuklarda ilkyardımcı yalnız ise, bilinci kapalı çocuk hasta/yaralı ile karşılaştığında, 5 tur temel yaşam desteği uyguladıktan sonra 112'yi aramalıdır. Bu, kesintisiz kalp masajı ve suni solunumun önemini vurgular.",
                    "wrong_explanations": {
                        "A. Bak dinle hisset yöntemi ile solunum kontrolü yaptıktan sonra": "Solunum kontrolü sonrası hemen 112 aranmaz, temel yaşam desteği başlanır.",
                        "B. Baş geri çene yukarı pozisyonundan sonra": "Hava yolu açıldıktan sonra hemen 112 aranmaz, temel yaşam desteği başlanır.",
                        "D. Bilinç controlünden hemen sonra.": "Bilinç kontrolü sonrası hemen 112 aranmaz, temel yaşam desteği başlanır."
                    }
                },
                {
                    "question": "12-Yetişkinlerde heimlich manevrası hangi bölgeye uygulanır?",
                    "options": ["A.Göğüs kemiği altına gelecek şekilde, midenin üst kısmına", "B.Göğüs kemiğinin 2 parmak üstüne", "C.Göğüs kemiğinin orta kısmına", "D.Göbek deliğinin 2 parmak altına"],
                    "answer": "A.Göğüs kemiği altına gelecek şekilde, midenin üst kısmına",
                    "explanation": "Yetişkinlerde Heimlich manevrası, göğüs kemiği altına gelecek şekilde, midenin üst kısmına uygulanır. Bu, karın bölgesine yapılan baskı ile hava yolunu tıkayan cismin dışarı atılmasını sağlar.",
                    "wrong_explanations": {
                        "B.Göğüs kemiğinin 2 parmak üstüne": "Bu bölge, Heimlich manevrası için doğru değildir.",
                        "C.Göğüs kemiğinin orta kısmına": "Bu bölge, Heimlich manevrası için doğru değildir.",
                        "D.Göbek deliğinin 2 parmak altına": "Bu bölge, Heimlich manevrası için doğru değildir."
                    }
                },
                {
                    "question": "13-Aşagıdakilerden hangisi iç kanaması olan bilinci açık bir hasta yaralıya yapılan müdahaleler arasında yer almaz?",
                    "options": ["A.Hasta yaralının bilinci değerlendirilir.", "B.Yaşamsal bulguları izlenir.", "C.Şok pozisyonu verilir.", "D.Hasta yaralıya ağızdan yiyecek içecek verilir."],
                    "answer": "D.Hasta yaralıya ağızdan yiyecek içecek verilir.",
                    "explanation": "İç kanaması olan bir hastaya ağızdan yiyecek veya içecek verilmemelidir. Bu, kanamayı artırabilir veya başka komplikasyonlara yol açabilir. Diğer seçenekler doğru müdahalelerdir.",
                    "wrong_explanations": {
                        "A.Hasta yaralının bilinci değerlendirilir.": "Bilinç değerlendirmesi, her türlü acil durumda yapılması gereken temel bir adımdır.",
                        "B.Yaşamsal bulguları izlenir.": "Yaşamsal bulguların (nabız, solunum, tansiyon) düzenli olarak izlenmesi, hastanın durumundaki değişiklikleri takip etmek için önemlidir.",
                        "C.Şok pozisyonu verilir.": "İç kanama şoka neden olabileceği için, şok pozisyonu (ayakları 30 cm yukarı kaldırma) uygulanabilir."
                    }
                },
                {
                    "question": "14-Aşagıdakilerden hangisi şoktaki bir hasta yaralıya yapılacak ilk yardım uygulamaları arasında yer almaktadır?",
                    "options": ["A.Hasta yaralının mümkün olduğunca temiz hava soluması sağlanır.", "B.Dolaşımını hızlandırmak için hareket etmesi sağlanır.", "C.Hasta yaralı yan yatırılır", "D. Hasta yaralı soğuk tutulur."],
                    "answer": "A.Hasta yaralının mümkün olduğunca temiz hava soluması sağlanır.",
                    "explanation": "Şoktaki bir hastanın mümkün olduğunca temiz hava soluması sağlanmalıdır. Bu, oksijenlenmeyi artırarak şokun etkilerini azaltmaya yardımcı olur.",
                    "wrong_explanations": {
                        "B.Dolaşımını hızlandırmak için hareket etmesi sağlanır.": "Şoktaki bir hastanın hareket etmesi engellenmelidir. Hareket, kan dolaşımını daha da bozabilir.",
                        "C.Hasta yaralı yan yatırılır": "Şoktaki bir hastaya genellikle sırtüstü yatış pozisyonu verilir ve ayakları 30 cm kadar yükseltilir. Yan yatış pozisyonu, bilinci kapalı ancak solunumu olan hastalara verilir.",
                        "D. Hasta yaralı soğuk tutulur.": "Şoktaki bir hasta sıcak tutulmalıdır. Vücut ısısının düşmesi şoku kötüleştirebilir."
                    }
                },
                {
                    "question": "15- Aşağıdakilerden hangisi şok belirtilerinden biri değildir?",
                    "options": ["A.İdrar ve gaita kaçırma", "B.Hızlı ve zayıf nabız", "C.Hızlı ve yüzeysel solunum", "D. Endişe ve huzursuzluk"],
                    "answer": "A.İdrar ve gaita kaçırma",
                    "explanation": "İdrar ve gaita kaçırma, şokun belirtilerinden biri değildir. Şokta, vücut yaşamsal organlara kan akışını sağlamak için diğer organlardan kanı çeker, bu da idrar üretimini azaltır. Şokun belirtileri arasında hızlı ve zayıf nabız, hızlı ve yüzeysel solunum, endişe ve huzursuzluk bulunur.",
                    "wrong_explanations": {
                        "B.Hızlı ve zayıf nabız": "Hızlı ve zayıf nabız, şokun önemli belirtilerindendir.",
                        "C.Hızlı ve yüzeysel solunum": "Hızlı ve yüzeysel solunum, şokun önemli belirtilerindendir.",
                        "D. Endişe ve huzursuzluk": "Endişe ve huzursuzluk, şokun önemli belirtilerindendir."
                    }
                },
                {
                    "question": "16-Aşagıdakilerden hangisi kanamalar ile ilgili doğru bir ifadedir?",
                    "options": ["A.Toplar damar ven kanamaları küçük kabarcıklar şeklindedir", "B.Atar damar arter kanamaları kalp atımı ile uyumlu olarak kesik kesik kanar", "C. kılcal damar kanamaları açık renklidir ve sızıntı şeklindedir", "D.Toplardamar ven kanamalarında kısa zamanda çok kan kaybedilir"],
                    "answer": "B.Atar damar arter kanamaları kalp atımı ile uyumlu olarak kesik kesik kanar",
                    "explanation": "Atardamar kanamaları, kalp atımı ile uyumlu olarak kesik kesik ve fışkırır tarzda olur. Rengi açık kırmızıdır ve en tehlikeli kanama türüdür.",
                    "wrong_explanations": {
                        "A.Toplar damar ven kanamaları küçük kabarcıklar şeklindedir": "Toplardamar kanamaları sürekli ve koyu renklidir. Küçük kabarcıklar şeklinde olan kanamalar kılcal damar kanamalarıdır.",
                        "C. kılcal damar kanamaları açık renklidir ve sızıntı şeklindedir": "Kılcal damar kanamaları sızıntı şeklinde ve açık renklidir, ancak bu ifade doğrudur.",
                        "D.Toplardamar ven kanamalarında kısa zamanda çok kan kaybedilir": "Kısa zamanda çok kan kaybedilen kanama türü atardamar kanamalarıdır."
                    }
                },
                {
                    "question": "17- Aşağıdakilerden hangisi delici karın yaralanmalarında yapılacak ilk yardım uygulamalarından biridir?",
                    "options": ["A.Hasta yaralının dışarı çıkan organları içeri sokulmaya çalışılır.", "B. Hasta yaralının bilinci açıksa sırtüstü pozisyonda bacaklar bükülerek yatırılır.", "C. Hasta yaralıya ağızdan yiyecek içecek verilir.", "D. Hasta yaralının bilinci açıksa yarı oturur pozisyon verilir."],
                    "answer": "B. Hasta yaralının bilinci açıksa sırtüstü pozisyonda bacaklar bükülerek yatırılır.",
                    "explanation": "Delici karın yaralanmalarında, yaralının bilinci açıksa sırtüstü pozisyonda bacaklar bükülerek yatırılır. Bu pozisyon, karın kaslarını gevşeterek ağrıyı azaltır ve organların dışarı çıkmasını engeller.",
                    "wrong_explanations": {
                        "A.Hasta yaralının dışarı çıkan organları içeri sokulmaya çalışılır.": "Dışarı çıkan organlar asla içeri sokulmaya çalışılmamalıdır. Bu, daha fazla hasara ve enfeksiyona neden olabilir.",
                        "C. Hasta yaralıya ağızdan yiyecek içecek verilir.": "Delici karın yaralanmalarında, yaralıya ağızdan hiçbir şey verilmemelidir.",
                        "D. Hasta yaralının bilinci açıksa yarı oturur pozisyon verilir.": "Yarı oturur pozisyon, delici karın yaralanmalarında karın kaslarını gererek ağrıyı artırabilir ve organların dışarı çıkma riskini artırabilir."
                    }
                },
                {
                    "question": "18-kaza sonucu yoğun ağrı, solunum zorluğu, morarma ve kan tükürme gibi belirtiler görülen bir hasta/yaralıda aşağıdaki hangi yaralanma gerçekleşmiştir?",
                    "options": ["A. Delici karın yaralanması", "B. Kafatası/omurga yaralanması", "C. Ezik yaralanma", "D.Delici göğüs yaralanması"],
                    "answer": "D.Delici göğüs yaralanması",
                    "explanation": "Yoğun ağrı, solunum zorluğu, morarma ve kan tükürme gibi belirtiler delici göğüs yaralanmalarında görülür. Bu tür yaralanmalar akciğerlere veya kalbe zarar verebilir.",
                    "wrong_explanations": {
                        "A. Delici karın yaralanması": "Delici karın yaralanmalarında genellikle karın ağrısı, hassasiyet ve dışarı çıkan organlar görülebilir.",
                        "B. Kafatası/omurga yaralanması": "Kafatası/omurga yaralanmalarında bilinç kaybı, felç, duyu kaybı gibi belirtiler görülebilir.",
                        "C. Ezik yaralanma": "Ezik yaralanmalarda morarma, şişlik ve ağrı görülür, ancak solunum zorluğu ve kan tükürme gibi belirtiler tipik değildir."
                    }
                },
                {
                    "question": "19-Aşağıdakilerden hangisi yara çeşitlerinden değildir?",
                    "options": ["A.Kesik yaralar", "B.Delici yaraalr", "C.Kısmi yaralar", "D.Kirli yaralar"],
                    "answer": "C.Kısmi yaralar",
                    "explanation": "Yara çeşitleri kesik, delici, ezik, parçalı gibi farklı şekillerde sınıflandırılır. Kısmi yara diye bir yara çeşidi yoktur.",
                    "wrong_explanations": {
                        "A.Kesik yaralar": "Kesik yaralar, kesici aletlerle oluşan yara çeşididir.",
                        "B.Delici yaraalr": "Delici yaralar, sivri uçlu cisimlerle oluşan yara çeşididir.",
                        "D.Kirli yaralar": "Kirli yaralar, enfeksiyon riski taşıyan yara çeşididir."
                    }
                },
                {
                    "question": "20-Aşağıdakilerden hangisi kafatası ve omurga yaralanmaları arasında yer almaz?",
                    "options": ["A.Saçlı deride yaralanmalar", "B.Omurga bel kemiği yaralanmaları", "C.Uyluk kemiği yaralanmaları", "D.Yüz yaralanmaları"],
                    "answer": "C.Uyluk kemiği yaralanmaları",
                    "explanation": "Uyluk kemiği yaralanmaları, kafatası ve omurga yaralanmaları arasında yer almaz. Kafatası ve omurga yaralanmaları, baş ve omurga bölgesindeki yaralanmaları kapsar.",
                    "wrong_explanations": {
                        "A.Saçlı deride yaralanmalar": "Saçlı derideki yaralanmalar, kafatası yaralanmaları kapsamında değerlendirilebilir.",
                        "B.Omurga bel kemiği yaralanmaları": "Omurga bel kemiği yaralanmaları, omurga yaralanmalarının önemli bir türüdür.",
                        "D.Yüz yaralanmaları": "Yüz yaralanmaları, kafatası ve omurga yaralanmaları ile birlikte görülebilir ve bu bölgedeki travmalarla ilişkilidir."
                    }
                }
            ]
        },
        "Test 5": {
            "questions": [
                {
                    "question": "1- \"Hasta yaralılara ambulans ve sağlık merkezlerinin acil ünitelerinde doktor veya sağlık personeli tarafından yapılan tıbbi müdahaledir \" ifadesi aşağıdakilerden hangisinin tanımıdır?",
                    "options": ["A- İlk yardım", "B- Acil tedavi", "C- Yoğun bakım", "D- Hepsi"],
                    "answer": "B- Acil tedavi",
                    "explanation": "Verilen tanım, sağlık profesyonelleri tarafından yapılan tıbbi müdahaleyi ifade eder ki bu da acil tedavidir. İlk yardım ise olay yerinde ilaçsız yapılan müdahaledir.",
                    "wrong_explanations": {
                        "A- İlk yardım": "İlk yardım, olay yerinde ilaçsız yapılan müdahaledir.",
                        "C- Yoğun bakım": "Yoğun bakım, hastanede kritik durumdaki hastaların özel olarak takip edildiği ve tedavi edildiği bir birimdir.",
                        "D- Hepsi": "Sadece acil tedavi doğru tanımdır."
                    }
                },
                {
                    "question": "2- Yapay solunum ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
                    "options": ["A- Yetişkin, bebek ve çocuklarda göğsünü yükseltmeye yarayacak kadar nefes verilir", "B- Bebeklerde ciğer dolusu kadar nefes verilir", "C- Çocuklarda ağız dolusu kadar nefes verilir", "D- Bebek- çocuk ve yetişkinlerde her biri en az 5 saniye süren 2 nefes verilir"],
                    "answer": "A- Yetişkin, bebek ve çocuklarda göğsünü yükseltmeye yarayacak kadar nefes verilir",
                    "explanation": "Yapay solunumda, yaş grubuna bakılmaksızın, hastanın göğsünü yükseltmeye yetecek kadar nefes verilmelidir. Ciğer dolusu veya ağız dolusu nefes vermek, akciğerlere zarar verebilir.",
                    "wrong_explanations": {
                        "B- Bebeklerde ciğer dolusu kadar nefes verilir": "Bebeklerde ciğer dolusu nefes vermek akciğerlere zarar verebilir.",
                        "C- Çocuklarda ağız dolusu kadar nefes verilir": "Çocuklarda ağız dolusu nefes vermek akciğerlere zarar verebilir.",
                        "D- Bebek- çocuk ve yetişkinlerde her biri en az 5 saniye süren 2 nefes verilir": "Her bir nefes 1 saniye sürmelidir, 5 saniye değil."
                    }
                },
                {
                    "question": "3- Aşağıdakilerden hangisi olay yerini değerlendirmenin amaçlarından değildir?",
                    "options": ["A- Tekrar kaza yapma riskinin kaldırılması", "B- H/Y sayısının belirlenmesi", "C- Yapılacak müdahelelerin planlanması", "D- Müdahale için 112 ekipleri beklenmeli"],
                    "answer": "D- Müdahale için 112 ekipleri beklenmeli",
                    "explanation": "Olay yerini değerlendirmenin amaçları arasında tekrar kaza riskini ortadan kaldırmak, hasta/yaralı sayısını belirlemek ve yapılacak müdahaleleri planlamak yer alır. Müdahale için 112 ekiplerini beklemek, olay yerini değerlendirmenin bir amacı değildir, aksine değerlendirme yapıldıktan sonra 112 aranır ve beklenir.",
                    "wrong_explanations": {
                        "A- Tekrar kaza yapma riskinin kaldırılması": "Bu, olay yeri güvenliğini sağlamak için önemli bir adımdır.",
                        "B- H/Y sayısının belirlenmesi": "Hasta/yaralı sayısını belirlemek, kaynakları doğru kullanmak ve yardım çağırmak için önemlidir.",
                        "C- Yapılacak müdahelelerin planlanması": "Olay yerindeki duruma göre hangi müdahalelerin yapılacağını planlamak, etkili ilk yardım için gereklidir."
                    }
                },
                {
                    "question": "4- Solunum sayısı ile ilgili aşağıda verilen bilgilerden hangisi doğrudur?",
                    "options": ["A- Çocuklarda 16-22/dk", "B- Bebeklerde 26-34/dk", "C- Gençlerde 22-24 / dk", "D- Yaşlılarda 24-26/dk"],
                    "answer": "A- Çocuklarda 16-22/dk",
                    "explanation": "Çocuklarda normal solunum sayısı dakikada 16-22 arasındadır. Bebeklerde 30-60, gençlerde 12-20, yetişkinlerde ise 12-20 arasındadır.",
                    "wrong_explanations": {
                        "B- Bebeklerde 26-34/dk": "Bebeklerde normal solunum sayısı 30-60 arasındadır.",
                        "C- Gençlerde 22-24 / dk": "Gençlerde normal solunum sayısı 12-20 arasındadır.",
                        "D- Yaşlılarda 24-26/dk": "Yaşlılarda normal solunum sayısı 12-20 arasındadır."
                    }
                },
                {
                    "question": "5- Bir travma sonucu deri ya da mukoza bütünlüğünün bozulması aşağıdakilerden hangisidir?",
                    "options": ["A- Şok", "B- Yara", "C- Zehirlenme", "D- Koma"],
                    "answer": "B- Yara",
                    "explanation": "Yara, bir travma sonucu deri veya mukoza bütünlüğünün bozulması durumudur. Şok, zehirlenme ve koma ise farklı tıbbi durumlardır.",
                    "wrong_explanations": {
                        "A- Şok": "Şok, vücudun yaşamsal organlarına yeterli kan gitmemesi durumudur.",
                        "C- Zehirlenme": "Zehirlenme, vücuda zararlı bir maddenin girmesi sonucu oluşan durumdur.",
                        "D- Koma": "Koma, uzun süreli ve derin bilinç kaybı durumudur."
                    }
                },
                {
                    "question": "6- Zehirli madde içmiş h/y uygulanacak ilk yardım aşağıdakilerden hangisidir?",
                    "options": ["A- Kusturulmalıdır", "B- Bol sıvı içirilmelidir", "C- Yatırılarak dinlendirilmeli ve kendi kendine iyileşmesi beklenmelidir", "D- Ağız zehirli madde ile temas etmişse su ile çalkalanmalıdır"],
                    "answer": "D- Ağız zehirli madde ile temas etmişse su ile çalkalanmalıdır",
                    "explanation": "Zehirli madde içmiş bir hastaya ilk yardımda, eğer ağız zehirli madde ile temas etmişse su ile çalkalanmalıdır. Kusturmak veya bol sıvı içirmek her zaman doğru değildir ve bazı durumlarda zararlı olabilir. Hastanın kendi kendine iyileşmesi beklenmemelidir.",
                    "wrong_explanations": {
                        "A- Kusturulmalıdır": "Bazı zehirli maddeler kusturulduğunda daha fazla zarar verebilir. Kusturma kararı tıbbi profesyoneller tarafından verilmelidir.",
                        "B- Bol sıvı içirilmelidir": "Her zehirlenme durumunda bol sıvı içirmek doğru değildir, bazı durumlarda emilimi hızlandırabilir.",
                        "C- Yatırılarak dinlendirilmeli ve kendi kendine iyileşmesi beklenmelidir": "Zehirlenme ciddi bir durumdur ve tıbbi müdahale gerektirir, kendi kendine iyileşmesi beklenmemelidir."
                    }
                },
                {
                    "question": "7- Aşağıdakilerden hangisi hasta/yaralının taşınmasında yer alan genel kurallardan değildir?",
                    "options": ["A- Hasta/yaralıya yakın mesafede çalışılmalıdır", "B- Hasta/yaralı mümkün olduğunca az hareket ettirilmelidir", "C- Tüm hareketleri yönlendirecek birden fazla sorumlu olmalıdır", "D- Yön değiştirirken ani dönme ve bükülmelerden kaçınılmalıdır"],
                    "answer": "C- Tüm hareketleri yönlendirecek birden fazla sorumlu olmalıdır",
                    "explanation": "Hasta/yaralı taşınırken, tüm hareketleri yönlendirecek tek bir sorumlu olmalıdır. Birden fazla kişinin yönlendirmesi, koordinasyon eksikliğine ve yaralının daha fazla zarar görmesine neden olabilir.",
                    "wrong_explanations": {
                        "A- Hasta/yaralıya yakın mesafede çalışılmalıdır": "Yaralıya yakın mesafede çalışmak, kaldırma ve taşıma sırasında daha iyi kontrol sağlar.",
                        "B- Hasta/yaralı mümkün olduğunca az hareket ettirilmelidir": "Yaralının hareketini kısıtlamak, özellikle omurga yaralanmalarında hayati önem taşır.",
                        "D- Yön değiştirirken ani dönme ve bükülmelerden kaçınılmalıdır": "Ani hareketlerden kaçınmak, yaralının durumunun kötüleşmesini engeller."
                    }
                },
                {
                    "question": "8- Uzuv kopmasında yapılan ilk yardım uygulamalarından hangisi yanlıştır?",
                    "options": ["A- Kopan parça temiz ve su geçirmez, ağzı kapalı plastik torbaya konmalı", "B- Kopan parçanın en geç 6 saat içerisinden sağlık kuruluşuna sevki sağlanmaldır", "C- Kopan parça direkt buz ve su dolu bir torbanın içine konmalıdır", "D- Kopan parçanın içine konduğu torba h/y ile aynı vasıtaya konulmalı ve üzerine adı soyadı yazılmalıdır"],
                    "answer": "C- Kopan parça direkt buz ve su dolu bir torbanın içine konmalıdır",
                    "explanation": "Kopan parça direkt buz veya su dolu bir torbaya konulmamalıdır. Bu, doku hasarını artırabilir. Kopan parça temiz ve su geçirmez bir torbaya konulduktan sonra, bu torba buz içeren başka bir torbanın içine yerleştirilmelidir (direkt temas olmamalıdır).",
                    "wrong_explanations": {
                        "A- Kopan parça temiz ve su geçirmez, ağzı kapalı plastik torbaya konmalı": "Bu, kopan parçanın korunması için doğru bir adımdır.",
                        "B- Kopan parçanın en geç 6 saat içerisinden sağlık kuruluşuna sevki sağlanmaldır": "Kopan parçanın en kısa sürede sağlık kuruluşuna ulaştırılması önemlidir.",
                        "D- Kopan parçanın içine konduğu torba h/y ile aynı vasıtaya konulmalı ve üzerine adı soyadı yazılmalıdır": "Kopan parçanın yaralı ile birlikte aynı vasıtada ve doğru şekilde etiketlenerek gönderilmesi önemlidir."
                    }
                },
                {
                    "question": "9- Yoğun ağrı, şişlik ve kızarıklık, işlev kaybı, eklem bozukluğu belirtileri veren hastada gözlemlenen durum ile ilgili aşağıda verilen şıklardan hangisi doğrudur?",
                    "options": ["A- Kırık", "B- Burkulma", "C- Çıkık", "D- Çökme"],
                    "answer": "C- Çıkık",
                    "explanation": "Yoğun ağrı, şişlik, kızarıklık, işlev kaybı ve eklem bozukluğu belirtileri çıkık durumunda görülür. Çıkık, eklem yüzeylerinin kalıcı olarak birbirinden ayrılmasıdır.",
                    "wrong_explanations": {
                        "A- Kırık": "Kırıkta kemik bütünlüğü bozulur, ancak eklem bozukluğu her zaman görülmez.",
                        "B- Burkulma": "Burkulmada eklem bağları gerilir veya yırtılır, ancak eklem yüzeyleri kalıcı olarak ayrılmaz.",
                        "D- Çökme": "Çökme, genellikle kemiklerde görülen bir durumdur ve eklem bozukluğu ile doğrudan ilişkili değildir."
                    }
                },
                {
                    "question": "10- Hayat kurtarma zincirinin üçüncü halkası nedir?",
                    "options": ["A- Hastane acil servisinin müdahalesi", "B- Sağlık kuruluşuna haber verme", "C- Olay yerinde yapılan temel yaşam desteği", "D- Ambulans ekiplerince yapılan müdahale"],
                    "answer": "D- Ambulans ekiplerince yapılan müdahale",
                    "explanation": "Hayat kurtarma zincirinin halkaları sırasıyla; 1. Sağlık kuruluşuna haber verilmesi, 2. Olay yerinde temel yaşam desteği, 3. Ambulans ekiplerince müdahaleler yapılması, 4. Hastane acil servislerinde müdahale yapılmasıdır.",
                    "wrong_explanations": {
                        "A- Hastane acil servisinin müdahalesi": "Bu, hayat kurtarma zincirinin dördüncü halkasıdır.",
                        "B- Sağlık kuruluşuna haber verme": "Bu, hayat kurtarma zincirinin birinci halkasıdır.",
                        "C- Olay yerinde yapılan temel yaşam desteği": "Bu, hayat kurtarma zincirinin ikinci halkasıdır."
                    }
                },
                {
                    "question": "11- Aşağıdakilerden hangisi kafatası ve omurga yaralanmalarının nedenleri arasında yer alır?",
                    "options": ["A- Zehirlenme", "B- Donma sonucu oluşan yanık", "C- Spor ve iş kazaları", "D- Akrep sokmaları"],
                    "answer": "C- Spor ve iş kazaları",
                    "explanation": "Kafatası ve omurga yaralanmaları genellikle yüksek enerjili travmalar sonucu oluşur. Spor ve iş kazaları bu tür travmaların yaygın nedenlerindendir.",
                    "wrong_explanations": {
                        "A- Zehirlenme": "Zehirlenme, kafatası ve omurga yaralanmalarına doğrudan neden olmaz.",
                        "B- Donma sonucu oluşan yanık": "Donma sonucu oluşan yanık, kafatası ve omurga yaralanmaları ile ilgili değildir.",
                        "D- Akrep sokmaları": "Akrep sokmaları, zehirlenmeye neden olur, kafatası ve omurga yaralanmalarına doğrudan neden olmaz."
                    }
                },
                {
                    "question": "12- Kemik bütünlüğünün bozulduğu ancak deri bütünlüğünün bozulmadan sağlam olarak kaldığı kırık çeşidi hangisidir?",
                    "options": ["A- Kapalı kırık", "B- Açık kırık", "C- Çıkık", "D- Burkulma"],
                    "answer": "A- Kapalı kırık",
                    "explanation": "Kapalı kırık, kemik bütünlüğünün bozulduğu ancak deri bütünlüğünün sağlam kaldığı kırık çeşididir. Açık kırıkta ise deri bütünlüğü de bozulmuştur.",
                    "wrong_explanations": {
                        "B- Açık kırık": "Açık kırıkta kemik bütünlüğü ile birlikte deri bütünlüğü de bozulmuştur.",
                        "C- Çıkık": "Çıkık, eklem yüzeylerinin kalıcı olarak birbirinden ayrılmasıdır, kemik bütünlüğünün bozulması değildir.",
                        "D- Burkulma": "Burkulma, eklem bağlarının gerilmesi veya yırtılmasıdır, kemik bütünlüğünün bozulması değildir."
                    }
                },
                {
                    "question": "13- Aşağıdakilerden hangisi Bayılma belirtilerinden değildir?",
                    "options": ["A- Bacaklarda uyuşma", "B- Üşüme ve terleme", "C- Yavaş ve güçlü nabız", "D- Yüzde solgunluk"],
                    "answer": "C- Yavaş ve güçlü nabız",
                    "explanation": "Bayılma durumunda nabız genellikle hızlı ve zayıf olur, yavaş ve güçlü nabız bayılma belirtisi değildir. Diğer seçenekler bayılmanın yaygın belirtileridir.",
                    "wrong_explanations": {
                        "A- Bacaklarda uyuşma": "Bacaklarda uyuşma, bayılma öncesi veya sırasında görüilebilen bir belirtidir.",
                        "B- Üşüme ve terleme": "Üşüme ve terleme, bayılma öncesi veya sırasında görülebilen bir belirtidir.",
                        "D- Yüzde solgunluk": "Yüzde solgunluk, beyne giden kan akışının azalması nedeniyle görülen bir belirtidir."
                    }
                },
                {
                    "question": "14- Kan şekeri düşen hasta/yaralıya yapılacak ilk yardım uygulamaları ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
                    "options": ["A- Yaşamsal bulguları değerlendirilir", "B- Bilinci açık ise ağızdan şekerli içecekler verilir", "C- Bilinci kapalı ise koma pozisyonu verilir", "D- Bilinci kapalı ise ağızdan şeker verilir"],
                    "answer": "D- Bilinci kapalı ise ağızdan şeker verilir",
                    "explanation": "Kan şekeri düşen (hipoglisemi) ve bilinci kapalı olan bir hastaya ağızdan şeker verilmemelidir. Çünkü bilinci kapalı olduğu için boğulma riski vardır. Bu durumda en yakın sağlık kuruluşuna başvurulmalı veya tıbbi yardım istenmelidir.",
                    "wrong_explanations": {
                        "A- Yaşamsal bulguları değerlendirilir": "Yaşamsal bulguların değerlendirilmesi, her türlü acil durumda yapılması gereken temel bir adımdır.",
                        "B- Bilinci açık ise ağızdan şekerli içecekler verilir": "Bilinci açık olan ve kan şekeri düşen bir hastaya şekerli içecekler verilmesi doğru bir uygulamadır.",
                        "C- Bilinci kapalı ise koma pozisyonu verilir": "Bilinci kapalı olan ancak solunumu olan hastalara koma pozisyonu verilmesi, hava yolunun açık kalmasını sağlar."
                    }
                },
                {
                    "question": "15- Aşağıdakilerden hangisi OED kullanımı ile ilgili yanlış bir ifadedir?",
                    "options": ["A- OED kalp ritim analizi yaparken hastaya dokunulmamalıdır", "B- Şok verildikten sonra hemen bak-dinle-hisset yapılmalıdır", "C-Oed şok verirken hastaya dokunulmamalıdır", "D- Şok sonrası temel yaşam desteğine başlanmalıdır"],
                    "answer": "B- Şok verildikten sonra hemen bak-dinle-hisset yapılmalıdır",
                    "explanation": "OED ile şok verildikten sonra hemen temel yaşam desteğine (kalp masajı ve suni solunum) başlanmalıdır. Bak-dinle-hisset yöntemi, solunumun varlığını değerlendirmek için kullanılır ve şok sonrası hemen yapılmaz.",
                    "wrong_explanations": {
                        "A- OED kalp ritim analizi yaparken hastaya dokunulmamalıdır": "OED kalp ritim analizi yaparken hastaya dokunulmamalıdır, aksi takdirde cihaz yanlış analiz yapabilir.",
                        "C-Oed şok verirken hastaya dokunulmamalıdır": "OED şok verirken hastaya dokunulmamalıdır, aksi takdirde elektrik çarpması riski vardır.",
                        "D- Şok sonrası temel yaşam desteğine başlanmalıdır": "Şok sonrası temel yaşam desteğine başlanması, hayati öneme sahiptir."
                    }
                },
                {
                    "question": "16- Aşağıdakilerden hangisi kanamanın durdurulması için vücutta baskı uygulanacak noktalardan biri değildir?",
                    "options": ["A- Koltuk altı", "B- Kolun üst bölümü", "C- Kürek kemiği", "D- Uyluk"],
                    "answer": "C- Kürek kemiği",
                    "explanation": "Kanamanın durdurulması için vücutta baskı uygulanacak noktalar genellikle atardamarların yüzeye yakın geçtiği yerlerdir. Koltuk altı, kolun üst bölümü ve uyluk bu noktalara örnektir. Kürek kemiği ise baskı noktası değildir.",
                    "wrong_explanations": {
                        "A- Koltuk altı": "Koltuk altı, kanamanın durdurulması için baskı uygulanabilecek noktalardan biridir.",
                        "B- Kolun üst bölümü": "Kolun üst bölümü, kanamanın durdurulması için baskı uygulanabilecek noktalardan biridir.",
                        "D- Uyluk": "Uyluk, kanamanın durdurulması için baskı uygulanabilecek noktalardan biridir."
                    }
                },
                {
                    "question": "17- \"Renksiz, kokusuz havadan hafif ve rahatsız edici olmamakla birlikte hemoglobine bağlanma kapasitesi oksijenden 280 kat fazla olan \" ibaresi aşağıdaki zehirlenme türlerinden hangisini ifade eder?",
                    "options": ["A- Şofben zehirlenmesi", "B- Karbonmonoksit zehirlenmesi", "C- Cilt yolu ile zehirlenme", "D- Sindirim yolu ile zehirlenme"],
                    "answer": "B- Karbonmonoksit zehirlenmesi",
                    "explanation": "Verilen tanım, karbonmonoksit gazının özelliklerini ve zehirlenme mekanizmasını açıklamaktadır. Karbonmonoksit, renksiz, kokusuz ve havadan hafif bir gazdır ve hemoglobine oksijenden çok daha güçlü bağlanarak oksijen taşınmasını engeller.",
                    "wrong_explanations": {
                        "A- Şofben zehirlenmesi": "Şofben zehirlenmesi, genellikle karbonmonoksit zehirlenmesi sonucu oluşur, ancak tanım doğrudan karbonmonoksit gazını ifade eder.",
                        "C- Cilt yolu ile zehirlenme": "Cilt yolu ile zehirlenme, zehirli maddenin deri yoluyla emilmesiyle oluşur.",
                        "D- Sindirim yolu ile zehirlenme": "Sindirim yolu ile zehirlenme, zehirli maddenin ağız yoluyla alınmasıyla oluşur."
                    }
                },
                {
                    "question": "18- Suda boğulmalarla ilgili olarak aşağıdaki ifadelerden hangisi doğrudur?",
                    "options": ["A- Boğulma sırasında çok fazla miktarda su akciğerlere girer", "B- Soğuk havalarda 20-30 dk. geçse bile yapay solunum ve kalp masajına başlanmalıdır", "C- Hasta sudan çıkarılmadan herhangi bir müdahalede bulunulmamalıdır", "D- Suda başın çok fazla arkaya itilerek soluk verilmesi gereklidir"],
                    "answer": "B- Soğuk havalarda 20-30 dk. geçse bile yapay solunum ve kalp masajına başlanmalıdır",
                    "explanation": "Soğuk havalarda boğulma vakalarında, vücut ısısının düşmesi metabolizmayı yavaşlattığı için beyin hasarı riski azalır. Bu nedenle, uzun süre geçmiş olsa bile yapay solunum ve kalp masajına başlanmalıdır.",
                    "wrong_explanations": {
                        "A- Boğulma sırasında çok fazla miktarda su akciğerlere girer": "Boğulma sırasında akciğerlere genellikle az miktarda su girer, asıl sorun laringospazm (gırtlak spazmı) nedeniyle hava yolunun kapanmasıdır.",
                        "C- Hasta sudan çıkarılmadan herhangi bir müdahalede bulunulmamalıdır": "Hasta sudan çıkarılmadan da temel yaşam desteği uygulamalarına başlanabilir, özellikle sığ sularda.",
                        "D- Suda başın çok fazla arkaya itilerek soluk verilmesi gereklidir": "Suda başın çok fazla arkaya itilmesi, omurilik yaralanması riskini artırabilir. Baş-çene pozisyonu dikkatli verilmelidir."
                    }
                },
                {
                    "question": "19- Çocuklarda temel yaşam desteği uygulamasında kalp bası yeri neresidir?",
                    "options": ["A- Göğüs kemiğinin alt ve üstü ucunun ortası", "B- İki meme başının altındaki hattın ortası", "C- Göğüs kemiğinin alt yarısı", "D- Göğüs kemiğinin üst yarısı"],
                    "answer": "B- İki meme başının altındaki hattın ortası",
                    "explanation": "Çocuklarda temel yaşam desteği uygulamasında kalp bası yeri, iki meme başının altındaki hattın ortasıdır. Bu bölge, kalbin en etkili şekilde sıkıştırılabileceği yerdir.",
                    "wrong_explanations": {
                        "A- Göğüs kemiğinin alt ve üstü ucunun ortası": "Bu, yetişkinlerde kalp masajı için doğru bir yerdir.",
                        "C- Göğüs kemiğinin alt yarısı": "Bu, çocuklarda kalp masajı için doğru bir yer değildir.",
                        "D- Göğüs kemiğinin üst yarısı": "Bu, çocuklarda kalp masajı için doğru bir yer değildir."
                    }
                },
                {
                    "question": "20- Aşağıdakilerden hangisi birinci derece donuğun belirtilerinden değildir?",
                    "options": ["A- Ödem, şişkinlik, ağrı ve içi su dolu kabarcıklar meydana gelir", "B- Deride solukluk, soğukluk hissi olur", "C- Kızarıklık ve iğnelenme hissi oluşur", "D- Uyuşukluk ve halsizlik görülür"],
                    "answer": "A- Ödem, şişkinlik, ağrı ve içi su dolu kabarcıklar meydana gelir",
                    "explanation": "Ödem, şişkinlik, ağrı ve içi su dolu kabarcıklar ikinci derece donuğun belirtileridir. Birinci derece donukta deride solukluk, soğukluk hissi, kızarıklık, iğnelenme hissi, uyuşukluk ve halsizlik görülür.",
                    "wrong_explanations": {
                        "B- Deride solukluk, soğukluk hissi olur": "Bu, birinci derece donuğun belirtilerindendir.",
                        "C- Kızarıklık ve iğnelenme hissi oluşur": "Bu, birinci derece donuğun belirtilerindendir.",
                        "D- Uyuşukluk ve halsizlik görülür": "Bu, birinci derece donuğun belirtilerindendir."
                    }
                }
            ]
        },
        "Test 6": {
            "questions": [
                {
                    "question": "1-Aşağıdakilerden hangisi sıcak çarpmasında bilinci açık hasta/yaralıya uygulanacak doğru ilkyardım uygulamasıdır?",
                    "options": ["A.Bir litre suya 5 çay kaşığı karbonat ve 5 çay kaşığı tuz karıştırılarak içirilir.", "B.Sıcak içecekler verilir.", "C.Tüm vücut su-buz karışımıyla en az 15-20 dakika yıkanır.", "D.Serin ve havadar bir yere alınır."],
                    "answer": "D.Serin ve havadar bir yere alınır.",
                    "explanation": "Sıcak çarpmasında bilinci açık hastaya serin ve havadar bir yere alınarak vücut ısısının düşürülmesi sağlanır. Diğer uygulamalar yanlış veya tehlikeli olabilir.",
                    "wrong_explanations": {
                        "A.Bir litre suya 5 çay kaşığı karbonat ve 5 çay kaşığı tuz karıştırılarak içirilir.": "Bu tür bir karışım sıcak çarpmasında verilmemelidir, elektrolit dengesini bozabilir.",
                        "B.Sıcak içecekler verilir.": "Sıcak çarpmasında hastanın vücut ısısını daha da artıracağı için sıcak içecekler verilmemelidir.",
                        "C.Tüm vücut su-buz karışımıyla en az 15-20 dakika yıkanır.": "Ani ve aşırı soğutma, şoka neden olabilir. Ilık su ile ıslatılmış bezlerle silme daha uygundur."
                    }
                },
                {
                    "question": "2-Aşağıdakilerden hangisi hayat kurtarma zincirine ait değildir?",
                    "options": ["A.Sağlık kuruluşuna haber verilmesi", "B.Hastane acil servislerinde müdahale yapılması", "C.Olay yerinde temel yaşam desteği yapılması", "D.Yoğun bakım ünitelerinde yapılan tedavi"],
                    "answer": "D.Yoğun bakım ünitelerinde yapılan tedavi",
                    "explanation": "Hayat kurtarma zinciri; 1. Sağlık kuruluşuna haber verilmesi, 2. Olay yerinde temel yaşam desteği, 3. Ambulans ekiplerince müdahale, 4. Hastane acil servislerinde müdahale halkalarından oluşur. Yoğun bakım ünitelerindeki tedavi bu zincirin bir parçası değildir.",
                    "wrong_explanations": {
                        "A.Sağlık kuruluşuna haber verilmesi": "Sağlık kuruluşuna haber verilmesi, hayat kurtarma zincirinin ilk ve en önemli halkalarından biridir.",
                        "B.Hastane acil servislerinde müdahale yapılması": "Hastane acil servislerinde yapılan müdahale, hayat kurtarma zincirinin dördüncü halkasıdır.",
                        "C.Olay yerinde temel yaşam desteği yapılması": "Olay yerinde temel yaşam desteği yapılması, hayat kurtarma zincirinin ikinci halkasıdır."
                    }
                },
                {
                    "question": "3-Aşağıdakilerden hangisinde baş-boyun-gövde ekseninin bozulmamasına özellikle dikkat edilmelidir?",
                    "options": ["A.Kafatası ve omurga yaralanmalarında", "B.İç kanaması olan hastalarda", "C.Bacak kırıklarında", "D.Kedi, köpek ısırmalarında"],
                    "answer": "A.Kafatası ve omurga yaralanmalarında",
                    "explanation": "Kafatası ve omurga yaralanmalarında, omurilik hasarını önlemek için baş-boyun-gövde ekseninin bozulmamasına azami dikkat gösterilmelidir. Diğer durumlarda bu kadar kritik değildir.",
                    "wrong_explanations": {
                        "B.İç kanaması olan hastalarda": "İç kanaması olan hastalarda şok pozisyonu gibi müdahaleler önemlidir, ancak omurga ekseninin korunması birincil öncelik değildir.",
                        "C.Bacak kırıklarında": "Bacak kırıklarında kırık bölgenin sabitlenmesi önemlidir, ancak baş-boyun-gövde ekseninin korunması bu kadar kritik değildir.",
                        "D.Kedi, köpek ısırmalarında": "Kedi, köpek ısırmalarında yara temizliği ve enfeksiyon önleme önemlidir, omurga ekseni ile ilgili bir durum değildir."
                    }
                },
                {
                    "question": "4-Cilt yolu ile zehirlenmelerde yapılan ilkyardım uygulamaları ile ilgili aşağıdakilerden hangisi yanlıştır?",
                    "options": ["A.15-20 dakika boyunca deri bol suyla yıkanmalıdır.", "B.Zehir bulaşmış giysiler çıkartılmaz.", "C.Ellerin zehirli madde ile teması önlenmelidir.", "D.Yaşam bulguları değerlendirilir."],
                    "answer": "B.Zehir bulaşmış giysiler çıkartılmaz.",
                    "explanation": "Cilt yolu ile zehirlenmelerde zehir bulaşmış giysiler hemen çıkartılmalıdır. Giysiler zehirli maddeyi deriye temas ettirmeye devam ederek zehirlenmeyi artırabilir.",
                    "wrong_explanations": {
                        "A.15-20 dakika boyunca deri bol suyla yıkanmalıdır.": "Deriye temas eden zehirli madde bol suyla yıkanarak uzaklaştırılmalıdır.",
                        "C.Ellerin zehirli madde ile teması önlenmelidir.": "İlkyardımcı kendi güvenliğini sağlamak için zehirli madde ile temastan kaçınmalıdır.",
                        "D.Yaşam bulguları değerlendirilir.": "Her türlü acil durumda olduğu gibi, zehirlenmelerde de yaşam bulguları değerlendirilmelidir."
                    }
                },
                {
                    "question": "5-Yetişkinlerde uygulanan kalp masajı ritmi dakikada kaç olmalıdır?",
                    "options": ["A.60/dk", "B.80/dk", "C.30/dk", "D.100/dk"],
                    "answer": "D.100/dk",
                    "explanation": "Yetişkinlerde uygulanan kalp masajı ritmi dakikada 100 bası olmalıdır. Bu, etkili bir dolaşım sağlamak için gerekli olan minimum bası sayısıdır.",
                    "wrong_explanations": {
                        "A.60/dk": "60/dk, yetişkinlerde normal nabız sayısıdır, kalp masajı ritmi değildir.",
                        "B.80/dk": "80/dk, kalp masajı için yeterli bir ritim değildir.",
                        "C.30/dk": "30/dk, kalp masajı ve suni solunum oranıdır (30 bası, 2 soluk), ritim değildir."
                    }
                },
                {
                    "question": "6-Hasta/yaralı taşınmasıyla ilgili olarak aşağıdaki ifadelerden hangisi yanlıştır?",
                    "options": ["A.Hasta/yaralı mümkün olduğunca az hareket ettirilmeli", "B.Hasta/yaralıya yakın mesafede çalışılmalı", "C.Hasta/yaralı taşınırken ekip çalışması yapılmalı", "D.Hasta/yaralı en az dört destek noktasından kavranmak"],
                    "answer": "D.Hasta/yaralı en az dört destek noktasından kavranmak",
                    "explanation": "Hasta/yaralı taşınırken, yaralının durumuna göre uygun taşıma tekniği seçilmeli ve genellikle üç destek noktasından kavranmalıdır. Dört destek noktası her zaman gerekli veya mümkün olmayabilir.",
                    "wrong_explanations": {
                        "A.Hasta/yaralı mümkün olduğunca az hareket ettirilmeli": "Yaralının hareketini kısıtlamak, özellikle omurga yaralanmalarında hayati önem taşır.",
                        "B.Hasta/yaralıya yakın mesafede çalışılmalı": "Yaralıya yakın mesafede çalışmak, kaldırma ve taşıma sırasında daha iyi kontrol sağlar.",
                        "C.Hasta/yaralı taşınırken ekip çalışması yapılmalı": "Ekip çalışması, yaralının güvenli bir şekilde taşınması için önemlidir."
                    }
                },
                {
                    "question": "7-Çocuklarda yapılacak temel yaşam desteği uygulama sırala ması aşağıdakilerden hangisinde doğru olarak verilmiştir?",
                    "options": ["A.Hava yolu açıklığı sağlanması/ Bilinç kontrolü/ Soluk verilmesi/ Kalp masajı", "B.Bilinç kontrolü/ Soluk verilmesi/ Hava yolu açıklığı sağlanması/ Kalp masajı", "C.Bilinç kontrolü/ Hava yolu açıklığı sağlanması/ Kalp masajı/ Soluk verilmesi", "D.Bilinç kontrolü/Hava yolu açıklığı sağlanması/ Bak-Dinle-Hisset/ Soluk verilmesi/ Kalp masajı"],
                    "answer": "D.Bilinç kontrolü/Hava yolu açıklığı sağlanması/ Bak-Dinle-Hisset/ Soluk verilmesi/ Kalp masajı",
                    "explanation": "Çocuklarda temel yaşam desteği (TYD) uygulama sırası şu şekildedir: 1. Bilinç kontrolü, 2. Hava yolu açıklığının sağlanması, 3. Solunumun değerlendirilmesi (Bak-Dinle-Hisset), 4. Kurtarıcı soluk, 5. Kalp masajı.",
                    "wrong_explanations": {
                        "A.Hava yolu açıklığı sağlanması/ Bilinç kontrolü/ Soluk verilmesi/ Kalp masajı": "Sıralama yanlıştır. Önce bilinç kontrolü yapılmalıdır.",
                        "B.Bilinç kontrolü/ Soluk verilmesi/ Hava yolu açıklığı sağlanması/ Kalp masajı": "Sıralama yanlıştır. Soluk vermeden önce hava yolu açıklığı sağlanmalı ve solunum değerlendirilmelidir.",
                        "C.Bilinç kontrolü/ Hava yolu açıklığı sağlanması/ Kalp masajı/ Soluk verilmesi": "Sıralama yanlıştır. Kalp masajından önce solunum değerlendirilmeli ve gerekirse kurtarıcı soluk verilmelidir."
                    }
                },
                {
                    "question": "8-Suda boğulmalarla ilgili olarak aşağıdaki ifadelerden hangisi doğrudur?",
                    "options": ["A.Boğulma sırasında çok fazla miktarda su akciğerlere girer.", "B.Soğuk havalarda 20-30 dk. geçse bile yapay solunum ve kalp masajına başlanmalıdır.", "C.Hasta sudan çıkarılmadan herhangi bir müdahalede bulunulmamalıdır.", "D.Suda başın çok fazla arkaya itilerek soluk verilmesi gereklidir."],
                    "answer": "B.Soğuk havalarda 20-30 dk. geçse bile yapay solunum ve kalp masajına başlanmalıdır.",
                    "explanation": "Soğuk havalarda boğulma vakalarında, vücut ısısının düşmesi metabolizmayı yavaşlattığı için beyin hasarı riski azalır. Bu nedenle, uzun süre geçmiş olsa bile yapay solunum ve kalp masajına başlanmalıdır.",
                    "wrong_explanations": {
                        "A.Boğulma sırasında çok fazla miktarda su akciğerlere girer.": "Boğulma sırasında akciğerlere genellikle az miktarda su girer, asıl sorun laringospazm (gırtlak spazmı) nedeniyle hava yolunun kapanmasıdır.",
                        "C.Hasta sudan çıkarılmadan herhangi bir müdahalede bulunulmamalıdır.": "Hasta sudan çıkarılmadan da temel yaşam desteği uygulamalarına başlanabilir, özellikle sığ sularda.",
                        "D.Suda başın çok fazla arkaya itilerek soluk verilmesi gereklidir.": "Suda başın çok fazla arkaya itilmesi, omurilik yaralanması riskini artırabilir. Baş-çene pozisyonu dikkatli verilmelidir."
                    }
                },
                {
                    "question": "9-Dirsekten el bileğine kadar olan bölgede sıcak su ile meydana gelen ikinci derece yanığa yapılacak ilkyardım aşağıdakilerden hangisidir?",
                    "options": ["A.Yanık bölge 20 dakika soğuk su altında tutulur.", "B.Yanık üzerine yanık kremi sürülür.", "C.Varsa su toplamış yerler patlatılır.", "D.Hasta/yaralının tüm giysileri çıkarılır."],
                    "answer": "A.Yanık bölge 20 dakika soğuk su altında tutulur.",
                    "explanation": "İkinci derece yanıklarda, yanık bölge en az 20 dakika boyunca soğuk su altında tutulmalıdır. Bu, yanığın ilerlemesini durdurur ve ağrıyı azaltır. Yanık kremi sürmek, su toplamış yerleri patlatmak veya giysileri çıkarmak yanlış uygulamalardır.",
                    "wrong_explanations": {
                        "B.Yanık üzerine yanık kremi sürülür.": "Yanık kremi veya benzeri maddeler sürmek, yanığın değerlendirilmesini zorlaştırabilir ve enfeksiyon riskini artırabilir.",
                        "C.Varsa su toplamış yerler patlatılır.": "Su toplamış yerler (bül) patlatılmamalıdır, çünkü bu enfeksiyon riskini artırır.",
                        "D.Hasta/yaralının tüm giysileri çıkarılır.": "Yanık bölgesine yapışmış giysiler çıkarılmamalıdır, aksi takdirde deriye zarar verilebilir."
                    }
                },
                {
                    "question": "10-Aşağıdakilerden hangisi burkulma belirtilerinden değildir?",
                    "options": ["A.Ağrı", "B.Kızarma ve şişlik", "C.İşlev kaybı", "D.Şekil bozukluğu"],
                    "answer": "D.Şekil bozukluğu",
                    "explanation": "Burkulma, eklem bağlarının gerilmesi veya yırtılmasıdır. Şekil bozukluğu genellikle kırık veya çıkık gibi daha ciddi yaralanmalarda görülür. Burkulmanın belirtileri ağrı, kızarma, şişlik ve işlev kaybıdır.",
                    "wrong_explanations": {
                        "A.Ağrı": "Ağrı, burkulmanın en yaygın belirtilerinden biridir.",
                        "B.Kızarma ve şişlik": "Kızarma ve şişlik, burkulma bölgesinde görülen iltihabi reaksiyonlardır.",
                        "C.İşlev kaybı": "İşlev kaybı, burkulma nedeniyle eklemin normal hareketini yapamaması durumudur."
                    }
                },
                {
                    "question": "11-Kalp masajı ve yapay solunuma ne zaman son verilir?",
                    "options": ["A.5 dakika yapıldıktan sonra", "B.Tıbbi yardım gelince", "C.30 dakika yapıldıktan sonra", "D.5 tur yaptıktan sonra"],
                    "answer": "B.Tıbbi yardım gelince",
                    "explanation": "Kalp masajı ve yapay solunum, tıbbi yardım gelene kadar veya hasta/yaralı kendiliğinden solunum ve dolaşım belirtileri gösterene kadar kesintisiz olarak devam ettirilmelidir. Belirli bir süre veya tur sayısı ile sınırlı değildir.",
                    "wrong_explanations": {
                        "A.5 dakika yapıldıktan sonra": "Kalp masajı ve yapay solunum belirli bir süre ile sınırlı değildir.",
                        "C.30 dakika yapıldıktan sonra": "Kalp masajı ve yapay solunum belirli bir süre ile sınırlı değildir.",
                        "D.5 tur yaptıktan sonra": "Kalp masajı ve yapay solunum belirli bir tur sayısı ile sınırlı değildir."
                    }
                },
                                {
                                    "question": "12-Aşağıdakilerden hangisi koma belirtisidir?",
                                    "options": ["A.Üşüme", "B.Baş dönmesi", "C.Bacaklarda uyuşma hissi", "D.Yutkunma ve öksürük reflekslerinin kaybolması"],
                                    "answer": "D.Yutkunma ve öksürük reflekslerinin kaybolması",
                                    "explanation": "Koma, derin bilinç kaybı durumudur ve yutkunma, öksürük gibi reflekslerin kaybolmasıyla karakterizedir. Üşüme, baş dönmesi ve bacaklarda uyuşma hissi genellikle bayılma veya başka durumların belirtileridir.",
                                    "wrong_explanations": {
                                        "A.Üşüme": "Üşüme, koma belirtisi değildir, genellikle bayılma veya şok durumlarında görülür.",
                                        "B.Baş dönmesi": "Baş dönmesi, koma belirtisi değildir, genellikle bayılma veya başka durumların belirtisidir.",
                                        "C.Bacaklarda uyuşma hissi": "Bacaklarda uyuşma hissi, koma belirtisi değildir, genellikle bayılma veya başka durumların belirtisidir."
                                    }
                                },                {
                    "question": "13-Kalp kökenli gelişen şok çeşidi aşağıdakilerden hangisidir?",
                    "options": ["A.Hipovolemik şok", "B.Anaflaktik şok", "C.Kardiyojenik şok", "D.Toksik şok"],
                    "answer": "C.Kardiyojenik şok",
                    "explanation": "Kardiyojenik şok, kalbin yeterince kan pompalayamaması sonucu oluşan şok türüdür. Hipovolemik şok sıvı kaybına, anaflaktik şok alerjik reaksiyona, toksik şok ise zehirlenmeye bağlı gelişir.",
                    "wrong_explanations": {
                        "A.Hipovolemik şok": "Hipovolemik şok, vücuttaki sıvı kaybına bağlı olarak gelişen şoktur.",
                        "B.Anaflaktik şok": "Anaflaktik şok, alerjik reaksiyona bağlı olarak gelişen şoktur.",
                        "D.Toksik şok": "Toksik şok, zehirlenmeye bağlı olarak gelişen şoktur."
                    }
                },                {
                    "question": "14-Kedi-köpek gibi hayvan ısırmalarında yapılacak ilkyardım uygulaması aşağıdakilerden hangisidir?",
                    "options": ["A.Isırılan bölge 5 dk.boyunca su ve sabunla yıkanır.", "B.Isırılan bölgeye sıcak uygulama yapılır.", "C.Isırılan bölgeye merhem sürülür.", "D.Isırılan bölgeye turnike uygulanır."],
                    "answer": "A.Isırılan bölge 5 dk.boyunca su ve sabunla yıkanır.",
                    "explanation": "Kedi-köpek gibi hayvan ısırmalarında, ısırılan bölge enfeksiyon riskini azaltmak için en az 5 dakika boyunca su ve sabunla yıkanmalıdır. Diğer uygulamalar yanlış veya zararlı olabilir.",
                    "wrong_explanations": {
                        "B.Isırılan bölgeye sıcak uygulama yapılır.": "Sıcak uygulama, enfeksiyon riskini artırabilir.",
                        "C.Isırılan bölgeye merhem sürülür.": "Merhem sürmek, yaranın temizlenmesini zorlaştırabilir ve enfeksiyon riskini artırabilir.",
                        "D.Isırılan bölgeye turnike uygulanır.": "Turnike uygulaması, kan dolaşımını engelleyerek doku hasarına neden olabilir ve hayvan ısırmalarında genellikle önerilmez."
                    }
                },
                {
                    "question": "15-İlkyardım ve acil tedavi arasındaki farklarla ilgili aşağıdaki bilgilerden hangisi doğrudur?",
                    "options": ["A.İlkyardım ilaçla yapılan, acil tedavi ilaçsız yapılan müdahalelerdir", "B.İlkyardım mevcut araç ve gereçlerle, acil tedavi gerekli donanımla yapılır.", "C.İlkyardım acil ünitelerinde, acil tedavi olayın olduğu yerde ilaçsız yapılır.", "D.İlkyardımı sağlık personeli, acil tedaviyi ise herkes yapabilir."],
                    "answer": "B.İlkyardım mevcut araç ve gereçlerle, acil tedavi gerekli donanımla yapılır.",
                    "explanation": "İlkyardım, olay yerinde mevcut araç ve gereçlerle, ilkyardım eğitimi almış kişilerce yapılan ilaçsız müdahalelerdir. Acil tedavi ise sağlık personeli tarafından gerekli donanımla yapılan tıbbi müdahalelerdir.",
                    "wrong_explanations": {
                        "A.İlkyardım ilaçla yapılan, acil tedavi ilaçsız yapılan müdahalelerdir": "Bu ifade yanlıştır. İlkyardım ilaçsız, acil tedavi ise ilaçla yapılan müdahalelerdir.",
                        "C.İlkyardım acil ünitelerinde, acil tedavi olayın olduğu yerde ilaçsız yapılır.": "Bu ifade yanlıştır. İlkyardım olayın olduğu yerde, acil tedavi ise acil ünitelerinde yapılır.",
                        "D.İlkyardımı sağlık personeli, acil tedaviyi ise herkes yapabilir.": "Bu ifade yanlıştır. İlkyardımı herkes yapabilir, acil tedaviyi ise sağlık personeli yapar."
                    }
                },
                {
                    "question": "16-Vücut ısısı kaç derecenin altına düşerse ölümcül olur?",
                    "options": ["A.37,5 °C", "B.36,5°C", "C.31°C", "D.39°C"],
                    "answer": "C.31°C",
                    "explanation": "Vücut ısısı 31°C'nin altına düştüğünde hipotermi riski artar ve ölümcül olabilir. Normal vücut ısısı 36.5-37.5°C arasındadır.",
                    "wrong_explanations": {
                        "A.37,5 °C": "Bu, normal vücut ısısının üst sınırıdır.",
                        "B.36,5°C": "Bu, normal vücut ısısının alt sınırıdır.",
                        "D.39°C": "Bu, yüksek ateş durumudur, ölümcül hipotermi değildir."
                    }
                },
                {
                    "question": "17-Hava yolu kısmi olarak tıkanmış hasta/yaralıda aşağıdakilerden hangisi görülür?",
                    "options": ["A.Öksürebilir.", "B.Nefes alamaz.", "C.Konuşamaz.", "D.Rengi morarmıştır."],
                    "answer": "A.Öksürebilir.",
                    "explanation": "Hava yolu kısmi olarak tıkanmış bir hasta/yaralıda kişi öksürebilir, konuşabilir ve nefes alabilir. Tam tıkanmada ise kişi nefes alamaz, konuşamaz ve öksüremez, rengi morarır.",
                    "wrong_explanations": {
                        "B.Nefes alamaz.": "Nefes alamama, tam tıkanmanın belirtisidir.",
                        "C.Konuşamaz.": "Konuşamama, tam tıkanmanın belirtisidir.",
                        "D.Rengi morarmıştır.": "Rengi morarma, tam tıkanmanın belirtisidir."
                    }
                },
                {
                    "question": "18-Aşağıdakilerden hangisi kan şekerinin düşmesi sonucu ortaya çıkan belirtilerden değildir?",
                    "options": ["A.Baş ağrısı", "B.Görme bozukluğu", "C.Yüksek ateş", "D.Konuşma güçlüğü"],
                    "answer": "C.Yüksek ateş",
                    "explanation": "Yüksek ateş, kan şekerinin düşmesi (hipoglisemi) sonucu ortaya çıkan bir belirti değildir. Kan şekerinin düşmesi durumunda baş ağrısı, görme bozukluğu, konuşma güçlüğü, terleme, titreme gibi belirtiler görülebilir.",
                    "wrong_explanations": {
                        "A.Baş ağrısı": "Baş ağrısı, kan şekeri düşüklüğünün yaygın belirtilerindendir.",
                        "B.Görme bozukluğu": "Görme bozukluğu, kan şekeri düşüklüğünün belirtilerindendir.",
                        "D.Konuşma güçlüğü": "Konuşma güçlüğü, kan şekeri düşüklüğünün belirtilerindendir."
                    }
                },
                {
                    "question": "19-Aşağıdakilerden hangisi kırık çıkık ve burkulmalarda tespit sırasında dikkat edilmesi gereken hususlardan biri değildir?",
                    "options": ["A.Tespit edilecek bölge önce yumuşak malzeme ile kaplanmalı", "B.Yara varsa üzeri temiz bir bezle kapatılmalı", "C.Yaralanan bölgenin pozisyonu düzeltildikten sonra tespit edilmeli", "D.Tespit yapılırken yaralı bölge sabit tutulmalı"],
                    "answer": "C.Yaralanan bölgenin pozisyonu düzeltildikten sonra tespit edilmeli",
                    "explanation": "Kırık, çıkık ve burkulmalarda yaralanan bölgenin pozisyonu düzeltilmeye çalışılmamalıdır. Bu, daha fazla hasara neden olabilir. Tespit, yaralı bölge bulunduğu pozisyonda sabit tutularak yapılmalıdır.",
                    "wrong_explanations": {
                        "A.Tespit edilecek bölge önce yumuşak malzeme ile kaplanmalı": "Tespit sırasında yumuşak malzeme kullanmak, hastanın konforunu artırır ve baskıyı azaltır.",
                        "B.Yara varsa üzeri temiz bir bezle kapatılmalı": "Açık yara varsa enfeksiyon riskini azaltmak için üzeri temiz bir bezle kapatılmalıdır.",
                        "D.Tespit yapılırken yaralı bölge sabit tutulmalı": "Yaralı bölgenin sabit tutulması, daha fazla hareket ve hasarı önler."
                    }
                },
                {
                    "question": "20.Aşağıdakilerden hangisi dış kanamalarda ilk yapılacak olan ilkyardım uygulamasıdır?",
                    "options": ["A.Bandaj ile sararak basınç uygulamak", "B.Turnike uygulamak", "C.Kanayan bölgeyi yukarı kaldırmak", "D.Kanayan yer üzerine temiz bir bezle bastırmak"],
                    "answer": "D.Kanayan yer üzerine temiz bir bezle bastırmak",
                    "explanation": "Dış kanamalarda ilk yapılacak olan ilkyardım uygulaması, kanayan yer üzerine temiz bir bezle bastırmaktır. Bu, kanamayı durdurmak için en hızlı ve etkili yöntemdir.",
                    "wrong_explanations": {
                        "A.Bandaj ile sararak basınç uygulamak": "Bandaj ile sararak basınç uygulamak, ilk baskıdan sonra kanama durmazsa yapılan bir sonraki adımdır.",
                        "B.Turnike uygulamak": "Turnike uygulaması, ciddi kanamalarda ve uzuv kopmalarında son çare olarak düşünülmelidir.",
                        "C.Kanayan bölgeyi yukarı kaldırmak": "Kanayan bölgeyi yukarı kaldırmak, kan akışını yavaşlatmaya yardımcı olur ancak ilk müdahale değildir."
                    }
                }
            ]
        },
        "Test 7": {
            "questions": [
                {
                    "question": "1- Dış kanamalarda yapılacak ilkyardım uygulamaları ile ilgili aşağıdakilerden hangisi yanlıştır?",
                    "options": ["A-Kanayan bölge aşağıda tutulur.", "B-Kanayan yer üzerine temiz bir bezle bastırılır.", "C-Kanayan yere en yakın basınç noktasına baskı uygulanır.", "D-Gerekirse bandaj ile sararak basınç uygulanır."],
                    "answer": "A-Kanayan bölge aşağıda tutulur.",
                    "explanation": "Dış kanamalarda kanayan bölge kalp seviyesinden yukarıda tutulmalıdır. Kanayan bölgenin aşağıda tutulması kan kaybını artırır.",
                    "wrong_explanations": {
                        "B-Kanayan yer üzerine temiz bir bezle bastırılır.": "Bu, dış kanamalarda yapılması gereken temel ilk yardım uygulamalarından biridir.",
                        "C-Kanayan yere en yakın basınç noktasına baskı uygulanır.": "Diğer yöntemler başarısız olduğunda, kanamayı kontrol altına almak için en yakın basınç noktasına baskı uygulamak gerekir.",
                        "D-Gerekirse bandaj ile sararak basınç uygulanır.": "Kanayan yer üzerine bezle yapılan baskı yetersiz kalırsa, bandaj ile sararak basınç uygulamak doğru bir yöntemdir."
                    }
                },
                {
                    "question": "2- Aşağıdakilerden hangisi kulağa yabancı cisim kaçması durumunda yapılması gereken ilkyardım uygulamalarından değildir?",
                    "options": ["A-Sivri ve delici bir cisimle müdahale edilmemeli", "B-Tıbbi yardım istenmeli", "C-Kulak içi ılık su ile yıkanmalı", "D-Kulağa su değdirilmemeli"],
                    "answer": "C-Kulak içi ılık su ile yıkanmalı",
                    "explanation": "Kulağa yabancı cisim kaçması durumunda kulak içi ılık su ile yıkanmamalıdır. Bu, cismin daha derine gitmesine veya enfeksiyona neden olabilir. Sivri ve delici cisimlerle müdahale edilmemeli, tıbbi yardım istenmeli ve kulağa su değdirilmemelidir.",
                    "wrong_explanations": {
                        "A-Sivri ve delici bir cisimle müdahale edilmemeli": "Sivri ve delici cisimlerle müdahale etmek, kulağa daha fazla zarar verebilir.",
                        "B-Tıbbi yardım istenmeli": "Kulağa yabancı cisim kaçması durumunda tıbbi yardım istenmelidir.",
                        "D-Kulağa su değdirilmemeli": "Kulağa su değdirmek, cismin şişmesine veya enfeksiyona neden olabilir."
                    }
                },
                {
                    "question": "3- Hava yolu tam tıkanmış bilinci açık 8 aylık hasta/yaralıda hangi ilkyardım uygulaması yapılmalıdır?",
                    "options": ["A-Kalp masajı yapılır.", "B-5 kez sırtına vurulur, 5 kez iki parmakla göğüs basısı uygulanır.", "C-Dokunulmaz, sadece öksürmeye teşvik edilir.", "D-Hasta/yaralının seviyesine inilerek Heimlich Manevrası uygulanır."],
                    "answer": "B-5 kez sırtına vurulur, 5 kez iki parmakla göğüs basısı uygulanır.",
                    "explanation": "Hava yolu tam tıkanmış 8 aylık bebekte, 5 kez sırta vurulur ve 5 kez iki parmakla göğüs basısı uygulanır. Heimlich manevrası bebeklerde uygulanmaz.",
                    "wrong_explanations": {
                        "A-Kalp masajı yapılır.": "Kalp masajı, kalbi durmuş hastalara yapılır, hava yolu tıkanıklığında değil.",
                        "C-Dokunulmaz, sadece öksürmeye teşvik edilir.": "Bu, kısmi tıkanıklıkta yapılır. Tam tıkanıklıkta kişi öksüremez.",
                        "D-Hasta/yaralının seviyesine inilerek Heimlich Manevrası uygulanır.": "Heimlich manevrası bebeklerde uygulanmaz, çocuklarda ve yetişkinlerde kullanılır."
                    }
                },
                {
                    "question": "4- Bilinçsiz bir hasta/yaralının solunum yolunun Tıkanmasının nedeni ne olabilir?",
                    "options": ["A-Bilincinin kaybolması sonucu çenenin kasılması", "B-Başın arkaya giderek soluk yolunu tıkaması", "C-Bilincin kaybolması sonucu vücudun kasılması", "D-Dilin geriye kaçarak soluk yolunu tıkaması"],
                    "answer": "D-Dilin geriye kaçarak soluk yolunu tıkaması",
                    "explanation": "Bilinçsiz bir hasta/yaralının solunum yolunun tıkanmasının en yaygın nedeni, dilin geriye kaçarak soluk yolunu tıkamasıdır. Bilinç kaybı ile birlikte kaslar gevşer ve dil geriye düşebilir.",
                    "wrong_explanations": {
                        "A-Bilincinin kaybolması sonucu çenenin kasılması": "Bilinç kaybı genellikle kasların gevşemesine neden olur, kasılmasına değil.",
                        "B-Başın arkaya giderek soluk yolunu tıkaması": "Başın arkaya gitmesi hava yolunu açmak için kullanılan bir yöntemdir, tıkamaz.",
                        "C-Bilincin kaybolması sonucu vücudun kasılması": "Bilinç kaybı genellikle kasların gevşemesine neden olur, kasılmasına değil."
                    }
                },
                {
                    "question": "5- Aşağıdakilerden hangisi kırık belirtilerinden değildir?",
                    "options": ["A-Hareket ile artan ağrı", "B-Ödem (şişlik-", "C-Şekil bozukluğu", "D-Eklem bozukluğu"],
                    "answer": "D-Eklem bozukluğu",
                    "explanation": "Eklem bozukluğu, genellikle çıkık belirtisidir. Kırık belirtileri arasında hareket ile artan ağrı, ödem (şişlik) ve şekil bozukluğu bulunur.",
                    "wrong_explanations": {
                        "A-Hareket ile artan ağrı": "Hareket ile artan ağrı, kırığın önemli belirtilerindendir.",
                        "B-Ödem (şişlik-": "Ödem (şişlik), kırık bölgesinde görülen bir belirtidir.",
                        "C-Şekil bozukluğu": "Şekil bozukluğu, kırığın önemli belirtilerindendir."
                    }
                },
                {
                    "question": "6- Sindirim yolu ile zehirlenmelerde yapılan ilkyardım uygulamalarından hangisi yanlıştır?",
                    "options": ["A-Bilinci kapalı ve solunumu var ise korna pozisyonu verilir.", "B-Kusturulup rahatlatılır.", "C-Ağız zehirli madde ile temas etmişse su ile çalkalanır.", "D-Olayla ilgili bilgiler toplanarak kaydedilir."],
                    "answer": "B-Kusturulup rahatlatılır.",
                    "explanation": "Sindirim yoluyla zehirlenmelerde hastayı kusturmak her zaman doğru değildir ve bazı durumlarda daha fazla zarar verebilir. Bilinci kapalı hastalarda kusturma kesinlikle yapılmamalıdır. Diğer seçenekler doğru ilk yardım uygulamalarıdır.",
                    "wrong_explanations": {
                        "A-Bilinci kapalı ve solunumu var ise korna pozisyonu verilir.": "Bilinci kapalı ve solunumu olan hastalara koma pozisyonu verilmesi, hava yolunun açık kalmasını sağlar.",
                        "C-Ağız zehirli madde ile temas etmişse su ile çalkalanır.": "Ağız zehirli madde ile temas etmişse su ile çalkalamak, zehrin emilimini azaltabilir.",
                        "D-Olayla ilgili bilgiler toplanarak kaydedilir.": "Olayla ilgili bilgileri toplamak, sağlık ekiplerine doğru bilgi aktarımı için önemlidir."
                    }
                },
                {
                    "question": "7- Aşağıdakilerden hangisi turnike uygulaması için vanlış bir ifadedir?",
                    "options": ["A-Turnike 8-10 cm genişliğinde, kuvvetli ve esnemeyen bir malzemeden yapılır.", "B-Hasta/yaralı turnike bölgesi görülecek şekilde battaniye ile sarılır.", "C-Turnike 5 dakika aralıklarla gevşetilip, tekrar sıkılır", "D-Hasta/yaralının üzerine, turnikenin uygulandığı zaman not edilir."],
                    "answer": "C-Turnike 5 dakika aralıklarla gevşetilip, tekrar sıkılır",
                    "explanation": "Turnike, kanamayı durdurmak için uygulanan bir yöntemdir ve 15-20 dakikada bir gevşetilmelidir. 5 dakika aralıklarla gevşetmek çok sık bir aralıktır ve kanamanın tekrar başlamasına neden olabilir.",
                    "wrong_explanations": {
                        "A-Turnike 8-10 cm genişliğinde, kuvvetli ve esnemeyen bir malzemeden yapılır.": "Turnike, geniş ve esnemeyen bir malzemeden yapılmalıdır.",
                        "B-Hasta/yaralı turnike bölgesi görülecek şekilde battaniye ile sarılır.": "Turnike uygulanan bölge görülecek şekilde bırakılmalıdır.",
                        "D-Hasta/yaralının üzerine, turnikenin uygulandığı zaman not edilir.": "Turnike uygulandığı zaman not edilmeli ve sağlık ekiplerine bildirilmelidir."
                    }
                },
                {
                    "question": "8- Hiçbir uyarana cevap vermeyen, tepkisiz hasta/yaralıda kaçıncı derece bilinç kaybı mevcuttur?",
                    "options": ["A-3. derece", "B-4. derece", "C-2. derece", "D-1. derece"],
                    "answer": "A-3. derece",
                    "explanation": "Hiçbir uyarana cevap vermeyen, tepkisiz hasta/yaralıda 3. derece bilinç kaybı (koma) mevcuttur. 1. derece bilinç kaybı hafif, 2. derece orta düzeyde bilinç kaybıdır.",
                    "wrong_explanations": {
                        "B-4. derece": "Bilinç kaybı dereceleri genellikle 1, 2 ve 3 olarak sınıflandırılır. 4. derece bilinç kaybı tıbbi literatürde yaygın olarak kullanılmaz.",
                        "C-2. derece": "2. derece bilinç kaybında hasta/yaralı ağrılı uyaranlara tepki verebilir.",
                        "D-1. derece": "1. derece bilinç kaybında hasta/yaralı sözlü uyaranlara tepki verebilir."
                    }
                },
                {
                    "question": "9- Aşağıdakilerden hangisi vücudu oluşturan sistemlerden değildir?",
                    "options": ["A-Omurga sistemi", "B-Dolaşım sistemi", "C-Solunum sistemi", "D-Hareket sistemi"],
                    "answer": "A-Omurga sistemi",
                    "explanation": "Vücudu oluşturan ana sistemler; hareket, dolaşım, sinir, solunum, boşaltım ve sindirim sistemleridir. Omurga, hareket sisteminin bir parçasıdır ancak tek başına bir sistem değildir.",
                    "wrong_explanations": {
                        "B-Dolaşım sistemi": "Dolaşım sistemi, kan, kalp ve damarlardan oluşur ve vücudun temel sistemlerinden biridir.",
                        "C-Solunum sistemi": "Solunum sistemi, akciğerler ve solunum yollarından oluşur ve vücudun temel sistemlerinden biridir.",
                        "D-Hareket sistemi": "Hareket sistemi, kemikler, eklemler ve kaslardan oluşur ve vücudun temel sistemlerinden biridir."
                    }
                },
                {
                    "question": "10- Kanamalar ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
                    "options": ["A-Toplardamar kanamaları küçük kabarcıklar şeklindedir.", "B-Kılcal damar kanamaları açık renkli ve sızıntı şeklindedir.", "C-Toplardamar kanamalarında kısa zamanda çok kan Kaybedilir.", "D-Atardamar kanamaları kalp atımları ile uyumlu olarak Kesik kesik akar."],
                    "answer": "D-Atardamar kanamaları kalp atımları ile uyumlu olarak Kesik kesik akar.",
                    "explanation": "Atardamar kanamaları, kalp atımı ile uyumlu olarak kesik kesik ve fışkırır tarzda olur. Rengi açık kırmızıdır ve en tehlikeli kanama türüdür.",
                    "wrong_explanations": {
                        "A-Toplardamar kanamaları küçük kabarcıklar şeklindedir.": "Toplardamar kanamaları sürekli ve koyu renklidir. Küçük kabarcıklar şeklinde olan kanamalar kılcal damar kanamalarıdır.",
                        "B-Kılcal damar kanamaları açık renkli ve sızıntı şeklindedir.": "Kılcal damar kanamaları sızıntı şeklinde ve açık renklidir, ancak bu ifade doğrudur.",
                        "C-Toplardamar kanamalarında kısa zamanda çok kan Kaybedilir.": "Kısa zamanda çok kan kaybedilen kanama türü atardamar kanamalarıdır."
                    }
                },
                {
                    "question": "11- Hasta/yaralıyı araçtan çıkartmak gerektiğinde dikkat edilmesi gereken kural aşağıdakilerden hangisidir?",
                    "options": ["A-Baş ağrısı oluşmaması", "B-Omurga ekseninin bozulmaması", "C-Bilinç kaybı oluşmaması", "D-Öncelikle ayaklarının çıkarılması"],
                    "answer": "B-Omurga ekseninin bozulmaması",
                    "explanation": "Hasta/yaralıyı araçtan çıkartmak gerektiğinde, özellikle trafik kazalarında, omurga ekseninin bozulmamasına dikkat edilmelidir. Yanlış taşıma omurilik yaralanmalarına ve kalıcı hasarlara yol açabilir.",
                    "wrong_explanations": {
                        "A-Baş ağrısı oluşmaması": "Baş ağrısı, omurga yaralanmalarına göre daha az öncelikli bir durumdur.",
                        "C-Bilinç kaybı oluşmaması": "Bilinç kaybı zaten mevcut olabilir veya taşıma sırasında oluşabilir, ancak omurga ekseninin korunması daha önemlidir.",
                        "D-Öncelikle ayaklarının çıkarılması": "Yaralıyı araçtan çıkarırken belirli bir sıra izlenir, ancak omurga ekseninin korunması en önemli kuraldır."
                    }
                },
                {
                    "question": "12- Nabız sayısı ile ilgili aşağıda verilen bilgilerden hangisi doğrudur?",
                    "options": ["A-Çocuklarda 140-150/dk", "B-Bebeklerde 100-140/dk", "C-Gençlerde 40-60/dk", "D-Yetişkinlerde 50-100/dk"],
                    "answer": "B-Bebeklerde 100-140/dk",
                    "explanation": "Bebeklerde normal nabız sayısı dakikada 100-140 arasındadır. Çocuklarda 80-100, gençlerde 60-100, yetişkinlerde ise 60-100 arasındadır.",
                    "wrong_explanations": {
                        "A-Çocuklarda 140-150/dk": "Çocuklarda normal nabız sayısı 80-100 arasındadır.",
                        "C-Gençlerde 40-60/dk": "Gençlerde normal nabız sayısı 60-100 arasındadır.",
                        "D-Yetişkinlerde 50-100/dk": "Yetişkinlerde normal nabız sayısı 60-100 arasındadır."
                    }
                },
                {
                    "question": "13- Hava yolu açıklığının değerlendirilmesi ile ilgili aşağıdakilerden hangisi yanlıstır?",
                    "options": ["A-Baş geri-çene yukarı pozisyonu ile hava yolunun tıkanması engellenir.", "B-Ağız içi kontrolü önce göz ile yapılır.", "C-Önce baş geri-çene yukarı pozisyonu verilir, daha sonra ağız içi kontrol edilir.", "D-Ağız içinde yabancı cisim var ise çıkarılır."],
                    "answer": "C-Önce baş geri-çene yukarı pozisyonu verilir, daha sonra ağız içi kontrol edilir.",
                    "explanation": "Hava yolu açıklığı sağlanırken, öncelikle ağız içi kontrol edilmeli ve gözle görülen bir cisim varsa çıkarılmalıdır. Daha sonra baş geri-çene yukarı pozisyonu verilerek hava yolu açılmalıdır.",
                    "wrong_explanations": {
                        "A-Baş geri-çene yukarı pozisyonu ile hava yolunun tıkanması engellenir.": "Bu ifade doğrudur. Baş geri-çene yukarı pozisyonu hava yolunu açar.",
                        "B-Ağız içi kontrolü önce göz ile yapılır.": "Bu ifade doğrudur. Ağız içi kontrolü önce göz ile yapılmalıdır.",
                        "D-Ağız içinde yabancı cisim var ise çıkarılır.": "Bu ifade doğrudur. Ağız içinde yabancı cisim varsa çıkarılmalıdır."
                    }
                },
                {
                    "question": "14- Kulak kanaması görülen bilinci kapalı ve solunumu olan hasta/yaralıya hangi pozisyon verilir?",
                    "options": ["A-Kanayan kulak üstte kalacak şekilde korna pozisyonu", "B-Yarı oturur pozisyonu", "C-Kanayan kulak altta kalacak şekilde korna pozisyonu", "D-Şok pozisyonu"],
                    "answer": "C-Kanayan kulak altta kalacak şekilde korna pozisyonu",
                    "explanation": "Kulak kanaması görülen bilinci kapalı ve solunumu olan hasta/yaralıya, kanayan kulak altta kalacak şekilde koma pozisyonu verilmelidir. Bu, kanın dışarı akmasını sağlayarak beyin içine basınç yapmasını engeller.",
                    "wrong_explanations": {
                        "A-Kanayan kulak üstte kalacak şekilde korna pozisyonu": "Kanayan kulak üstte kalacak şekilde pozisyon vermek, kanın beyin içine akmasına neden olabilir.",
                        "B-Yarı oturur pozisyonu": "Yarı oturur pozisyon, kulak kanamalarında uygun bir pozisyon değildir.",
                        "D-Şok pozisyonu": "Şok pozisyonu, kulak kanamalarında uygun bir pozisyon değildir."
                    }
                },
                {
                    "question": "15- Trafik kazası sonucu solunum sıkıntısı çektiği ve kan tükürdüğü görülen yaralıda aşağıdakilerden hangisi düşünülür",
                    "options": ["A-Kafa yaralanması", "B-Mide yaralanması", "C-Sara krizi", "D-Göğüs yaralanması"],
                    "answer": "D-Göğüs yaralanması",
                    "explanation": "Solunum sıkıntısı ve kan tükürme, delici göğüs yaralanmalarının tipik belirtileridir. Bu durum, akciğer veya solunum yollarında bir hasar olduğunu gösterir.",
                    "wrong_explanations": {
                        "A-Kafa yaralanması": "Kafa yaralanmalarında bilinç kaybı, baş ağrısı, bulantı gibi belirtiler görülür.",
                        "B-Mide yaralanması": "Mide yaralanmalarında karın ağrısı, hassasiyet, bulantı, kusma gibi belirtiler görülür.",
                        "C-Sara krizi": "Sara krizi, nöbetlerle karakterize bir durumdur ve solunum sıkıntısı ile kan tükürme tipik belirtileri değildir."
                    }
                },
                {
                    "question": "16- Kemik bütünlüğünün bozulmasına ne denir?",
                    "options": ["A-Çıkık", "B-Kırık", "C-Burkulma", "D-Yaralanma"],
                    "answer": "B-Kırık",
                    "explanation": "Kırık, kemik bütünlüğünün bozulması durumudur. Çıkık, eklem yüzeylerinin ayrılması; burkulma, eklem bağlarının gerilmesi veya yırtılmasıdır.",
                    "wrong_explanations": {
                        "A-Çıkık": "Çıkık, eklem yüzeylerinin kalıcı olarak birbirinden ayrılmasıdır.",
                        "C-Burkulma": "Burkulma, eklem bağlarının gerilmesi veya yırtılmasıdır.",
                        "D-Yaralanma": "Yaralanma, genel bir terimdir ve kırığı da kapsar, ancak kırık daha spesifik bir tanımdır."
                    }
                },
                                {
                                    "question": "17- Aşağıdakilerden hangisi ciddi yaralanmalardan değildir?",
                                    "options": ["A-Ezik yara", "B-Delici göğüs yarası", "C-Hayvan ısırığı", "D-Ateşli silah yaralanması"],
                                    "answer": "A-Ezik yara",
                                    "explanation": "Ezik yara, genellikle künt travma sonucu oluşan, morarma ve şişlik ile karakterize bir yaradır. Diğer seçenekler ise daha ciddi yaralanma türleridir.",
                                    "wrong_explanations": {
                                        "B-Delici göğüs yarası": "Delici göğüs yarası, iç organlara zarar verme riski taşıdığı için ciddi bir yaralanmadır.",
                                        "C-Hayvan ısırığı": "Hayvan ısırıkları, enfeksiyon riski ve doku hasarı nedeniyle ciddi kabul edilir.",
                                        "D-Ateşli silah yaralanması": "Ateşli silah yaralanması, iç organlara ciddi zarar verebileceği için çok ciddi bir yaralanmadır."
                                    }
                                },                {
                    "question": "18- 8 aylık bir hasta/yaralıya kalp masajı nasıl uygulanır?",
                    "options": ["A-İki parmak ile", "B-Bir elin topuğu ile", "C-İki elin topuğu ile", "D-Tek parmak ile"],
                    "answer": "A-İki parmak ile",
                    "explanation": "8 aylık bir bebeğe kalp masajı, iki meme başının altındaki hattın ortasına iki parmak ile uygulanır. Bu, bebeğin hassas göğüs kafesine zarar vermeden etkili bası sağlamak içindir.",
                    "wrong_explanations": {
                        "B-Bir elin topuğu ile": "Bir elin topuğu ile kalp masajı çocuklarda uygulanır.",
                        "C-İki elin topuğu ile": "İki elin topuğu ile kalp masajı yetişkinlerde uygulanır.",
                        "D-Tek parmak ile": "Tek parmak ile kalp masajı yapılmaz."
                    }
                },
                {
                    "question": "19- Beynin normal faaliyetlerindeki herhangi bir aksama nedeni üe uyku halinden başlayarak, hiçbir uyarıya. Cevap vermeme haline kadar giden, bilincin tamamen veya kısmen kaybolmasına ne nedir?",
                    "options": ["A-Şok", "B-Yaralanma", "C-kanama", "D- bilinç bozukluğu"],
                    "answer": "D- bilinç bozukluğu",
                    "explanation": "Verilen tanım, bilincin tamamen veya kısmen kaybolması durumunu ifade eder ki bu da bilinç bozukluğudur. Şok, yaralanma ve kanama farklı tıbbi durumlardır.",
                    "wrong_explanations": {
                        "A-Şok": "Şok, yaşamsal organlara yeterli kan gitmemesi durumudur.",
                        "B-Yaralanma": "Yaralanma, doku veya organ hasarıdır.",
                        "C-kanama": "Kanama, kanın damar dışına çıkmasıdır."
                    }
                },
                {
                    "question": "20- Aşağıdakilerden hangisi hayat kurtarma zincirinin birinci halkasını ifade eder?",
                    "options": ["A-Hastane acil servisinin müdahale yapılması", "B-Ambulans ekiplerince müdahale yapılması", "C-Sağlık kuruluşuna haber verilmesi", "D-Olay yerinde temel yaşam desteği yapılması"],
                    "answer": "C-Sağlık kuruluşuna haber verilmesi",
                    "explanation": "Hayat kurtarma zincirinin birinci halkası, olay yerinde sağlık kuruluşuna (112) haber verilmesidir. Bu, hızlı ve etkili tıbbi yardımın ulaşmasını sağlar.",
                    "wrong_explanations": {
                        "A-Hastane acil servisinin müdahale yapılması": "Hastane acil servislerinde müdahale, hayat kurtarma zincirinin dördüncü halkasıdır.",
                        "B-Ambulans ekiplerince müdahale yapılması": "Ambulans ekiplerince müdahale, hayat kurtarma zincirinin üçüncü halkasıdır.",
                        "D-Olay yerinde temel yaşam desteği yapılması": "Olay yerinde temel yaşam desteği yapılması, hayat kurtarma zincirinin ikinci halkasıdır."
                    }
                }
            ]
        },
        "Test 8": {
            "questions": [
                {
                    "question": "1.Tek kişi ile yetişkin bir hastada kalp-akciğer canlandırması uygulaması sırasında verilmesi gereken soluk ile kalp masajı sayısı ne olmalıdır ?",
                    "options": ["A- 5 soluk - 1 kalp masajı", "B-30 kalp masajı- 2 soluk", "C-5 soluk-15 kalp masajı", "D-2 soluk -5 kalp masajı"],
                    "answer": "B-30 kalp masajı- 2 soluk",
                    "explanation": "Yetişkinlerde tek kişi ile yapılan kalp-akciğer canlandırmasında, 30 kalp masajına 2 soluk verilmelidir. Bu oran, etkili bir canlandırma için uluslararası standartlara uygundur.",
                    "wrong_explanations": {
                        "A- 5 soluk - 1 kalp masajı": "Bu oran, canlandırma için uygun değildir.",
                        "C-5 soluk-15 kalp masajı": "Bu oran, canlandırma için uygun değildir.",
                        "D-2 soluk -5 soluk -5 kalp masajı": "Bu oran, canlandırma için uygun değildir."
                    }
                },
                {
                    "question": "2. İlkyardımda hayat kurtarma zincirinin ilk halkasında hangi uygulama vardır?",
                    "options": ["A-112'ye haber vermek", "B-Temel yaşam desteği uygulamak", "C-Hemen hastaneye götürmek", "D-Sağlık ekiplerinin olay yerine ulaşmasını beklemek"],
                    "answer": "A-112'ye haber vermek",
                    "explanation": "Hayat kurtarma zincirinin ilk halkası, olay yerinde sağlık kuruluşuna (112) haber verilmesidir. Bu, hızlı ve etkili tıbbi yardımın ulaşmasını sağlar.",
                    "wrong_explanations": {
                        "B-Temel yaşam desteği uygulamak": "Temel yaşam desteği, hayat kurtarma zincirinin ikinci halkasıdır.",
                        "C-Hemen hastaneye götürmek": "Hastaneye götürmek, genellikle ambulans ekiplerinin görevidir ve ilk yardımın ilk adımı değildir.",
                        "D-Sağlık ekiplerinin olay yerine ulaşmasını beklemek": "Sağlık ekiplerini beklerken ilk yardım uygulamalarına başlanmalıdır."
                    }
                },
                {
                    "question": "3. 'Eklem yüzeylerinin kalıcı olarak ayrılmasıdır.' İfadesi aşağıdakilerden hangisini tanımlar?",
                    "options": ["A-Çıkık", "B-Burkulma", "C-Açık kırık", "D-Kapalı kırık"],
                    "answer": "A-Çıkık",
                    "explanation": "Çıkık, eklem yüzeylerinin kalıcı olarak birbirinden ayrılması durumudur. Burkulma, eklem bağlarının gerilmesi veya yırtılması; kırık ise kemik bütünlüğünün bozulmasıdır.",
                    "wrong_explanations": {
                        "B-Burkulma": "Burkulma, eklem bağlarının gerilmesi veya yırtılmasıdır, eklem yüzeylerinin ayrılması değildir.",
                        "C-Açık kırık": "Açık kırıkta kemik bütünlüğü ile birlikte deri bütünlüğü de bozulmuştur.",
                        "D-Kapalı kırık": "Kapalı kırıkta kemik bütünlüğü bozulmuş ancak deri bütünlüğü sağlam kalmıştır."
                    }
                },
                {
                    "question": "4. 8(sekiz- aylık hasta/yaralıda kalp basısı nereye uygulanır",
                    "options": ["A- Güğüs kemiğinin 1/5 alt kısmına", "B- Göğüs kemiğinin üst ve alt ucu tespit edilerek alt yarısına", "C- Göğüs kemiğinin 1/3 üst kısmına", "D- İki meme başının birleştiği hayali çizginin orta noktasının bir parmak altına"],
                    "answer": "D- İki meme başının birleştiği hayali çizginin orta noktasının bir parmak altına",
                    "explanation": "8 aylık bir bebekte kalp masajı, iki meme başının birleştiği hayali çizginin orta noktasının bir parmak altına uygulanır. Bu, bebeğin hassas göğüs kafesine zarar vermeden etkili bası sağlamak içindir.",
                    "wrong_explanations": {
                        "A- Güğüs kemiğinin 1/5 alt kısmına": "Bu, bebeklerde kalp masajı için doğru bir yer değildir.",
                        "B- Göğüs kemiğinin üst ve alt ucu tespit edilerek alt yarısına": "Bu, yetişkinlerde kalp masajı için doğru bir yerdir.",
                        "C- Göğüs kemiğinin 1/3 üst kısmına": "Bu, bebeklerde kalp masajı için doğru bir yer değildir."
                    }
                },
                {
                    "question": "5.Sindirim yolu ile olan zehirlenmelerde aşağıdakilerden hangisi yapılmalıdır?",
                    "options": ["A- Hasta kusturulmalıdır", "B- Yoğurt yedirilmelidir", "C- Bol su içirilir", "D- ABC kontrolü yapılarak 112'den yardım istenmelidir"],
                    "answer": "D- ABC kontrolü yapılarak 112'den yardım istenmelidir",
                    "explanation": "Sindirim yoluyla zehirlenmelerde öncelikle ABC (hava yolu, solunum, dolaşım) kontrolü yapılmalı ve hemen 112'den yardım istenmelidir. Kusturmak veya yoğurt yedirmek gibi uygulamalar her zaman doğru değildir ve bazı durumlarda zararlı olabilir.",
                    "wrong_explanations": {
                        "A- Hasta kusturulmalıdır": "Bazı zehirli maddeler kusturulduğunda daha fazla zarar verebilir. Kusturma kararı tıbbi profesyoneller tarafından verilmelidir.",
                        "B- Yoğurt yedirilmelidir": "Yoğurt yedirmek, zehirlenmelerde etkili bir tedavi yöntemi değildir ve tıbbi müdahaleyi geciktirebilir.",
                        "C- Bol su içirilir": "Her zehirlenme durumunda bol su içirmek doğru değildir, bazı durumlarda emilimi hızlandırabilir."
                    }
                },
                {
                    "question": "6.Kısa süreli yüzeysel bilinç kaybına ne denir?",
                    "options": ["A-Havale", "B- Bayılma", "C- Koma", "D- Sıcak çarpması"],
                    "answer": "B- Bayılma",
                    "explanation": "Bayılma, genellikle kısa süreli, yüzeysel ve geçici bilinç kaybıdır. Beyne giden kan akışının geçici olarak azalması sonucu oluşur.",
                    "wrong_explanations": {
                        "A-Havale": "Havale, beyindeki elektriksel aktivitenin ani ve kontrolsüz boşalması sonucu oluşan bir durumdur ve genellikle kasılmalarla seyreder.",
                        "C- Koma": "Koma, uzun süreli ve derin bilinç kaybı durumudur.",
                        "D- Sıcak çarpması": "Sıcak çarpması, vücut ısısının tehlikeli derecede yükselmesi sonucu oluşan ciddi bir durumdur ve bilinç kaybına yol açabilir ancak tanımı farklıdır."
                    }
                },
                {
                    "question": "7.Solunum yolu ile zehirlenen bilinci açık hasta/yaralıya hangi pozisyon verilmelidir?",
                    "options": ["A- Yüz üstü pozisyonda", "B- Şok pozisyonunda", "C- Yarı oturur pozisyonda", "D- Yan pozisyonda"],
                    "answer": "C- Yarı oturur pozisyonda",
                    "explanation": "Solunum yoluyla zehirlenen bilinci açık hasta/yaralıya yarı oturur pozisyon verilmelidir. Bu pozisyon, solunumu kolaylaştırır ve zehirli gazın daha fazla emilimini engellemeye yardımcı olur.",
                    "wrong_explanations": {
                        "A- Yüz üstü pozisyonda": "Yüz üstü pozisyon, solunumu zorlaştırabilir.",
                        "B- Şok pozisyonunda": "Şok pozisyonu, genellikle dolaşım yetmezliği durumlarında kullanılır ve solunum yolu zehirlenmelerinde uygun değildir.",
                        "D- Yan pozisyonda": "Yan pozisyon, bilinci kapalı hastalarda hava yolunu açık tutmak için kullanılır, bilinci açık hastalarda uygun değildir."
                    }
                },
                {
                    "question": "8.Bebeklerde temel yaşam desteği (TYD- ile ilgili verilen şıklardan hangisi yanlıştır?",
                    "options": ["A- Bebeklerde bilinç kontrolü ayak tabanına vurularak yapılabilir", "B-Bebeklerde ilkyardımcı yalnız ise müdehaleden önce 112'yi arar", "C-Hava yolunu açmak için baş hafifçe yukarı geri itilerek eğilir, baş geriene yukarı pozisyonu verilir.", "D- Bebeklerde TYD 2 kurtarıcı soluk verildikten sonra 30 dış kalp masajı 2 solunum olarak uygulanır."],
                    "answer": "B-Bebeklerde ilkyardımcı yalnız ise müdehaleden önce 112'yi arar",
                    "explanation": "Bebeklerde ilkyardımcı yalnız ise, temel yaşam desteği uygulamasına 2 kurtarıcı soluk ile başlar ve 5 tur (yaklaşık 2 dakika) uyguladıktan sonra 112'yi aramalıdır. Yetişkinlerde ise bilinç kontrolünden hemen sonra 112 aranır.",
                    "wrong_explanations": {
                        "A- Bebeklerde bilinç kontrolü ayak tabanına vurularak yapılabilir": "Bebeklerde bilinç kontrolü, ayak tabanına hafifçe vurularak veya seslenerek yapılabilir.",
                        "C-Hava yolunu açmak için baş hafifçe yukarı geri itilerek eğilir, baş geriene yukarı pozisyonu verilir.": "Bebeklerde hava yolu açmak için baş hafifçe geriye itilir, yetişkinlerde ise daha fazla.",
                        "D- Bebeklerde TYD 2 kurtarıcı soluk verildikten sonra 30 dış kalp masajı 2 solunum olarak uygulanır.": "Bebeklerde TYD, 2 kurtarıcı soluk ve 30 kalp masajı şeklinde uygulanır."
                    }
                },
                {
                    "question": "9.Aşağıdakilerden hangisi burkulmanın belirtilerinden biri değildir?",
                    "options": ["A- Ağrı", "B- Dış kanama", "C- Şişlik, kızarma", "D- İşlev kaybı"],
                    "answer": "B- Dış kanama",
                    "explanation": "Burkulma, eklem bağlarının gerilmesi veya yırtılmasıdır. Dış kanama, burkulmanın tipik bir belirtisi değildir. Burkulmanın belirtileri ağrı, şişlik, kızarma ve işlev kaybıdır.",
                    "wrong_explanations": {
                        "A- Ağrı": "Ağrı, burkulmanın yaygın belirtilerinden biridir.",
                        "C- Şişlik, kızarma": "Şişlik ve kızarma, burkulma bölgesinde görülen iltihabi reaksiyonlardır.",
                        "D- İşlev kaybı": "İşlev kaybı, burkulma nedeniyle eklemin normal hareketini yapamaması durumudur."
                    }
                },
                {
                    "question": "10.Aşağıdakilerden hangisi yanığın ciddiyetini belirleyen faktörler arasında yer almaz?",
                    "options": ["A-Enfeksiyon riski", "B-Yanığın derinliği", "C-Derinin inceliği", "D-Oluştuğu bölge"],
                    "answer": "A-Enfeksiyon riski",
                    "explanation": "Yanığın ciddiyetini belirleyen faktörler arasında yanığın derinliği, genişliği, oluştuğu bölge, enfeksiyon riski ve hastanın yaşı gibi faktörler yer alır. Ancak enfeksiyon riski, yanığın ciddiyetini belirleyen bir faktör değildir, yanığın bir komplikasyonudur.",
                    "wrong_explanations": {
                        "B-Yanığın derinliği": "Yanığın derinliği, ciddiyetini belirleyen önemli bir faktördür.",
                        "C-Derinin inceliği": "Derinin inceliği, yanığın ciddiyetini etkileyen bir faktördür.",
                        "D-Oluştuğu bölge": "Yanığın oluştuğu bölge (örneğin, yüz, eller, genital bölge) ciddiyetini etkileyen bir faktördür."
                    }
                },
                {
                    "question": "11.Kırık veya çıkıkta atel(tespit- uygulaması ile ilgili aşağıdaki ifadelerden hangisi yanlıştır?",
                    "options": ["A-Tespit yapılırken yaralı bölge sabit tutulmalıdır", "B-yara varsa üzeri temiz bir bezle kapatılır", "C-yaralı bölge düzeltilerek tespit edilmelidir", "D-tespit; kırık, çıkık ve burkulmanın üstünde ve altında kalan eklemleri de içerecek şekilde yapılmalıdır"],
                    "answer": "C-yaralı bölge düzeltilerek tespit edilmelidir",
                    "explanation": "Kırık veya çıkıkta, yaralı bölgenin pozisyonu düzeltilmeye çalışılmamalıdır. Bu, daha fazla hasara neden olabilir. Tespit, yaralı bölge bulunduğu pozisyonda sabit tutularak yapılmalıdır.",
                    "wrong_explanations": {
                        "A-Tespit yapılırken yaralı bölge sabit tutulmalıdır": "Tespit sırasında yaralı bölgenin sabit tutulması, daha fazla hareket ve hasarı önler.",
                        "B-yara varsa üzeri temiz bir bezle kapatılır": "Açık yara varsa enfeksiyon riskini azaltmak için üzeri temiz bir bezle kapatılmalıdır.",
                        "D-tespit; kırık, çıkık ve burkulmanın üstünde ve altında kalan eklemleri de içerecek şekilde yapılmalıdır": "Tespit, yaralı bölgenin hareketini tamamen kısıtlamak için kırık, çıkık ve burkulmanın üstünde ve altında kalan eklemleri de içerecek şekilde yapılmalıdır."
                    }
                },
                {
                    "question": "12.Aşağıdakilerden hangisi yaraların ortak belirtilerinden biri değildir?",
                    "options": ["A-yara kenarları ayrılır", "B-kanama olur", "C-ağrı olur", "D-yara içerisinde yabancı cisim olur"],
                    "answer": "D-yara içerisinde yabancı cisim olur",
                    "explanation": "Yaraların ortak belirtileri kanama, ağrı ve yara kenarlarının ayrılmasıdır. Yara içerisinde yabancı cisim olması, her yara türünde görülmez ve yaranın ortak bir belirtisi değildir.",
                    "wrong_explanations": {
                        "A-yara kenarları ayrılır": "Yara kenarlarının ayrılması, yaranın tipine göre değişmekle birlikte, birçok yara türünde görülen bir belirtidir.",
                        "B-kanama olur": "Kanama, yaralanmaların en yaygın belirtilerinden biridir.",
                        "C-ağrı olur": "Ağrı, yaralanmanın şiddetine göre değişmekle birlikte, tüm yaralarda görülen bir belirtidir."
                    }
                },
                {
                    "question": "13.Bilinci kapalı bir hasta hangi yöntemle taşınmaz?",
                    "options": ["A-itfaiyeci yöntemi (omuzda taşıma-", "B-sürükleme", "C-koltuk altından tutarak sürükleme", "D-dört elle taşıma (altın beşik-"],
                    "answer": "D-dört elle taşıma (altın beşik-",
                    "explanation": "Dört elle taşıma (altın beşik) yöntemi, bilinci açık, yürüyebilen veya kısa mesafede taşınması gereken hafif yaralılar için kullanılan bir taşıma yöntemidir. Bilinci kapalı hastalarda omurga yaralanması riski nedeniyle bu yöntem kullanılmaz.",
                    "wrong_explanations": {
                        "A-itfaiyeci yöntemi (omuzda taşıma-": "İtfaiyeci yöntemi, bilinci kapalı hastalarda kullanılabilen bir taşıma yöntemidir.",
                        "B-sürükleme": "Sürükleme yöntemi, bilinci kapalı hastalarda kullanılabilen bir taşıma yöntemidir.",
                        "C-koltuk altından tutarak sürükleme": "Koltuk altından tutarak sürükleme yöntemi, bilinci kapalı hastalarda kullanılabilen bir taşıma yöntemidir."
                    }
                },
                {
                    "question": "14. Kanı süzerek gerekli maddelerin vücutta tutulması zararlı olanların atılması görevlerini yaparak vücutta iç dengeyi koruyan sistem hangisidir?",
                    "options": ["A-Dolaşım sistemi", "B-Solunum sistemi", "C-Sindirim sistemi", "D-Boşaltım sistemi"],
                    "answer": "D-Boşaltım sistemi",
                    "explanation": "Boşaltım sistemi, kanı süzerek vücut için gerekli maddelerin tutulmasını ve zararlı atık maddelerin atılmasını sağlar. Bu sayede vücudun iç dengesini (homeostaz) korur.",
                    "wrong_explanations": {
                        "A-Dolaşım sistemi": "Dolaşım sistemi, kanı vücutta taşıyarak oksijen ve besin maddelerini hücrelere ulaştırır, atık maddeleri toplar.",
                        "B-Solunum sistemi": "Solunum sistemi, vücuda oksijen alıp karbondioksit veren sistemdir.",
                        "C-Sindirim sistemi": "Sindirim sistemi, alınan besinleri öğütülerek sindirilmesini ve emilimini sağlar."
                    }
                },
                {
                    "question": "15.Aşağıdakilerden hangisi akrep sokmalarında yapılacak ilkyardım uygulamasıdır?",
                    "options": ["A-Kan dolaşımını engellemeycek şekilde bandaj uygulanır.", "B-Yaraya sıcak uygulama yapılır.", "C-Yaralı bölge bir süre ovularak zehrin etkileri azaltılır", "D-Kol ve bacaktan ısırmalarda turnike uygulanır"],
                    "answer": "A-Kan dolaşımını engellemeycek şekilde bandaj uygulanır.",
                    "explanation": "Akrep sokmalarında, zehrin yayılmasını yavaşlatmak için sokulan bölgeye kan dolaşımını engellemeyecek şekilde bandaj uygulanır. Diğer uygulamalar yanlış veya zararlı olabilir.",
                    "wrong_explanations": {
                        "B-Yaraya sıcak uygulama yapılır.": "Sıcak uygulama, zehrin emilimini hızlandırabilir.",
                        "C-Yaralı bölge bir süre ovularak zehrin etkileri azaltılır": "Yaralı bölgeyi ovmak, zehrin vücuda daha hızlı yayılmasına neden olabilir.",
                        "D-Kol ve bacaktan ısırmalarda turnike uygulanır": "Turnike uygulaması, doku hasarına neden olabilir ve akrep sokmalarında önerilmez."
                    }
                },
                {
                    "question": "16.kedi, köpek ısırmalarında yapılan ilkyardım uygulamalarında hangisi yanlıştır?",
                    "options": ["A-yara 5 dakika süre ile sabun ve soğuk su ile yıkanır", "B-yaranın üstü açık bırakılır", "C-yaşamsal bulguları kontrol edilir", "D-kanama varsa durdurulur"],
                    "answer": "B-yaranın üstü açık bırakılır",
                    "explanation": "Kedi, köpek ısırmalarında yaranın üstü açık bırakılmamalıdır. Enfeksiyon riskini azaltmak için yara temiz bir bezle kapatılmalıdır. Diğer seçenekler doğru ilk yardım uygulamalarıdır.",
                    "wrong_explanations": {
                        "A-yara 5 dakika süre ile sabun ve soğuk su ile yıkanır": "Yara, enfeksiyon riskini azaltmak için sabun ve soğuk su ile yıkanmalıdır.",
                        "C-yaşamsal bulguları kontrol edilir": "Yaşamsal bulguların kontrolü, her türlü acil durumda yapılması gereken temel bir adımdır.",
                        "D-kanama varsa durdurulur": "Kanamayı durdurmak, ilk yardımın öncelikli amaçlarından biridir."
                    }
                },
                {
                    "question": "17.Aşağıdaki şıklardan hangisinde temel yaşam desteği uygulaması sırasında yapılan diş kalp masajı basısı şekli doğru olarak verilmiştir?",
                    "options": ["YETİŞKİN ÇOÇUK BEBEK", "A-tek elle iki parmakla çift elle", "B-çift elle iki parmakla tek elle", "C-çift elle çift elle tek elle", "D-çift elle tek elle iki parmakla"],
                    "answer": "D-çift elle tek elle iki parmakla",
                    "explanation": "Temel yaşam desteği (TYD) sırasında kalp masajı basısı şekli yaş gruplarına göre değişir: Yetişkinlerde çift elle, çocuklarda tek elle, bebeklerde ise iki parmakla yapılır.",
                    "wrong_explanations": {
                        "A-tek elle iki parmakla çift elle": "Bu sıralama yanlıştır. Yetişkinlerde çift elle, çocuklarda tek elle, bebeklerde iki parmakla yapılmalıdır.",
                        "B-çift elle iki parmakla tek elle": "Bu sıralama yanlıştır. Yetişkinlerde çift elle, çocuklarda tek elle, bebeklerde iki parmakla yapılmalıdır.",
                        "C-çift elle çift elle tek elle": "Bu sıralama yanlıştır. Yetişkinlerde çift elle, çocuklarda tek elle, bebeklerde iki parmakla yapılmalıdır."
                    }
                },
                {
                    "question": "18.Göze toz gibi küçük yabancı cisim kaçmasında yapılacak ilkyardım aşağıdakilerden hangisidir?",
                    "options": ["A- nemli bir bezle çıkarılmaya çalışılir", "B- karbonatlı su yıkanır", "C- göz sıcak tutulur", "D- ovularak tozun atılması sağlanır"],
                    "answer": "A- nemli bir bezle çıkarılmaya çalışılir",
                    "explanation": "Göze toz gibi küçük yabancı cisim kaçmasında, öncelikle göz kırpıştırılarak cismin kendiliğinden çıkması sağlanmaya çalışılır. Eğer çıkmazsa, nemli temiz bir bezle nazikçe çıkarılmaya çalışılır. Diğer uygulamalar göze zarar verebilir.",
                    "wrong_explanations": {
                        "B- karbonatlı su yıkanır": "Karbonatlı su ile yıkamak göze zarar verebilir.",
                        "C- göz sıcak tutulur": "Gözü sıcak tutmak, yabancı cisim durumunda uygun bir uygulama değildir.",
                        "D- ovularak tozun atılması sağlanır": "Gözü ovmak, yabancı cismin korneaya zarar vermesine neden olabilir."
                    }
                },
                {
                    "question": "19.Aşağıdakilerden hangisi deniz canlıları sokmasında yapılan doğru ilkyardım uygulamalarından biridir?",
                    "options": ["A-yaralı bölge ovularak dolaşım hızlandırılır ve zehrin dağılması sağlanır", "B-sokulan yer kesilerek zehirli kanın akması sağlanır daha sonra turnike uygulanır", "C-batan diken varsa görülse bile çıkartılmaz", "D-yaralı bölge hareket ettirilmez"],
                    "answer": "D-yaralı bölge hareket ettirilmez",
                    "explanation": "Deniz canlıları sokmasında, zehrin yayılmasını engellemek ve doku hasarını artırmamak için yaralı bölge hareket ettirilmemelidir. Diğer uygulamalar yanlış veya zararlı olabilir.",
                    "wrong_explanations": {
                        "A-yaralı bölge ovularak dolaşım hızlandırılır ve zehrin dağılması sağlanır": "Yaralı bölgeyi ovmak, zehrin vücuda daha hızlı yayılmasına neden olabilir.",
                        "B-sokulan yer kesilerek zehirli kanın akması sağlanır daha sonra turnike uygulanır": "Sokulan yeri kesmek veya turnike uygulamak, doku hasarına ve zehrin daha hızlı yayılmasına neden olabilir.",
                        "C-batan diken varsa görülse bile çıkartılmaz": "Batan dikenler, sağlık profesyonelleri tarafından çıkarılmalıdır."
                    }
                },
                {
                    "question": "20.Bak-dinle-hisset yöntemiyle solunumu değerlendirilen ve solunumu olmadığı anlaşılan yetişkin bir hastaya ilk olarak ne yapılmalıdır?",
                    "options": ["A-30 defa dış kalp masajı", "B-2 kurtarıcı soluk verilir", "C-5 kurtarıcı soluk verilir", "D-hasta koma pozisyonuna getirilmelidir"],
                    "answer": "B-2 kurtarıcı soluk verilir",
                    "explanation": "Bak-dinle-hisset yöntemiyle solunumu değerlendirilen ve solunumu olmadığı anlaşılan yetişkin bir hastaya ilk olarak 2 kurtarıcı soluk verilmelidir. Ardından kalp masajına başlanır.",
                    "wrong_explanations": {
                        "A-30 defa dış kalp masajı": "Kalp masajına başlamadan önce 2 kurtarıcı soluk verilmelidir.",
                        "C-5 kurtarıcı soluk verilir": "Yetişkinlerde 2 kurtarıcı soluk verilir, 5 değil.",
                        "D-hasta koma pozisyonuna getirilmelidir": "Koma pozisyonu, bilinci kapalı ancak solunumu olan hastalara verilir. Solunumu olmayan hastaya temel yaşam desteği uygulanmalıdır."
                    }
                }
            ]
        },
        "Test 9": {
            "questions": [
                {
                    "question": "1- Aşağıdakilerden hangisi ilkyardımın temel uygulamalar arasında yer almaz?",
                    "options": ["A. tıbbi tedavi", "B. bildirme", "C. kurtarma", "D. koruma"],
                    "answer": "A. tıbbi tedavi",
                    "explanation": "İlkyardımın temel uygulamaları Koruma, Bildirme ve Kurtarma (KBK) olarak sıralanır. Tıbbi tedavi ise sağlık profesyonelleri tarafından yapılan müdahaledir ve ilk yardımın bir parçası değildir.",
                    "wrong_explanations": {
                        "B. bildirme": "Bildirme, ilk yardımın temel uygulamalarından biridir (112'ye haber verme).",
                        "C. kurtarma": "Kurtarma, ilk yardımın temel uygulamalarından biridir (temel yaşam desteği, yaralı taşıma vb.).",
                        "D. koruma": "Koruma, ilk yardımın temel uygulamalarından biridir (olay yeri güvenliğini sağlama)."
                    }
                },
                {
                    "question": "2- Aşağıdakilerden hangisi ilkyardımın öncelikli amaçlarından birisi değildir?",
                    "options": ["A. yaşamsal fonksiyonların sürdürülmesini sağlamak", "B. hayati tehlikeyi ortadan kaldırmak", "C. iyileştirmeyi kolaylaştırmak", "D. hastanın durumu kötüleştiğinde ilaçla müdahale etmek"],
                    "answer": "D. hastanın durumu kötüleştiğinde ilaçla müdahale etmek",
                    "explanation": "İlkyardımın öncelikli amaçları; hayati tehlikeyi ortadan kaldırmak, yaşamsal fonksiyonların sürdürülmesini sağlamak ve iyileşmeyi kolaylaştırmaktır. İlaçla müdahale etmek, ilk yardımın değil, acil tedavinin amacıdır.",
                    "wrong_explanations": {
                        "A. yaşamsal fonksiyonların sürdürülmesini sağlamak": "Yaşamsal fonksiyonların (solunum, dolaşım) sürdürülmesini sağlamak, ilk yardımın en kritik amaçlarındandır.",
                        "B. hayati tehlikeyi ortadan kaldırmak": "Hayati tehlikeyi ortadan kaldırmak, ilk yardımın en temel ve öncelikli amacıdır.",
                        "C. iyileştirmeyi kolaylaştırmak": "İyileşmeyi kolaylaştırmak, ilk yardımın amaçlarından biridir. Örneğin, bir yarayı temiz tutmak enfeksiyonu önleyerek iyileşmeyi kolaylaştırır."
                    }
                },
                {
                    "question": "3- hasta yaralın değerlendirilmesinde ilk aşama aşağıdakilerden hangisidir?",
                    "options": ["A. bilinç durumunun değerlendirilmesi", "B. hava yolu açıklığının değerlendirilmesi", "C. solunumun değerlendirilmesi", "D. kalp masajı"],
                    "answer": "A. bilinç durumunun değerlendirilmesi",
                    "explanation": "Hasta/yaralının ilk değerlendirmesinde öncelikle bilinç durumu kontrol edilmelidir. Bilinç durumu, diğer yaşamsal fonksiyonların değerlendirilmesi için bir ön koşuldur.",
                    "wrong_explanations": {
                        "B. hava yolu açıklığının değerlendirilmesi": "Hava yolu açıklığının değerlendirilmesi, bilinç kontrolünden sonra yapılır.",
                        "C. solunumun değerlendirilmesi": "Solunumun değerlendirilmesi, bilinç kontrolü ve hava yolu açıklığının sağlanmasından sonra yapılır.",
                        "D. kalp masajı": "Kalp masajı, kalbi durmuş hastalara yapılan bir müdahaledir ve ilk değerlendirmenin bir aşaması değildir."
                    }
                },
                {
                    "question": "4- Aşağıdakilerden hangisi yaşam bulguları denildiğinde akla gelen unsurlardan biri değildir?",
                    "options": ["A. bilinç", "B. solunum", "C. dolaşım", "D. cilt rengi"],
                    "answer": "D. cilt rengi",
                    "explanation": "Yaşam bulguları; bilinç, solunum, nabız (dolaşım) ve vücut ısısıdır. Cilt rengi, dolaşım bozukluklarında bir belirti olabilir ancak doğrudan bir yaşam bulgusu değildir.",
                    "wrong_explanations": {
                        "A. bilinç": "Bilinç, yaşam bulgularının en önemlilerinden biridir.",
                        "B. solunum": "Solunum, yaşam bulgularının en önemlilerinden biridir.",
                        "C. dolaşım": "Dolaşım (nabız), yaşam bulgularının en önemlilerinden biridir."
                    }
                },
                {
                    "question": "5- Aşağıdakilerden hangisi solunum sisteminin işlevidir?",
                    "options": ["A. Vücudun hareket etmesini desteklenmesini sağlar", "B. kanı süzerek gerekli maddelerin vücutta tutulmasını zararlı maddelerin atılmasını sağlar", "C. alınan besinleri öğütülerek sindirilmesini ve kan dolaşımı vasıtasıyla vücuda dağıtılmasını sağlar", "D. vücuda gerekli olan gaz alışverişi görevini yaparak hücre ve dokuların oksijenlenmesini sağlar"],
                    "answer": "D. vücuda gerekli olan gaz alışverişi görevini yaparak hücre ve dokuların oksijenlenmesini sağlar",
                    "explanation": "Solunum sistemi, vücuda gerekli olan oksijeni alıp karbondioksiti dışarı atarak hücre ve dokuların oksijenlenmesini sağlar.",
                    "wrong_explanations": {
                        "A. Vücudun hareket etmesini desteklenmesini sağlar": "Bu, hareket sisteminin işlevidir.",
                        "B. kanı süzerek gerekli maddelerin vücutta tutulmasını zararlı maddelerin atılmasını sağlar": "Bu, boşaltım sisteminin işlevidir.",
                        "C. alınan besinleri öğütülerek sindirilmesini ve kan dolaşımı vasıtasıyla vücuda dağıtılmasını sağlar": "Bu, sindirim sisteminin işlevidir."
                    }
                },
                {
                    "question": "6- aşağıdaki organlardan hangisi sindirim sistemi organlarından biri değildir?",
                    "options": ["A. dil ve dişler", "B. Safra kesesi", "C. Bağırsaklar", "D. İdrar kesesi"],
                    "answer": "D. İdrar kesemesi",
                    "explanation": "İdrar kesesi, boşaltım sisteminin bir organıdır. Dil ve dişler, safra kesesi ve bağırsaklar ise sindirim sisteminin organlarıdır.",
                    "wrong_explanations": {
                        "A. dil ve dişler": "Dil ve dişler, sindirimin başlangıcı olan mekanik sindirimde görev alır.",
                        "B. Safra kesesi": "Safra kesesi, karaciğerde üretilen safrayı depolar ve sindirime yardımcı olur.",
                        "C. Bağırsaklar": "Bağırsaklar, besinlerin sindirimi ve emiliminde önemli rol oynar."
                    }
                },
                {
                    "question": "7- Hasta yaralının ikinci değerlendirilmesinde izlenecek sıra aşağıdakilerden hangisidir?",
                    "options": ["A. gövde baş boyun kol ve bacaklar", "B. baş boyun gövde kol ve bacaklar", "C. Baş gövde boyun kol ve bacaklar", "D. Kol ve bacaklar gövde boyun baş"],
                    "answer": "B. baş boyun gövde kol ve bacaklar",
                    "explanation": "Hasta/yaralının ikinci değerlendirilmesinde izlenecek sıra baş, boyun, gövde, kol ve bacaklardır. Bu sistematik yaklaşım, herhangi bir yaralanmanın atlanmamasını sağlar.",
                    "wrong_explanations": {
                        "A. gövde baş boyun kol ve bacaklar": "Sıralama yanlıştır. Baş ve boyun önce değerlendirilmelidir.",
                        "C. Baş gövde boyun kol ve bacaklar": "Sıralama yanlıştır. Boyun, baştan sonra ve gövdeden önce değerlendirilmelidir.",
                        "D. Kol ve bacaklar gövde boyun baş": "Sıralama yanlıştır. Baş ve boyun önce değerlendirilmelidir."
                    }
                },
                {
                    "question": "8- nabız nedir?",
                    "options": ["A. Kalp atımlarının atardamar duvarından hissedilmesidir", "B. Kalbin kasılma ve gevşeme anında damar duvarına yaptığı basınçtır", "C. Nefes alma sırasında göğsün yükselmesidir", "D. Kalbin kanı pompalama gücüd"],
                    "answer": "A. Kalp atımlarının atardamar duvarından hissedilmesidir",
                    "explanation": "Nabız, kalbin her atışında atardamar duvarına yaptığı basıncın parmak uçlarıyla hissedilmesidir.",
                    "wrong_explanations": {
                        "B. Kalbin kasılma ve gevşeme anında damar duvarına yaptığı basınçtır": "Bu, tansiyonun tanımıdır.",
                        "C. Nefes alma sırasında göğsün yükselmesidir": "Bu, solunumun bir belirtisidir.",
                        "D. Kalbin kanı pompalama gücüd": "Bu, kalbin işlevidir, nabız değildir."
                    }
                },
                {
                    "question": "9- ilkyardımcı yalnız ise bilinci kapalı yetişkin hasta yaralı ile karşılaşması durumunda 112 yi ne zaman aramalıdır?",
                    "options": ["A. Baş geri çene yukarı verdikten sonra", "B. Bak dinle hisset yöntemi ile solunum kontrolü yaptıktan sonra", "C. 30-2 kalp masajı suni solunum uygulamasını 5 kez tekrarladıktan sonra", "D. Temel yaşam desteği uygulamasından sonra"],
                    "answer": "C. 30-2 kalp masajı suni solunum uygulamasını 5 kez tekrarladıktan sonra",
                    "explanation": "Yetişkinlerde ilkyardımcı yalnız ise, bilinci kapalı hasta/yaralı ile karşılaştığında, temel yaşam desteği uygulamasının 5 tur tekrarından sonra 112'yi aramalıdır. Bu, kesintisiz kalp masajı ve suni solunumun önemini vurgular.",
                    "wrong_explanations": {
                        "A. Baş geri çene yukarı verdikten sonra": "Hava yolu açıldıktan sonra hemen 112 aranmaz, temel yaşam desteği başlanır.",
                        "B. Bak dinle hisset yöntemi ile solunum kontrolü yaptıktan sonra": "Solunum kontrolü sonrası hemen 112 aranmaz, temel yaşam desteği başlanır.",
                        "D. Temel yaşam desteği uygulamasından sonra": "Temel yaşam desteği uygulaması bitmeden 112 aranmalıdır."
                    }
                },
                {
                    "question": "10- aşağıdakilerden hangisi bebek hasta yaralı da temel yaşam desteği uygulaması için doğru ifadedir?",
                    "options": ["A. Bebeklerde suni solunumda ciğer dolusu hava verilir", "B. Bebeklerde kalp masajı suni solunum yapılır", "C. İlkyardımcı suni solunum vermek için ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir", "D. İlkyardımcı bilinci ve solunumu olmayan bebeğe kalp masajı ve 5 suni solunum verir"],
                    "answer": "C. İlkyardımcı suni solunum vermek için ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir",
                    "explanation": "Bebeklerde suni solunum yapılırken, ilkyardımcı ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir ve her biri 1 saniyeden uzun süren 2 kurtarıcı soluk verir.",
                    "wrong_explanations": {
                        "A. Bebeklerde suni solunumda ciğer dolusu hava verilir": "Bebeklerde ciğer dolusu hava vermek akciğerlere zarar verebilir.",
                        "B. Bebeklerde kalp masajı suni solunum yapılır": "Bebeklerde hem kalp masajı hem de suni solunum yapılır, ancak bu ifade doğru değildir.",
                        "D. İlkyardımcı bilinci ve solunumu olmayan bebeğe kalp masajı ve 5 suni solunum verir": "Bebeklerde temel yaşam desteğine 2 kurtarıcı soluk ile başlanır, sonra kalp masajı yapılır."
                    }
                },
                {
                    "question": "11- ilkyardımcının yetişkin bir hasta yaralıya uygulayacağı kalp masajı ile ilgili aşağıdaki ifadelerden hangisi doğrudur?",
                    "options": ["A. Tek el ile göğüs kemiği 2-3 cm aşağı inecek şekilde bası uygulamak", "B. Tek elin orta ve yüzük parmağı ile göğüs kafesi 5 cm aşağı inecek şekilde bası uygulamak", "C. İki el ile göğüs kafesi 5 cm aşağı inecek şekilde bası uygulama", "D. İki el ile göğüs kafesi 3 cm aşağı inecek şekilde bası uygulamak"],
                    "answer": "C. İki el ile göğüs kafesi 5 cm aşağı inecek şekilde bası uygulama",
                    "explanation": "Yetişkinlerde kalp masajı, göğüs kafesi 5 cm aşağı inecek şekilde iki el ile uygulanır.",
                    "wrong_explanations": {
                        "A. Tek el ile göğüs kemiği 2-3 cm aşağı inecek şekilde bası uygulamak": "Tek el ile kalp masajı çocuklarda uygulanır ve bası derinliği 5 cm olmalıdır.",
                        "B. Tek elin orta ve yüzük parmağı ile göğüs kafesi 5 cm aşağı inecek şekilde bası uygulamak": "Bu teknik bebeklerde kullanılır ve bası derinliği 4 cm olmalıdır.",
                        "D. İki el ile göğüs kafesi 3 cm aşağı inecek şekilde bası uygulamak": "Bası derinliği 5 cm olmalıdır."
                    }
                },
                {
                    "question": "12- havayolunun kısmi tıkanmasında aşağıdakilerden hangisi yapılır?",
                    "options": ["A. Heimlich manevrası uygulanır", "B. Öksürmeye teşvik edilir", "C. Kurtarıcı nefes verilir", "D. Şok pozisyonu verilir"],
                    "answer": "B. Öksürmeye teşvik edilir",
                    "explanation": "Hava yolunun kısmi tıkanmasında kişi öksürebilir, konuşabilir ve nefes alabilir. Bu durumda öksürmeye teşvik edilmelidir. Tam tıkanmada ise Heimlich manevrası uygulanır.",
                    "wrong_explanations": {
                        "A. Heimlich manevrası uygulanır": "Heimlich manevrası tam tıkanmada uygulanır.",
                        "C. Kurtarıcı nefes verilir": "Kurtarıcı nefes, solunumu durmuş kişilere verilir.",
                        "D. Şok pozisyonu verilir": "Şok pozisyonu, şok durumundaki hastalara verilir."
                    }
                },
                {
                    "question": "13- bir yaşın altındaki bebekte göğüs kemiğinde belirlenen noktaya aşağıdaki tekniklerin hangisi yapılır?",
                    "options": ["A. bir elin topuğu ile", "B. iki elin topuğu ile", "C. Tek parmak ile", "D. İki parmak ile"],
                    "answer": "D. İki parmak ile",
                    "explanation": "Bir yaşın altındaki bebeklerde kalp masajı, iki meme başının altındaki hattın ortasına iki parmak ile uygulanır.",
                    "wrong_explanations": {
                        "A. bir elin topuğu ile": "Bir elin topuğu ile kalp masajı çocuklarda uygulanır.",
                        "B. iki elin topuğu ile": "İki elin topuğu ile kalp masajı yetişkinlerde uygulanır.",
                        "C. Tek parmak ile": "Tek parmak ile kalp masajı yapılmaz."
                    }
                },
                {
                    "question": "14- ilkyardımcı hangi yaş grubunu çocuk olarak değerlendirmelidir?",
                    "options": ["A. 0-1 yaş arası", "B. 2-5 yaş arası", "C. 1-8 yaş arası", "D. 5-10 yaş arası"],
                    "answer": "C. 1-8 yaş arası",
                    "explanation": "İlkyardımda çocuk yaş grubu 1-8 yaş arası olarak kabul edilir. 0-1 yaş arası bebek, 8 yaş üzeri ise yetişkin olarak değerlendirilir.",
                    "wrong_explanations": {
                        "A. 0-1 yaş arası": "0-1 yaş arası bebek olarak değerlendirilir.",
                        "B. 2-5 yaş arası": "Bu aralık çocuk yaş grubunun bir kısmını kapsar ancak tam tanım değildir.",
                        "D. 5-10 yaş arası": "Bu aralık çocuk yaş grubunun bir kısmını kapsar ancak tam tanım değildir."
                    }
                },
                {
                    "question": "15- kanı süzerek gerekli maddelerin vücutta tutulmasını zararlı olanların atılması görevlerini yaparak vücutta iç dengeyi koruyan sistem hangisidir?",
                    "options": ["A. Dolaşım sistemi", "B. Solunum sistemi", "C. Boşaltım sistemi", "D. Sindirim sistemi"],
                    "answer": "C. Boşaltım sistemi",
                    "explanation": "Boşaltım sistemi, kanı süzerek vücut için gerekli maddelerin tutulmasını ve zararlı atık maddelerin atılmasını sağlar. Bu sayede vücudun iç dengesini (homeostaz) korur.",
                    "wrong_explanations": {
                        "A. Dolaşım sistemi": "Dolaşım sistemi, kanı vücutta taşıyarak oksijen ve besin maddelerini hücrelere ulaştırır, atık maddeleri toplar.",
                        "B. Solunum sistemi": "Solunum sistemi, vücuda oksijen alıp karbondioksit veren sistemdir.",
                        "D. Sindirim sistemi": "Sindirim sistemi, alınan besinleri öğütülerek sindirilmesini ve emilimini sağlar."
                    }
                },
                {
                    "question": "16- iç kanamalarda yapılan ilk yardım müdahalesinde aşağıdakilerden hangisi yapılmaz?",
                    "options": ["A. Ağızdan sıcak içecek verilir", "B. Şok pozisyonu verilir", "C. Yaşam bulguları incelenir", "D. Üstü örtülerek sıcak tutulur"],
                    "answer": "A. Ağızdan sıcak içecek verilir",
                    "explanation": "İç kanaması olan bir hastaya ağızdan yiyecek veya içecek verilmemelidir. Bu, kanamayı artırabilir veya başka komplikasyonlara yol açabilir.",
                    "wrong_explanations": {
                        "B. Şok pozisyonu verilir": "İç kanama şoka neden olabileceği için, şok pozisyonu (ayakları 30 cm yukarı kaldırma) uygulanabilir.",
                        "C. Yaşam bulguları incelenir": "Yaşamsal bulguların (nabız, solunum, tansiyon) düzenli olarak izlenmesi, hastanın durumundaki değişiklikleri takip etmek için önemlidir.",
                        "D. Üstü örtülerek sıcak tutulur": "Hastanın vücut ısısını korumak için üstü örtülerek sıcak tutulması önemlidir."
                    }
                },
                {
                    "question": "17- Aşağıdakilerden hangisi şok belirtilerinden değildir?",
                    "options": ["A. Kan basıncında artma", "B. hızlı ve yüzeysel solunum", "C. Ciltte soğukluk solukluk nemlilik", "D. Endişe huzursuzluk baş dönmesi"],
                    "answer": "A. Kan basıncında artma",
                    "explanation": "Şokta kan basıncı düşer, artmaz. Diğer seçenekler şokun belirtileridir.",
                    "wrong_explanations": {
                        "B. hızlı ve yüzeysel solunum": "Hızlı ve yüzeysel solunum, şokun önemli belirtilerindendir.",
                        "C. Ciltte soğukluk solukluk nemlilik": "Ciltte soğukluk, solukluk ve nemlilik, şokun önemli belirtilerindendir.",
                        "D. Endişe huzursuzluk baş dönmesi": "Endişe, huzursuzluk ve baş dönmesi, şokun önemli belirtilerindendir."
                    }
                },
                {
                    "question": "18- aşağıdaki durumlardan hangisinde turnike uygulanır?",
                    "options": ["A. toplardamar kanamalarında", "B. Akrep yılan sokmasında", "C. Delici aletle oluşan karın yaralanmalarında", "D. Çok sayıda yaralının bulunduğu ortamda tek ilk yardımcı varsa"],
                    "answer": "D. Çok sayıda yaralının bulunduğu ortamda tek ilk yardımcı varsa",
                    "explanation": "Turnike, uzuv kopması, çok sayıda yaralının olduğu ve tek ilkyardımcının bulunduğu ortamlar gibi durumlarda kanamayı durdurmak için kullanılır. Toplardamar kanamaları, akrep/yılan sokmaları ve delici karın yaralanmalarında turnike uygulanmaz.",
                    "wrong_explanations": {
                        "A. toplardamar kanamalarında": "Toplardamar kanamalarında genellikle doğrudan baskı uygulanır, turnike değil.",
                        "B. Akrep yılan sokmasında": "Akrep veya yılan sokmalarında turnike uygulanması zehrin yayılmasını hızlandırabilir.",
                        "C. Delici aletle oluşan karın yaralanmalarında": "Delici karın yaralanmalarında turnike uygulanmaz, yara kapatılır ve tıbbi yardım beklenir."
                    }
                },
                {
                    "question": "19- Aşağıdakilerden hangisi burun kanamalarında yapılan ilk yardım uygulamasıdır?",
                    "options": ["A. hasta yaralının başı geriye doğru yatırılır", "B. Burun kanatları 5 dakika süre ile sıkılır", "C. Pamuklu çubuk ile burun içi ileri geri yapılarak temizlenir", "D. Burun deliklerine tampon uygulanır"],
                    "answer": "B. Burun kanatları 5 dakika süre ile sıkılır",
                    "explanation": "Burun kanamalarında, hasta/yaralının başı hafifçe öne eğilerek burun kanatları 5 dakika süre ile sıkılmalıdır. Bu, kanamanın durmasına yardımcı olur.",
                    "wrong_explanations": {
                        "A. hasta yaralının başı geriye doğru yatırılır": "Başı geriye yatırmak, kanın genize akmasına ve yutulmasına neden olabilir.",
                        "C. Pamuklu çubuk ile burun içi ileri geri yapılarak temizlenir": "Burun içini pamuklu çubukla temizlemek, kanamayı artırabilir ve enfeksiyon riskini yükseltebilir.",
                        "D. Burun deliklerine tampon uygulanır": "Burun deliklerine tampon uygulamak, kanamayı durdurmak yerine kanın içeride birikmesine neden olabilir ve çıkarılırken tekrar kanamaya yol açabilir."
                    }
                },
                {
                    "question": "20- kulak kanaması görülen bilinci kapalı ve solunumu olan hasta yaralıya hangi pozisyon verilir?",
                    "options": ["A. Kanayan kulak üste kalacak şekilde koma pozisyonu", "B. Kanayan kulak altta kalacak şekilde koma pozisyonu", "C. Yarı oturur pozisyon", "D. Şok pozisyonu"],
                    "answer": "B. Kanayan kulak altta kalacak şekilde koma pozisyonu",
                    "explanation": "Kulak kanaması görülen bilinci kapalı ve solunumu olan hasta/yaralıya, kanayan kulak altta kalacak şekilde koma pozisyonu verilmelidir. Bu, kanın dışarı akmasını sağlayarak beyin içine basınç yapmasını engeller.",
                    "wrong_explanations": {
                        "A. Kanayan kulak üste kalacak şekilde koma pozisyonu": "Kanayan kulak üstte kalacak şekilde pozisyon vermek, kanın beyin içine akmasına neden olabilir.",
                        "C. Yarı oturur pozisyon": "Yarı oturur pozisyon, kulak kanamalarında uygun bir pozisyon değildir.",
                        "D. Şok pozisyonu": "Şok pozisyonu, kulak kanamalarında uygun bir pozisyon değildir."
                    }
                }
            ]
        },
        "Test 10": {
            "questions": [
                {
                    "question": "1-Aşağıdakilerden hangisi ilkyardım için yanlış bir ifadedir?",
                    "options": ["A. Hayati tehlikeyi ortadan kaldırmak ve yaşamsal fonksiyonların sürdürülmesi amacıyla yapılır", "B. Olay yerinde mevcut imkânlarla ilkyardım eğitimi almış kişilerce yapılır", "C. İlkyardımda amaç hasta/yaralıyı tedavi etmektir.", "D. İlaçsız yapılan uygulamalardır"],
                    "answer": "C. İlkyardımda amaç hasta/yaralıyı tedavi etmektir.",
                    "explanation": "İlkyardımın amacı, hayat kurtarmak, durumun kötüleşmesini önlemek ve iyileşmeyi kolaylaştırmaktır. Tedavi etmek, sağlık profesyonellerinin görevidir.",
                    "wrong_explanations": {
                        "A. Hayati tehlikeyi ortadan kaldırmak ve yaşamsal fonksiyonların sürdürülmesi amacıyla yapılır": "Bu, ilkyardımın doğru amaçlarından biridir.",
                        "B. Olay yerinde mevcut imkânlarla ilkyardım eğitimi almış kişilerce yapılır": "Bu, ilkyardımın doğru tanımına uyar.",
                        "D. İlaçsız yapılan uygulamalardır": "İlkyardım, ilaçsız yapılan uygulamaları kapsar."
                    }
                },
                {
                    "question": "2-112'nin aranması sırasında aşağıdakilerden hangisi yapılmamalıdır?",
                    "options": ["A. Sorulan sorulara net cevaplar verilmelidir.", "B. Kesin yer ve adres bilgileri verilmelidir.", "C. Telefon hemen kapatılmalıdır.", "D. Kimin hangi numaradan aradığı bildirilmelidir."],
                    "answer": "C. Telefon hemen kapatılmalıdır.",
                    "explanation": "112 aranırken, tüm bilgiler verildikten sonra karşıdaki görevli kapat demeden telefon kapatılmamalıdır. Çünkü görevlinin ek soruları veya yönlendirmeleri olabilir.",
                    "wrong_explanations": {
                        "A. Sorulan sorulara net cevaplar verilmelidir.": "Bu, doğru bir davranıştır.",
                        "B. Kesin yer ve adres bilgileri verilmelidir.": "Bu, doğru bir davranıştır.",
                        "D. Kimin hangi numaradan aradığı bildirilmelidir.": "Bu, doğru bir davranıştır."
                    }
                },
                {
                    "question": "3- Aşagıda yer alan sistem ve yapı eşleştirmelerinden hangisi yanlış verilmiştir?",
                    "options": ["A. Sindirim sistemi-safra kesesi", "B. Dolaşım sistemi-kalp", "C. Sinir sistemi-beyin", "D. Hareket sistemi-omurilik"],
                    "answer": "D. Hareket sistemi-omurilik",
                    "explanation": "Omurilik, sinir sisteminin bir parçasıdır. Hareket sistemi kemikler, kaslar ve eklemlerden oluşur.",
                    "wrong_explanations": {
                        "A. Sindirim sistemi-safra kesesi": "Safra kesesi, sindirim sistemine yardımcı bir organdır.",
                        "B. Dolaşım sistemi-kalp": "Kalp, dolaşım sisteminin ana organıdır.",
                        "C. Sinir sistemi-beyin": "Beyin, sinir sisteminin ana organıdır."
                    }
                },
                {
                    "question": "4- Trafik kazasında araç içerisinde bilinci açık görünür bir kanaması ve kırığı olmayan bir yaralıya olay yerinde bir tehlike yoksa ilkyardımda ne yapılmalıdır?",
                    "options": ["A. Koma pozisyonu verilir.", "B. Rentek yöntemiyle araçtan çıkarılır.", "C. Sağlık ekipleri gelene kadar hastanın yanında kalıp endişeleri giderilir.", "D. Suni solunum ve dış kalp masajı yapılır."],
                    "answer": "C. Sağlık ekipleri gelene kadar hastanın yanında kalıp endişeleri giderilir.",
                    "explanation": "Trafik kazalarında, olay yerinde tehlike yoksa ve yaralının durumu stabil ise, sağlık ekipleri gelene kadar yaralının hareket ettirilmemesi ve endişelerinin giderilmesi önemlidir. Gereksiz hareket, durumu kötüleştirebilir.",
                    "wrong_explanations": {
                        "A. Koma pozisyonu verilir.": "Koma pozisyonu, bilinci kapalı olan ve solunumu olan hastalara verilir.",
                        "B. Rentek yöntemiyle araçtan çıkarılır.": "Rentek yöntemi, omurilik yaralanması şüphesi olan ve araçtan çıkarılması gereken hastalarda kullanılır, ancak bu durumda öncelik değildir.",
                        "D. Suni solunum ve dış kalp masajı yapılır.": "Suni solunum ve dış kalp masajı, solunumu ve kalbi durmuş hastalara yapılır."
                    }
                },
                {
                    "question": "5- Aşağıdakilerden hangisi olay yerini değerlendirmenin amaçlarından biri değildir?",
                    "options": ["A. Olay yerinde tekrar kaza olma riskinin ortadan kaldırılması", "B. Olay yerindeki hasta/yaralı sayısının belirlenmesi", "C. Olay yerinde hasta/yaralı türünün belirlenmesi", "D. Olay yerindeki maddi hasarın boyutunun belirlenmesi"],
                    "answer": "D. Olay yerindeki maddi hasarın boyutunun belirlenmesi",
                    "explanation": "Olay yerini değerlendirmenin temel amacı, güvenliği sağlamak, hasta/yaralı sayısını ve türünü belirlemek, yapılacak müdahaleleri planlamaktır. Maddi hasarın boyutu ilk yardımın amaçlarından değildir.",
                    "wrong_explanations": {
                        "A. Olay yerinde tekrar kaza olma riskinin ortadan kaldırılması": "Bu, olay yeri güvenliğini sağlamak için önemli bir adımdır.",
                        "B. Olay yerindeki hasta/yaralı sayısının belirlenmesi": "Hasta/yaralı sayısını belirlemek, kaynakları doğru kullanmak ve yardım çağırmak için önemlidir.",
                        "C. Olay yerinde hasta/yaralı türünün belirlenmesi": "Hasta/yaralı türünü belirlemek, uygun ilk yardım müdahalesini seçmek için önemlidir."
                    }
                },
                {
                    "question": "6-Vucuda gerekli olan gaz alış verişi görevini yaparak hücre ve dokuların oksijenlenmesini sağlayan vücut sistemi hangisidir?",
                    "options": ["A. Hareket sistemi", "B. Boşaltım sistemi", "C. Sindirim sistemi", "D. Solunum sistemi"],
                    "answer": "D. Solunum sistemi",
                    "explanation": "Solunum sistemi, vücuda gerekli olan oksijeni alıp karbondioksiti dışarı atarak hücre ve dokuların oksijenlenmesini sağlar.",
                    "wrong_explanations": {
                        "A. Hareket sistemi": "Hareket sistemi, vücudun hareket etmesini ve desteklenmesini sağlar.",
                        "B. Boşaltım sistemi": "Boşaltım sistemi, kanı süzerek zararlı maddelerin atılmasını sağlar.",
                        "C. Sindirim sistemi": "Sindirim sistemi, alınan besinleri öğütülerek sindirilmesini ve emilimini sağlar."
                    }
                },
                {
                    "question": "7-Bir insanın normal vücut ısısı koltuk altından ölçüldüğünde kaç derecedir?",
                    "options": ["A.35", "Β. 36.5", "C. 38", "D. 35.5"],
                    "answer": "Β. 36.5",
                    "explanation": "Bir insanın normal vücut ısısı koltuk altından ölçüldüğünde 36.5°C'dir. Bu değer, vücudun sağlıklı bir şekilde işlev görmesi için ideal sıcaklıktır.",
                    "wrong_explanations": {
                        "A.35": "35°C, hipotermi sınırına yakın bir değerdir ve normal değildir.",
                        "C. 38": "38°C, hafif ateşi gösterir ve normal değildir.",
                        "D. 35.5": "35.5°C, normalin altında bir değerdir ve hipotermiye işaret edebilir."
                    }
                },
                {
                    "question": "8- Temel yaşam desteği uygularken tepki veren hasta/yaralıya ilk önce ne yapılır?",
                    "options": ["A. Hasta/yaralının bilinç solunum kontrolü ve ikinci değerlendirme yapılır.", "B. Hasta/yaralıya koma pozisyonu verilir", "C. Bir şey yapılmadan sağlık ekipleri beklenir.", "D. Hasta yaralıya şok pozisyonu verilir"],
                    "answer": "A. Hasta/yaralının bilinç solunum kontrolü ve ikinci değerlendirme yapılır.",
                    "explanation": "Temel yaşam desteği uygularken hasta/yaralı tepki vermeye başlarsa, öncelikle bilinç ve solunum kontrolü tekrar yapılmalı ve ardından ikinci değerlendirmeye geçilmelidir. Bu, hastanın durumundaki değişikliği anlamak ve uygun müdahaleyi sürdürmek için önemlidir.",
                    "wrong_explanations": {
                        "B. Hasta/yaralıya koma pozisyonu verilir": "Koma pozisyonu, bilinci kapalı ancak solunumu olan hastalara verilir. Tepki veren bir hastaya koma pozisyonu vermek uygun değildir.",
                        "C. Bir şey yapılmadan sağlık ekipleri beklenir.": "Hasta tepki vermeye başladığında, durumu değerlendirmek ve gerekirse müdahaleye devam etmek önemlidir.",
                        "D. Hasta yaralıya şok pozisyonu verilir": "Şok pozisyonu, şok durumundaki hastalara verilir. Tepki veren bir hastaya şok pozisyonu vermek her zaman gerekli değildir."
                    }
                },
                {
                    "question": "9-Bebek ve çocuklarda Temel yaşam desteği uygulamasına başlama sırası aşağıdakilerden hangisinde doğru olarak verilmiştir?",
                    "options": ["A. 30 kalp masajı 5 nefes", "B. 2 nefes 30 kalp masajı", "C. 2 nefes 15 kalp masajı", "D. 15 kalp masajı 5 nefes"],
                    "answer": "B. 2 nefes 30 kalp masajı",
                    "explanation": "Bebek ve çocuklarda temel yaşam desteği uygulamasına 2 kurtarıcı nefes ile başlanır, ardından 30 kalp masajı yapılır. Bu döngü, tıbbi yardım gelene kadar devam ettirilir.",
                    "wrong_explanations": {
                        "A. 30 kalp masajı 5 nefes": "Bu oran yanlıştır. Doğru oran 2 nefes 30 kalp masajıdır.",
                        "C. 2 nefes 15 kalp masajı": "Bu oran yanlıştır. Doğru oran 2 oran 2 nefes 30 kalp masajıdır.",
                        "D. 15 kalp masajı 5 nefes": "Bu oran yanlıştır. Doğru oran 2 nefes 30 kalp masajıdır."
                    }
                },
                {
                    "question": "10- Yetişkinlerde Hemlich manevrası hangi bölgeye uygulanır?",
                    "options": ["A. Göğüs kemiğinin orta kısmına", "B. Göğüs kemiğinin 2 parmak üstüne", "C. Göğüs kemiğinin altı midenin üst kısmına", "D. Göbek deliğinin altına"],
                    "answer": "C. Göğüs kemiğinin altı midenin üst kısmına",
                    "explanation": "Yetişkinlerde Heimlich manevrası, göğüs kemiğinin altı midenin üst kısmına, yani kaburgaların birleştiği noktanın hemen altına uygulanır. Bu, karın bölgesine yapılan baskı ile hava yolunu tıkayan cismin dışarı atılmasını sağlar.",
                    "wrong_explanations": {
                        "A. Göğüs kemiğinin orta kısmına": "Bu bölge, kalp masajı için kullanılır, Heimlich manevrası için değil.",
                        "B. Göğüs kemiğinin 2 parmak üstüne": "Bu bölge, Heimlich manevrası için doğru değildir.",
                        "D. Göbek deliğinin altına": "Bu bölge, Heimlich manevrası için doğru değildir."
                    }
                },
                {
                    "question": "11- Hava yolu açıklığının değerlendirilmesi ile ilgili hangisi yanlıştır?",
                    "options": ["A. Dilin geriye kaçarak hava yolunu tıkamasıdır.", "B. Ağız kontrolü önce göz ile yapılır.", "C. Tüm hareketler yumuşak şekilde yapılmalıdır.", "D. Önce baş çene pozisyonu verilir daha sonra ağız içi kontrol edilir"],
                    "answer": "D. Önce baş çene pozisyonu verilir daha sonra ağız içi kontrol edilir",
                    "explanation": "Hava yolu açıklığı sağlanırken, öncelikle ağız içi kontrol edilmeli ve gözle görülen bir cisim varsa çıkarılmalıdır. Daha sonra baş geri-çene yukarı pozisyonu verilerek hava yolu açılmalıdır.",
                    "wrong_explanations": {
                        "A. Dilin geriye kaçarak hava yolunu tıkamasıdır.": "Bu, bilinçsiz kişilerde hava yolu tıkanıklığının yaygın bir nedenidir.",
                        "B. Ağız kontrolü önce göz ile yapılır.": "Bu, hava yolu açıklığı değerlendirmesinde doğru bir adımdır.",
                        "C. Tüm hareketler yumuşak şekilde yapılmalıdır.": "Hava yolu açıklığı sağlanırken nazik ve dikkatli olmak önemlidir."
                    }
                },
                {
                    "question": "12- Hava yolunun tam tıkanmasındaki müdahale şekli aşağıdakilerden hangisinde doğru olarak verilmiştir?",
                    "options": ["A. Hasta öksürmeye teşvik edilir", "B. Önce sırta 5 kez vurulur sonra hemlich manevrası uygulanır.", "C. Hastanın hava yolunu açmak için baş-çene manevrası uygulanır", "D. Hastanın su içmesi sağlanır."],
                    "answer": "B. Önce sırta 5 kez vurulur sonra hemlich manevrası uygulanır.",
                    "explanation": "Hava yolunun tam tıkanmasında, bilinci açık kişilerde 5 kez sırta vurulur ve ardından 5 kez Heimlich manevrası uygulanır. Bu döngü, cisim çıkana veya kişi bilincini kaybedene kadar devam ettirilir.",
                    "wrong_explanations": {
                        "A. Hasta öksürmeye teşvik edilir": "Öksürmeye teşvik etme, kısmi tıkanıklıkta yapılır. Tam tıkanıklıkta kişi öksüremez.",
                        "C. Hastanın hava yolunu açmak için baş-çene manevrası uygulanır": "Baş-çene manevrası, hava yolu açıklığını sağlamak için kullanılır, tam tıkanıklığı gidermek için değil.",
                        "D. Hastanın su içmesi sağlanır.": "Tam tıkanıklıkta hastaya su içirmek, durumu daha da kötüleştirebilir."
                    }
                },
                {
                    "question": "13- Yapay solunum ile ilgili verilen şıklardan hangisi doğrudur?",
                    "options": ["A. Erişkinlerde ağız dolusu hava üflenir.", "B. Bebeklerde ağız ve buruna birlikte üflenir.", "C. Bebeklerde mümkün olduğu kadar çok hava üflenir.", "D. Erişkinlerde verilen her soluktan sonra 10 saniye bak dinle hisset yapılır."],
                    "answer": "B. Bebeklerde ağız ve buruna birlikte üflenir.",
                    "explanation": "Bebeklerde yapay solunum yapılırken, ilkyardımcı ağzını bebeğin ağız ve burnunu içine alacak şekilde yerleştirir ve her biri 1 saniyeden uzun süren 2 kurtarıcı soluk verir.",
                    "wrong_explanations": {
                        "A. Erişkinlerde ağız dolusu hava üflenir.": "Erişkinlerde göğsün yükselmesini sağlayacak kadar hava üflenir, ağız dolusu değil.",
                        "C. Bebeklerde mümkün olduğu kadar çok hava üflenir.": "Bebeklerde fazla hava üflemek akciğerlere zarar verebilir.",
                        "D. Erişkinlerde verilen her soluktan sonra 10 saniye bak dinle hisset yapılır.": "Bak-dinle-hisset, solunum kontrolü için yapılır, her soluktan sonra değil."
                    }
                },
                {
                    "question": "14- Solunum yolu kısmi olarak tıkanmış kişide aşağıdakilerden hangisi görülür?",
                    "options": ["A. öksürür", "B. Nefes alamaz", "C. Morarır", "D. Konuşamaz"],
                    "answer": "A. öksürür",
                    "explanation": "Solunum yolu kısmi olarak tıkanmış bir kişide öksürük, konuşma ve nefes alma belirtileri görülür. Tam tıkanıklıkta ise kişi nefes alamaz, konuşamaz ve morarır.",
                    "wrong_explanations": {
                        "B. Nefes alamaz": "Nefes alamama, tam tıkanıklığın belirtisidir.",
                        "C. Morarır": "Morarma, tam tıkanıklığın belirtisidir.",
                        "D. Konuşamaz": "Konuşamama, tam tıkanıklığın belirtisidir."
                    }
                },
                {
                    "question": "15- Yetişkinlerde kalp basısı sırasında göğüs kafesi ne kadar çöktürülmelidir?",
                    "options": ["A. Göğüs kafesinin 1/2 si kadar", "B. Göğüs kafesinin 1/3 ü kadar", "C. Göğüs kafesinin 1/4 ü kadar", "D. Göğüs kafesinin 1/5 i kadar"],
                    "answer": "B. Göğüs kafesinin 1/3 ü kadar"
                },
                {
                    "question": "16- Hangisi kanamalarda vücutta baskı uygulanabilecek noktalardan biri değildir?",
                    "options": ["A. Köprücük kemiği üzeri", "B. Kolun üst bölümü", "C. Uyluk bacak atardamarı", "D. El bileği"],
                    "answer": "D. El bileği"
                },
                {
                    "question": "17- Hangisi şok belirtilerinden değildir?",
                    "options": ["A. Kan basıncında artma", "B. Hızlı ve yüzeysel solunum", "C. Ciltte soğukluk solukluk nemlilik", "D. Endişe huzursuzluk baş dönmesi"],
                    "answer": "A. Kan basıncında artma"
                },
                {
                    "question": "18- Aşağıdakilerden hangisi kanamanın ciddiyetini belirleyen durumlar arasında yer almaz?",
                    "options": ["A. Kanamanın hızı", "B. Kanama miktarı", "C. Kan grubu", "D. Vücutta kanın aktığı bölge"],
                    "answer": "C. Kan grubu"
                },
                {
                    "question": "19- Aşağıdakilerden hangisinde şok pozisyonu doğru tanımlanmıştır?",
                    "options": ["A. Hasta/yaralı başı aşağıda olacak şekilde yatırılıp ayakları 60 cm yükseltilir", "B. Hasta/yaralı başı yukarıda yatırılıp ayakları uzatılır.", "C. Hasta/yaralı sırt üstü yatırılıp ayakları 30 cm yükseltilir.", "D. Hasta/yaralı yan yatırılarak üstteki bacak kıvrılır."],
                    "answer": "C. Hasta/yaralı sırt üstü yatırılıp ayakları 30 cm yükseltilir."
                },
                {
                    "question": "20- Aşağıdakilerden hangisinde baş-boyun-gövde ekseninin bozulmamasına özellikle dikkat edilmelidir?",
                    "options": ["A. Kafatası omurga yaralanmalarında", "B. İç kanaması olan hastalar", "C. Bacak kırıklarında", "D. Kedi köpek ısırmalarında"],
                    "answer": "A. Kafatası omurga yaralanmalarında"
                }
            ]
        }
}