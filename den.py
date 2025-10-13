 # Hesap Makinesi 

sayi1=float(input("Lütfen sayı Giriniz :"))
sayi2=float(input("Lütfen 2.sayıyı giriniz:"))

islem=(input("Hangi işlemi yapmak İstiyorsunuz ? (*,/,-,+):"))



if islem=="*":
    print(f"Çarpma İşleminizin Sonucu : {sayi1*sayi2}")
elif islem=="/":
    print(f"Çarpma İşleminizin Sonucu : {sayi1/sayi2}")
elif islem=="-":
    print(f"Çarpma İşleminizin Sonucu : {sayi1-sayi2}")
elif islem=="+":
    print(f"Çarpma İşleminizin Sonucu :{sayi1+sayi2}")
else:
    print(f"{islem} bu ifade bir işlem değildir lütfen (*,/,-,+) işlemlerinden birini giriniz.")















