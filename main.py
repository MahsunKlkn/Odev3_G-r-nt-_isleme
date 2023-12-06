import cv2
import numpy as np

# MAHSUN KALKAN
# Sayma İslemi İçin 2 gÖRÜNTÜ Bıraktım İkisinide Deneyebilirsiniz.

dosya_yolu = "Pirinc.jpeg"  # Görüntüyü yükleyip görüntü dosyasının yolunu doğru bir şekilde girdim.
görüntü = cv2.imread(dosya_yolu)


yeni_genislik = 450     # Yeni genişlik ve yükseklik değerleri girdim çünkü yüklediğim fotoğrafın boyutu sıkıntı yaratıyordu.
yeni_yukseklik = 600

# Görüntüyü yeniden boyutlandır
yeniden_boyutlandirilmis_goruntu = cv2.resize(görüntü, (yeni_genislik, yeni_yukseklik))


gri_goruntu = cv2.cvtColor(yeniden_boyutlandirilmis_goruntu, cv2.COLOR_BGR2GRAY)  # Görüntümüzü öncelikle gri tona dönüştürdüm.

# Eşikleme yap
_, esik_goruntu = cv2.threshold(gri_goruntu, 100, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler uyguladım (istenmeyen arka planları temizledim)
kernel = np.ones((5, 5), np.uint8)
acma_goruntu = cv2.morphologyEx(esik_goruntu, cv2.MORPH_OPEN, kernel, iterations=2)


_, etiketler, istatistikler, merkezler = cv2.connectedComponentsWithStats(acma_goruntu)  # Nesne etiketleme ve sayma

# Pirinç tanelerini saymaya başlayalım
pirinc_sayisi = len(istatistikler) - 1  # İlk etiket, arka planı temsil eder, bu nedenle çıkarılır

# Sonuçları ekrana yazdırıyoruz
print(f"Pirinç taneleri sayısı: {pirinc_sayisi}")

# Görüntüyü gösteriyoruz
cv2.imshow("Yuklenen Goruntu", yeniden_boyutlandirilmis_goruntu)
cv2.imshow("Islenmis Goruntu", acma_goruntu)
cv2.waitKey(0)
cv2.destroyAllWindows()

























