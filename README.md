# 🥊 UFC Karşılaşmaları İçin Açıklanabilir Karar Destek Sistemi

**Geliştirici:** Kaan Unutur - Manisa Celal Bayar Üniversitesi, Veri Bilimi ve Analitiği
**Ders:** Akademik Yapay Zekaya Giriş

## 📌 Problem Tanımı
Profesyonel karma dövüş sanatları (MMA) müsabakalarında, hangi istatistiksel faktörlerin (yaş, boy, uzanma mesafesi, vuruş isabet oranı vb.) galibiyette daha kritik rol oynadığı genellikle gözleme dayalıdır. Bu durum, sonuca yönelik veriye dayalı objektif öngörü eksikliği yaratmaktadır.

## 🎯 Hedef Kullanıcı
MMA antrenörleri, spor istatistikçileri, müsabaka izleyicileri ve dövüş analistleri.

## 💡 Çözümün Kısa Açıklaması
Bu ürün, UFC geçmiş maç verilerini kullanarak iki dövüşçü arasındaki olası maç sonucunu tahmin eden bir makine öğrenmesi karar destek sistemidir. Kara kutu (black-box) bir tahmin yerine, SHAP analizi ile modelin hangi özelliklere (örn. uzanma mesafesi veya isabetli vuruş) dayanarak bu kararı verdiğini açıklar.

## 🛠️ Kullanılan Teknolojiler
* **Veri İşleme ve Analiz:** Python, Pandas
* **Makine Öğrenmesi:** Scikit-Learn (Random Forest), XGBoost
* **Açıklanabilir Yapay Zeka (XAI):** SHAP
* **Web Arayüzü:** Streamlit
* **Sürüm Kontrolü:** Git & GitHub

## ⚙️ Sistem Mimarisi ve İş Akışı
1. **Veri Ön İşleme:** Kaggle'dan alınan ham UFC verisindeki eksik değerler medyan ile doldurulmuş, beraberlikler (Draw) veri setinden çıkarılarak hedef değişken ikili (Kırmızı/Mavi) formata getirilmiştir.
2. **Model Eğitimi:** Random Forest ve XGBoost algoritmaları %80 Eğitim, %20 Test verisi ile eğitilerek karşılaştırılmıştır.
3. **Açıklanabilirlik:** En başarılı model olan Random Forest üzerine SHAP entegre edilerek karar mekanizması görselleştirilmiştir.
4. **Kullanıcı Arayüzü:** Streamlit ile kullanıcının veri girebileceği ve anlık tahmin alabileceği etkileşimli bir panel oluşturulmuştur.

## 🚀 Kurulum Adımları
Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Depoyu klonlayın:
```bash
git clone https://github.com/kaanunutur4-wq/final-projesi-kaan-unutur.git
cd final-projesi-kaan-unutur
```

2. Gerekli kütüphaneleri yükleyin:
```bash
pip install pandas scikit-learn xgboost shap streamlit joblib
```

## 🎮 Kullanım Biçimi
Terminal üzerinden aşağıdaki komutu çalıştırarak web arayüzünü başlatabilirsiniz:
```bash
streamlit run app.py
```
Açılan tarayıcı penceresinde Kırmızı ve Mavi köşe dövüşçülerine ait yaş, boy, uzanma mesafesi ve istatistiksel verileri girerek "Sonucu Tahmin Et" butonuna tıklayınız.
## 📸 Örnek Ekran Görüntüleri

**1. Veri Giriş Ekranı:**
![Veri Giriş Ekranı](images/arayuz1.png.png)

**2. Model Tahmin Sonucu:**
![Tahmin Sonucu](images/arayuz2.png.png)


## 📊 Test Sonuçları
Veri seti üzerinde yapılan testlerde iki model karşılaştırılmıştır:
* **Random Forest Doğruluk (Accuracy):** %67.82 (Seçilen Model)
* **XGBoost Doğruluk (Accuracy):** %65.28

## 🚧 Bilinen Sınırlılıklar
* Model, dövüşçülerin psikolojik durumlarını, dövüş kampı kalitesini veya anlık sakatlık gibi dış faktörleri ölçememektedir.
* Sadece sayısal ortalama istatistiklere dayandığı için ilk kez UFC'ye çıkan (geçmiş verisi olmayan) dövüşçülerde kullanılamaz.

## 🔮 Gelecekte Yapılabilecek Geliştirmeler
* UFC API'leri üzerinden canlı veri çekilerek yaklaşan etkinliklerin otomatik analiz edilmesi.
* Dövüşçülerin geçmiş maçlarındaki sakatlık geçmişinin veriye entegre edilmesi.

## 🤖 Yapay Zeka Araçlarının Kullanımı
Bu projenin geliştirilme sürecinde kod hatalarının (syntax error, dosya yolu problemleri vb.) çözümü, SHAP kütüphanesinin projeye entegrasyonu ve veri temizleme adımlarının yapılandırılmasında **Gemini** modelinden destek alınmıştır. Yazılan tüm kodlar tarafımca kontrol edilmiş ve test edilmiştir.

## 🎥 Proje Tanıtım Videosu
(https://youtu.be/5KwAJoki9A0)