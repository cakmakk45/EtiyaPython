"""vize = input("Vize notunuzu giriniz :")
final = input("Final notunuzu giriniz :")
ort = (vize)*0.4 + (final)*0.6
print(float(ort))

if ort<=49:
    print(f"Ders notunuz {ort} FF ile kaldınız")
elif ort>= 50 and ort<=60:
    print(f"Ders notunuz {ort} DD ile sınırda geçtiniz" )
elif ort>= 60 and ort<=70:
    print(f"Ders notunuz {ort} CC ile geçtiniz")
elif ort>= 70 and ort<=80:
    print(f"Ders notunuz {ort} BB ile geçtiniz")
elif ort>= 80 and ort<=100:
    print(f"Ders notunuz {ort} AA Başarılı geçtiniz")
else:
    print("Geçersiz değer girdiniz.")
    """

#! 1. kullanıcı gireceği ders sayısını belirtecek
lessonCount = int(input("Kaç adet ders notu gireceksiniz :"))

#! 2. girilen ders sayısı kadar 2 adet soru sorulacak.
#! (1. ders için vize notu giriniz. 1. ders için final notu giriniz)
#! girilen notlar ondalıklı olabilir
lessons = {}
passedLessons = []
failedLessons = []
for i in range(lessonCount):
    lessonName = str(input(f"{i+1}. ders adını giriniz : "))
    firstNote = float(input(f"{i+1}. ders için vize notunuzu giriniz."))
    endNote = float(input(f"{i+1}. ders için final notunuzu giriniz."))
    totalExampNote = firstNote*0.4 + endNote*0.6
    lessons = {
        
    "Ders Adı": lessonName,
    "Vize Notu": firstNote,
    "Final Notu": endNote,
    "ortalama": totalExampNote
}
    print(lessons)
    
    if lessons["ortalama"] >= 50:
        passedLessons.append(lessons["Ders Adı"])
    else:
        failedLessons.append(lessons["Ders Adı"])
   
print("*********************************************") 
    
print(f"{len(passedLessons)} dersten geçtiniz {len(failedLessons)} dersten kaldınız")
print("*********************************************")
print(f"Geçtiğiniz dersler listesi : {passedLessons}")
print(f"kaldığınız dersler listesi : {failedLessons}")

    


    
    
    
  
  
  
    #firstNote = float(input(f"{i+1}. dersi için vize notunuzu giriniz :"))
    #lessonExamp2 = float(input(f"{i+1}. dersi için final notunuzu giriniz :"))
    #totalExampNote = lessonExamp1*0.4 + lessonExamp2*0.6
    #if totalExampNote >= 50:
        #passedExamps += 1
    #else:
     #   failedExamps += 1
#print(f"{passedExamps} dersten geçtiniz {failedExamps} dersten kaldınız")***






