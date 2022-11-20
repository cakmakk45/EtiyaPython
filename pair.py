#! Şirket çalışanları verilerini tutan dosya oluşturulacak
#! Kullanıcıdan çalışan sayısı alınacak 
#! Çalışan sayısı kadar isim,soyisim,maaş bilgisi alınacak
#! Dosyadaki her satıra "Ad Soyad - Maaş" kalıbında çalışan bilgileri eklenecek.
#! Programın sonunda bu dosyadan bilgileri satır satır okuyup listeleyecek kod yazılacak. 
#! Eklenen çalışanlar mevcut çalışanları silmeyecek, üzerine yazılacak
#! Hata yakalama işlemlerini unutmayalım

try:
    employeeCount = int(input("Kaç adet çalışan gireceksiniz :"))
except ValueError:
    print("İstenilen değeri girmediniz.")
finally:
    print("okey")


employees = {}

for i in range(employeeCount):

    employeeName = (input(f"{i+1}, çalışan adını giriniz : "))
    employeeSurname = (input(f"{i+1}, çalışan soyadını giriniz : "))
    employeePay = int(input(f"{i+1}, çalışan maaşını giriniz : "))
    
    file = open("employees.txt", "a+")
    file.write(f"employeeName : {employeeName} employeeSurname : {employeeSurname} - employeePay {employeePay} \n")
file.seek(0)
print(file.read())
file.close()

    #employees ={

    #"Çalışan Adı": employeeName,
    #"Çalışan Soyadı": employeeSurname,
    #"Çalışan Maaşı": employeePay
    #}

    #print(employees)


    