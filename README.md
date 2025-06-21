🛒 Direnc.net Ürün Yorum Analiz Aracı  
Bu proje, belirli bir ürün kategorisindeki (Arduino Ana Board) ürünleri tarayarak kullanıcı yorumlarını toplayan, yorum sayılarını analiz eden ve en çok yorum alan ürünü tespit eden bir web scraping uygulamasıdır.

---

✨ Özellikler

🔍 Direnc.net sitesinde kategori tabanlı ürün arama  
🗂️ Arduino ana kart ürünlerini otomatik olarak listeleme  
📝 Her ürünün yorumlarını toplama ve yorum sayısını belirleme  
📊 En çok yoruma sahip ürünü analiz etme ve bağlantısını yazdırma  
⌛ Dinamik içerik yüklenmesine karşı bekleme mekanizmaları (WebDriverWait, sleep)  
📦 Toplanan yorumların terminalde görüntülenmesi

---

📦 Kullanılan Teknolojiler

- 🐍 **Python** – Temel betik dili  
- 🌐 **Selenium WebDriver** – Web tarayıcı otomasyonu  
- 📊 **pandas** – Veri işleme (potansiyel kullanım)  
- 📈 **matplotlib / seaborn** – Görselleştirme (potansiyel kullanım)  
- 🛠️ **ChromeDriver** – Chrome tarayıcısıyla etkileşim  

---

🛠️ Kurulum ve Çalıştırma

1. Python 3.x kurulu olduğundan emin olun.  
2. Gerekli Python kütüphanelerini yükleyin:

```bash
pip install selenium pandas matplotlib seaborn
python web_scraping.py
