print("--- Islem Baslatiliyor ---")

try:
    # Dosyayı hata almamak için latin-1 ve errors ignore ile açıyoruz
    with open("verilerim.txt", "r", encoding="utf-8", errors="ignore") as dosya:
        icerik = dosya.read()
    
    # Veriyi büyük harfe çevir
    sonuc = icerik.upper()
    
    # Sonucu kaydet
    with open("sonuclar.txt", "w", encoding="utf-8") as dosya:
        dosya.write(sonuc)
    
    print("✅ Veri işleme başarıyla tamamlandı.")
    print("✅ Sonuçlar sonuclar.txt dosyasına kaydedildi.")

except Exception as e:
    print(f"❌ Bir hata oluştu: {e}")