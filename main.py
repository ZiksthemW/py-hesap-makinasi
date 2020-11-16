islem = input("""
İslem seçiniz;

Toplama - 1
Çıkarma - 2
Bölme   - 3
Üs alma - 4

İşlem: """)

if islem == "1":
    sayi1 = int(input("1. Sayıyı giriniz."))
    sayi2 = int(input("2. Sayıyı giriniz."))
    sonuc = print("Sonuç: ", sayi1 + sayi2)
    
elif islem == "2":
    sayi1 = int(input("1. Sayıyı giriniz."))
    sayi2 = int(input("2. Sayıyı giriniz."))
    sonuc = print("Sonuç: ", sayi1 - sayi2)
    
elif islem == "3":
    sayi1 = int(input("1. Sayıyı giriniz."))
    sayi2 = int(input("2. Sayıyı giriniz."))
    sonuc = print("Sonuç: ", sayi1 / sayi2)
    
else:
    print("Bir şeyler hatalı gitti!")
