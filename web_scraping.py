from telnetlib import EC

from selenium import webdriver
from time import sleep
# Data manipulation
import pandas as pd
# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# WebDriver'ı başlat ve belirtilen URL'ye git
driver = webdriver.Chrome()
driver.get("https://www.direnc.net/")

# Çerez bildirimini kapatmak için gerekli elementi bul ve tıkla
element = driver.find_element(By.XPATH, '//*[@id="cookie_law_close"]')
element.click()
sleep(35)
#kategoriden arduinoya tıkla
arduino_bul = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'span[style*="background: url(/Data/Kategori/17.png) 5px center no-repeat; background-size:contain;"]')))
arduino_bul.click()
sleep(10)
#arduinonun altındaki kategoriden arduino ana board'a tıkla
anaboard_bul = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li/a[@href='arduino-ana-board']")))
anaboard_bul.click()
sleep(30)
# Sayfadaki ürünlerin divlerini bul
urunler_divler = driver.find_elements(By.XPATH, '//div[contains(@class, "productKapsa") and contains(@class, "fl") and contains(@class, "col-12")]')
# Her bir ürünün linkini alarak listeye ekle
urun_linkleri = []
for div in urunler_divler:
    urun_linki = div.find_element(By.XPATH, './/a').get_attribute('href')
    urun_linkleri.append(urun_linki)
yorum_sayilari={}
# Her bir ürün sayfasını ziyaret et, yorumları aç ve yazdır
for link in urun_linkleri[:4]:
    driver.get(link)
    sleep(40)
    # Yorumları açmak için ilgili bölüme tıklayın
    try:
        # Yorumları açmak için ilgili bölümü bulun ve tıklayın
        yorum_acma_butonu = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'li#commentTab')))
        yorum_acma_butonu.click()

        sleep(30)
        # Yorum içeriklerini bul
        yorum_icerikleri = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div.col.col-12.p-right[itemprop="description"]')))
        # Yorum sayısını al ve sözlüğe ekle
        yorum_sayilari[link] = len(yorum_icerikleri)
        # Her bir yorumun içeriğini yazdırın
        for yorum in yorum_icerikleri:
            print(yorum.text)
    except Exception as e:
        print("Yorum Yok.")
    sleep(20)
en_cok_yorumlu_link = max(yorum_sayilari, key=yorum_sayilari.get)
print("En çok yoruma sahip olan ürünün linki:", en_cok_yorumlu_link)
sleep(5)