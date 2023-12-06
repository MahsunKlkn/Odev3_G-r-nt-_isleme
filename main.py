"""
import cv2
import numpy as np

# Kamera bağlantısını başlat
kamera = cv2.VideoCapture(0)

while True:
    # Kameradan bir kareyi oku
    ret, kare = kamera.read()

    # Orijinal görüntüyü göster
    cv2.imshow("Orijinal Görüntü", kare)

    # Görüntüyü HSV renk uzayına çevir
    hsv_kare = cv2.cvtColor(kare, cv2.COLOR_BGR2HSV)

    # Kırmızı renk sınırlarını belirle (HSV formatında)
    alt_kirmizi = np.array([0, 100, 100])
    ust_kirmizi = np.array([10, 255, 255])

    # Belirtilen sınırlar içindeki renkleri bul ve maskeyi uygula
    kirmizi_maske = cv2.inRange(hsv_kare, alt_kirmizi, ust_kirmizi)

    # Kırmızı renklere ait olan bölgeyi göster
    kirmizi_sonuc = cv2.bitwise_and(kare, kare, mask=kirmizi_maske)
    cv2.imshow("Sadece Kirmizi Renk", kirmizi_sonuc)

    # Eğer 'q' tuşuna basılırsa döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını serbest bırak
kamera.release()
cv2.destroyAllWindows()

"""





"""
import cv2
import numpy as np

# Görüntüyü yükle
image_path = "Pirinc1.jpeg"  # Görüntü dosyasının yolunu doğru şekilde güncelleyin
img = cv2.imread(image_path)

# Yeni genişlik ve yükseklik değerlerini belirle
new_width = 600
new_height = 800

# Görüntüyü yeniden boyutlandır
resized_img = cv2.resize(img, (new_width, new_height))

# Gri seviyeye dönüştür
gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

# Eşikleme yap
_, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler uygula (istenmeyen arka planları temizle)
kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Nesne etiketleme ve sayma
_, labels, stats, centroids = cv2.connectedComponentsWithStats(opening)

# Pirinç tanelerini say
num_rice = len(stats) - 1  # İlk etiket, arka planı temsil eder, bu nedenle çıkarılır

# Sonuçları ekrana yazdır
print(f"Pirinç taneleri sayısı: {num_rice}")

# Görüntüyü göster
cv2.imshow("Original Image", resized_img)
cv2.imshow("Processed Image", opening)
cv2.waitKey(0)
cv2.destroyAllWindows()


"""
import cv2
import numpy as np

# Görüntüyü yükle
dosya_yolu = "Pirinc.jpeg"  # Görüntü dosyasının yolunu doğru şekilde güncelleyin
görüntü = cv2.imread(dosya_yolu)

# Yeni genişlik ve yükseklik değerlerini belirle
yeni_genislik = 450
yeni_yukseklik = 600

# Görüntüyü yeniden boyutlandır
yeniden_boyutlandirilmis_goruntu = cv2.resize(görüntü, (yeni_genislik, yeni_yukseklik))

# Gri tonlamaya dönüştür
gri_goruntu = cv2.cvtColor(yeniden_boyutlandirilmis_goruntu, cv2.COLOR_BGR2GRAY)

# Eşikleme yap
_, esik_goruntu = cv2.threshold(gri_goruntu, 100, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler uygula (istenmeyen arka planları temizle)
kernel = np.ones((5, 5), np.uint8)
acma_goruntu = cv2.morphologyEx(esik_goruntu, cv2.MORPH_OPEN, kernel, iterations=2)

# Nesne etiketleme ve sayma
_, etiketler, istatistikler, merkezler = cv2.connectedComponentsWithStats(acma_goruntu)

# Pirinç tanelerini say
pirinc_sayisi = len(istatistikler) - 1  # İlk etiket, arka planı temsil eder, bu nedenle çıkarılır

# Sonuçları ekrana yazdır
print(f"Pirinç taneleri sayısı: {pirinc_sayisi}")

# Görüntüyü göster
cv2.imshow("Orijinal Görüntü", yeniden_boyutlandirilmis_goruntu)
cv2.imshow("İşlenmiş Görüntü", acma_goruntu)
cv2.waitKey(0)
cv2.destroyAllWindows()

























