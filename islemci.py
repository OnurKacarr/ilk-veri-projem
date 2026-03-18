import os

print("--- Islem Baslatiliyor ---")

# Dosyanın varlığını kontrol edelim
if os.path.exists('verilerim.txt'):
    with open('verilerim.txt', 'r', encoding='utf-8') as dosya:
        icerik = dosya.read()
    
    print(f"Okunan Veri: {icerik}")

    # Veriyi dönüştürelim
    buyuk_metin = icerik.upper()
    kelime_sayisi = len(icerik.split())

    # Sonucu kaydedelim
    with open('sonuclar.txt', 'w', encoding='utf-8') as hedef:
        hedef.write(f"Kelime Sayisi: {kelime_sayisi}\n")
        hedef.write(buyuk_metin)
    
    print("--- Islem Basariyla Tamamlandi! ---")
    print("Simdi klasorundeki 'sonuclar.txt' dosyasina bakabilirsin.")
else:
    print("HATA: 'verilerim.txt' dosyasi bulunamadi! Lutfen dosyayi olusturdugundan emin ol.")