# Kullanıcıdan hangi işlemi yapmak istediğini al
islem = input("Yapmak istediğiniz işlemi girin (+, -, *, /, ?): ")

# Kullanıcıdan iki sayı al
ilksayi = float(input("İlk sayıyı giriniz: "))
ikincisayi = float(input("İkinci sayıyı giriniz: "))

# İşlemi kontrol et ve sonucu hesapla
if islem == '+':
    sonuc = ilksayi + ikincisayi
    print(f"Sonuç: {sonuc}")
elif islem == '-':
    sonuc = ilksayi - ikincisayi
    print(f"Sonuç: {sonuc}")
elif islem == '*':
    sonuc = ilksayi * ikincisayi
    print(f"Sonuç: {sonuc}")
elif islem == '/':
    if ikincisayi == 0:
        print("Sıfıra bölme hatası!")
    else:
        sonuc = ilksayi / ikincisayi
        print(f"Sonuç: {sonuc}")
else:
    print("Geçersiz işlem girdiniz.")