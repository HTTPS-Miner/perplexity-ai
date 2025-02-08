from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import subprocess

# LibreWolf seçeneklerini tanımla
librewolf_options = webdriver.FirefoxOptions()
librewolf_path = "/usr/bin/firefox"  # LibreWolf'un sistemdeki tam yolu
librewolf_options.binary_location = librewolf_path
# librewolf_options.add_argument("--headless")  # Başsız mod

# WebDriver başlat
driver = webdriver.Firefox(options=librewolf_options)

try:
    # Perplexity AI'yi aç
    driver.get("https://www.perplexity.ai/")
    print("Sayfa yüklendi: ", driver.current_url)

    # Sayfanın tamamen yüklenmesini bekle
    WebDriverWait(driver, 20).until(lambda d: d.execute_script("return document.readyState") == "complete")

    # Giriş kutusunun görünmesini bekle
    input_box = WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.TAG_NAME, "textarea"))
    )
    with open('./prompt.txt', 'r') as file:
        text_content = file.read()
        
    # Giriş kutusuna yazı yaz ve Enter'a bas
    input_box.send_keys(text_content, Keys.RETURN)
    print("Metin gönderildi, Enter tuşuna basıldı.")

    # URL'nin değişmesini bekle (URL'deki 'new?q=' kısmının değişmesini bekle)
    WebDriverWait(driver, 30).until(
        EC.url_contains("new?q=")
    )
    print("URL değişti, yeni URL: ", driver.current_url)

    # Başka bir URL'ye yönlenmeyi bekle
    WebDriverWait(driver, 30).until(
        EC.url_changes(driver.current_url)
    )
    print("Yeni URL'ye yönlendirildi: ", driver.current_url)

    # Yanıt içeriğini içeren div'in görünmesini bekle
    response_container = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[@dir='auto']"))
    )

    # Div içeriğini al ve kaydet
    div_content = response_container.get_attribute("outerHTML")

    # Yanıt içeriğini dosyaya kaydet
    output_path = "./response_to_markdown/perplexity_response.html"
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(div_content)

    print("Yanıt başarıyla kaydedildi!")

except Exception as e:
    import traceback
    print("Hata oluştu:")
    print(traceback.format_exc())

finally:
    # Tarayıcıyı kapat
    driver.quit()
    print("Tarayıcı kapatıldı.")

try:
    # Run the script
    result = subprocess.run(["python", "response_to_markdown/response_to_markdown.py"])
except Exception as e:
    print(f"html to md error: {str(e)}")