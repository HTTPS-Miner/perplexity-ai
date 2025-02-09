**Türkçe Sürüm - README.md**

# Perplexity.ai İçin Selenium Tarayıcı Otomasyonu

## Genel Bakış

Bu proje, **selenium** ve **Firefox** kullanarak [perplexity-ai](https://perplexity.ai/) ile etkileşimleri otomatikleştirir. Script, bir dosyadan metin girişi gönderip, ChatGPT'den yanıt almanızı ve bunu çıktı dosyasına kaydetmenizi sağlar — tüm bunlar, tarayıcıyı manuel olarak açmanıza gerek kalmadan gerçekleştirilir.

https://github.com/user-attachments/assets/98b8be66-8835-4a26-a008-10367a0e8ec1

## Gereksinimler

**Linux üzerinde Python 3.11.2 ile test edilmiştir**

Başlamak için aşağıdaki Python paketlerini kurmanız gerekecek:

```
pip install selenium beautifulsoup4 markdownify
```

## İş Akışı

1. **Giriş Dosyası**: `prompt.txt` adında bir dosya oluşturun ve ChatGPT'ye göndermek istediğiniz mesajı yazın.
2. **Çıktı Dosyası**: ChatGPT'nin verdiği yanıt, `response_to_markdown/output.md` dosyasına kaydedilecektir.

## Yazılım Desteği

- **Crossplatform** - Windows, Linux

## Amaç

Bu aracın temel amacı, Perplexity.ai ile etkileşimleri hızlandırmak ve otomatikleştirerek daha verimli hale getirmektir.

## Kurulum ve Kullanım

### Terminal Komutları

1. Depoyu klonlayın:
   ```shell
   git clone https://github.com/HTTPS-Miner/perplexity-ai
   cd perplexity-ai
   ```

2. Sanal bir ortam oluşturun:
   ```shell
   python3 -m venv myenv
   source myenv/bin/activate
   ```

3. Gerekli bağımlılıkları yükleyin:
   ```shell
   pip install selenium beautifulsoup4 markdownify
   ```

4. Bulunduğunuz klasöre bir `prompt.txt` dosyası oluşturun ve ChatGPT'ye göndermek istediğiniz mesajı yazın.

5. Aracı çalıştırmak için:
   ```shell
   python3 main.py
   ```

Tarayıcı ekranının açılmasını istemiyorsanız, işlemi tarayıcıyı açmadan gerçekleştirmek için `main.py` dosyasının 13. satırındaki yorumu kaldırabilirsiniz.