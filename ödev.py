#Vücut kitle indeksi hesaplama 
 
kilo=float(input("Lütfen kilonuzu kg cinsinden giriniz: "))

boy=float(input("Lütfen boyunuzu metre cinsinden giriniz: "))

vücut_kitle_indeksi=kilo/boy**2
print(f"vücut kitle indeksiniz: {round(vücut_kitle_indeksi,3)} olarak hesaplanmıştır")

if vücut_kitle_indeksi <18.5:
    print("Zayıfsınız,kilo almanız gerekiyor.")
elif 18.5<vücut_kitle_indeksi <24.9 :
    print("Kilonuz normal.")
elif 25<vücut_kitle_indeksi<29.9 : 
    print("Kilonuz fazla,kilo vermelisiniz.")
elif 30.0<vücut_kitle_indeksi<34.9 :
    print=("1.derece obezsiniz.")
elif 35<vücut_kitle_indeksi<39.9 :
    print("2.derece obezsiniz.")
elif 40.0<vücut_kitle_indeksi :
     print("3.derece obezsiniz , acilen kilo veriniz.")

   