print("Merhaba Etiya Ailesi")
# string = metinsel ifade
text = "Metin 2"
print(text)
# integer
number = 5
print(type(number))

# double, float, decimal = ondalıklı sayı
dnumber = 5.3
print(dnumber)

# matematiksel operatörler
print(number + 5) 
print(number - 5)
print(number * 5)
print(number / 5)
print(number % 5)

#boolean, bool = true and false
isVerified = True

#mantıksal,karşılaştırma operatörler => her mantıksal operatör boolean değer döner
print(1 == 2)
print(1 != 3)
print(3 > 2)
print(2 > 2)
print( 2 >= 2)
print(10%2==0)

print(50/2 == 25)
print(50/2 == 25.0)

#string operasyonları 
text = "Merhaba Etiya"
print(text.upper())
print(text.lower())
print(text.startswith("Mer"))
print(text.endswith("etiya"))

name = "Kadriye"
age = 25
company = "etiya"

print(name+ " " + str(age) +" "+ "Yaşında " + company + "'de çalışıyor")
print(f"{name} {age} yaşında {company} 'de çalışıyor")
