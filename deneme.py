lessons = {}
studentName = input("Adınızı giriniz : ")
lessonName = input("Ders adı giriniz : ")
firstExamp = input("Vize notunuzu giriniz : ")
endExamp = input("Final notunuzu giriniz : ")

lessons[studentName] = {
    "Ders Adı": lessonName,
    "Vize Notu": firstExamp,
    "Final Notu": endExamp
}
print(lessons)