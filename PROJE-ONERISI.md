# PROJE ÖNERİSİ: UFC Kural ve Tarihçe Asistanı

**Seçilen Görev Numarası:** SEÇENEK 1 - RAG Tabanlı Uzman Bilgi Asistanı

**Ürünün Adı:** UFC Kural ve Tarihçe Asistanı

**Çözülecek Problem:** Karmaşık Karma Dövüş Sanatları (MMA) kurallarının, güncel puanlama kriterlerinin ve dövüşçü haklarının hızlıca sorgulanamaması; taraftarlar veya spor analistleri tarafından anında teyit edilememesi.

**Hedef Kullanıcı:** UFC izleyicileri, spor analistleri, bahis istatistikçileri ve MMA antrenörleri.

**Kullanılacak Veri veya Bilgi Kaynakları:**
1. UFC Resmi Kurallar Kitapçığı (Unified Rules of MMA)
2. Hakem Puanlama ve Karar Kriterleri Dokümanı
3. Anti-Doping (USADA/DFIA) Politikası ve Kuralları
4. UFC Ağırlık Sınıfları ve Tıbbi Ceza (Medical Suspension) Yönergeleri
5. Yasaklı Vuruşlar ve Faul Yönetmeliği

**Kullanılması Planlanan Teknolojiler:** * Programlama Dili: Java
* RAG Altyapısı: LangChain4j
* Vektör Veritabanı: ChromaDB veya benzeri bir yerel çözüm.
* Arayüz: Temel düzeyde Java (Swing/JavaFX) veya web tabanlı basit bir arayüz.

**Beklenen Ürün Çıktısı:** Kullanıcının doğal dilde sorular sorabildiği (Örn: "12-6 dirsek vuruşları yasal mıdır?"), sadece sisteme yüklenen resmi dokümanları tarayarak cevap veren ve verdiği cevabın hangi dokümandan alındığını açıkça gösteren çalışan bir bilgi asistanı.

**Ürünün Diğer Çalışmalardan Ayrılan Yönü:** Genel amaçlı büyük dil modelleri (LLM), spor kuralları hakkında halüsinasyon görüp yanlış veya güncel olmayan bilgiler uydurabilmektedir. Bu asistan, Sektörel YZ (Vertical AI) prensibiyle tasarlanarak sadece sağlanan spesifik dokümanlarla sınırlandırılmış, doğrulanabilir ve kaynak gösteren spesifik bir araç olacaktır.
