import os
from bs4 import BeautifulSoup
import markdownify

def html_to_markdown(html):
    # BeautifulSoup ile HTML'i parse et
    soup = BeautifulSoup(html, "html.parser")
    
    # Gereksiz class ve span etiketlerinden arındır
    for tag in soup.find_all(["span", "div", "a"]):
        tag.unwrap()
    
    # Markdown formatına dönüştür
    markdown_text = markdownify.markdownify(str(soup), heading_style="ATX")
    
    return markdown_text.strip()

# Çalıştırıldığı dizini belirle
current_dir = os.path.dirname(os.path.abspath(__file__))

# Dosya yollarını oluştur
html_file_path = os.path.join(current_dir, "perplexity_response.html")
markdown_file_path = os.path.join(current_dir, "output.md")

# HTML dosyasını oku ve Markdown'a dönüştür
with open(html_file_path, "r", encoding="utf-8") as file:
    html_content = file.read()

markdown_result = html_to_markdown(html_content)

# Markdown çıktısını kaydet
with open(markdown_file_path, "w", encoding="utf-8") as file:
    file.write(markdown_result)

print("Dönüştürme tamamlandı!")
