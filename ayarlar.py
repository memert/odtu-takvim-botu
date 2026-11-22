"""
Takvim botu ayarları — dönem değişince SADECE bu dosyayı düzenlemen yeterli.
"""

# ODTÜClass adresi her dönem değişir (ör. 2027 bahar için muhtemelen odtuclass2027s)
ODTUCLASS_URL = "https://odtuclass2026f.metu.edu.tr"

# Haftalık ders programı — gece özetinde "yarınki dersler" için.
# Gün numarası: 0=Pazartesi 1=Salı 2=Çarşamba 3=Perşembe 4=Cuma 5=Cumartesi 6=Pazar
# (başlangıç, bitiş, ders, yer)
DERS_PROGRAMI = {
    0: [("09:40", "11:30", "METE 451", "MT-B308")],
    1: [("09:40", "13:30", "METE 401", "MT-E04")],
    2: [("09:40", "12:30", "METE 453", "MT-E110"),
        ("09:40", "12:30", "MSE 475", "G111"),
        ("12:40", "13:30", "METE 451", "MT-B108"),
        ("13:40", "15:30", "METE 388", "MT-C AUD")],
    3: [("13:40", "15:30", "METE 421", "MT-E308")],
    4: [("09:40", "12:30", "METE 470", "MT-E04")],
}

# Gece özeti bu saatte gönderilir (bot saat başını ~7 geçe çalışır, GitHub birkaç dk geciktirebilir)
GECE_OZETI_SAATI = 23
# Sessiz saatler: bu aralıkta mail/dosya/not/sınav bildirimi gönderilmez, sabah toplu gelir.
SESSIZ_BASLANGIC = 23
SESSIZ_BITIS = 8
# Gece özetindeki "önümüzdeki günler" penceresi
OZET_GUN_SAYISI = 7

# Ödevler "Sınavlar" takvimine bu renkte eklenir (Google Takvim renk numarası, 1-11).
# 5 = sarı, 6 = turuncu, 10 = yeşil, 11 = kırmızı
ODEV_RENGI = "5"

# Gemini modelleri: biri yoğunsa/yoksa sıradakine geçilir.
GEMINI_MODELLERI = ["gemini-flash-latest", "gemini-2.5-flash", "gemini-flash-lite-latest"]
