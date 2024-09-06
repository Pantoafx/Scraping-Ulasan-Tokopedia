import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Load existing data from CSV
existing_df = pd.read_csv('DataScrap.csv')

url = 'https://www.tokopedia.com/distrilapid/review'

if url:
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    data = []

    for _ in range(60): 
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']")))
        soup = BeautifulSoup(driver.page_source, "html.parser")
        containers = soup.findAll('article', attrs={'class': 'css-ccpe8t'})

        for container in containers:
            try:
                nama = container.find('span', class_='name').text.strip()
            except AttributeError:
                nama = "Nama tidak ditemukan"

            # Mencari 'Tipe Barang' dengan beberapa cara jika tidak ditemukan
            tipe_barang = container.find('p', class_='css-1ig3wia-unf-heading e1qvo2ff8')
            if not tipe_barang:
                tipe_barang = container.find('p', class_='css-ra461b-unf-heading e1qvo2ff8')
            tipe_barang = tipe_barang.text.strip() if tipe_barang else "Tipe barang tidak ditemukan"

            try:
                varian_barang = container.find('p', class_='css-fwcdjp-unf-heading e1qvo2ff8')
                varian_barang = varian_barang.text.strip() if varian_barang else "Varian barang tidak ditemukan"
            except AttributeError:
                varian_barang = "Varian barang tidak ditemukan"
            
            try:
                rating_text = container.find('div', {'data-testid': 'icnStarRating'}).get('aria-label', 'Tidak ada rating')
                rating = ''.join(filter(str.isdigit, rating_text))  # Mengambil angka saja dari rating
            except AttributeError:
                rating = "Rating tidak ditemukan"

            review_elem = container.find('span', attrs={'data-testid': 'lblItemUlasan'})
            review = review_elem.text.strip() if review_elem else "Ulasan tidak ditemukan"

            try:
                tanggal = container.find('p', class_='css-1dfgmtm-unf-heading e1qvo2ff8').text.strip()
            except AttributeError:
                tanggal = "Tanggal tidak ditemukan"

            data.append((nama, tipe_barang, varian_barang, review, rating, tanggal))

        next_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label^='Laman berikutnya']")
        if next_button.is_enabled():
            next_button.click()
            time.sleep(5)  # Tambahkan penundaan 5 detik setelah mengklik tombol "Laman berikutnya"
        else:
            break

    driver.quit()

    # Buat DataFrame dari data yang di-scrape
    new_df = pd.DataFrame(data, columns=["Nama", "Tipe Barang", "Varian Barang", "Ulasan", "Rating", "Tanggal"])
    
    # Gabungkan data baru dengan data yang sudah ada
    combined_df = pd.concat([existing_df, new_df], ignore_index=True)

    # Remove duplicates
    combined_df = combined_df.drop_duplicates().reset_index(drop=True)

    # Simpan DataFrame ke file CSV yang sama atau file baru
    combined_df.to_csv("DataScrap.csv", index=False, encoding='utf-8-sig')
    print("Scrapping Berhasil...")
