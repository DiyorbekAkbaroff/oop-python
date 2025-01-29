# # TASK 01
# class Student:
#     def __init__(self,name,surname,course,grades):
#         self.name=name
#         self.surname=surname
#         self.course=course
#         self.grades=grades
# students=[
#     Student("Dior","Akbarov",course=1,grades=3),
#     Student("Akbarov","Dior",course=2,grades=4)
# ]
# print(students[0].name,students[0].surname)
# print(students[1].name,students[1].surname)

# # TASK 02
# class Employe:
#     def __init__(self,name,coast):
#         self.name=name
#         self.coast=coast
# empl=[
#     Employe("Dior",coast=400),
#     Employe("Akbarov",coast=600),
# ]
# print(f"{empl[0].name}ni oylik maoshi {empl[0].coast}")
# print(f"{empl[0].name}ni yillik maoshi {empl[0].coast*12}")

# print(f"{empl[1].name}ni oylik maoshi {empl[1].coast}")
# print(f"{empl[1].name}ni yillik maoshi {empl[1].coast*12}")

# # TASK 03
# class Movie:
#     def __init__(self,title,duration,rating):
#         self.title = title
#         self.duration = duration
#         self.rating = rating

#     def increase_duration(self, minutes):
#         self.duration += minutes
#         if self.duration > 150:
#             self.decrease_rating()

#     def decrease_rating(self):
#         self.rating -= 0.5

# film = Movie("Example Movie", 140, 8.0)
# print(f"Eski davomiyligi: {film.duration}, Eski ratingi: {film.rating}")
# film.increase_duration(20)
# print(f"Yangi davomiyligi: {film.duration}, Yangi ratingi: {film.rating}")

# # TASK 04
# class Telefon:
#     def __init__(self,name,ram,coast,company):
#         self.name = name
#         self.ram = ram
#         self.coast = coast
#         self.company = company

#     def kiritiw(self):
#         self.name = input("Telefon ismi: ")
#         self.ram = int(input("Telefon RAM hajmi: "))
#         self.coast = float(input("Telefon narxi: "))
#         self.company = input("Ishlab chiqaruvchi: ")

#     def chiqarish(self):
#         print(f"Telefon ismi: {self.name}")
#         print(f"Telefon RAM hajmi: {self.ram} GB")
#         print(f"Telefon narxi: {self.coast}")
#         print(f"Ishlab chiqaruvchi kompaniya: {self.company}")

# telefon1 = Telefon("NOKIA", 4, 500, "Noki")
# telefon2 = Telefon("Galaxy", 6, 700, "Galaxy")
# telefon3 = Telefon("Samsung", 2, 300, "Huawei")
# telefon4 = Telefon("IphoneX", 8, 900, "company4")

# telefonlar = [telefon1, telefon2, telefon3, telefon4]
# for telefon in telefonlar:
#     if 2 < telefon.ram < 8:
#         telefon.chiqarish()
#         print()

# # TASK 05
# class Dokon:
#     def __init__(self,nomi,joylashuvi,turi,vaqti):
#         self.nomi = nomi
#         self.joylashuvi = joylashuvi
#         self.turi = turi
#         self.vaqti = vaqti

#     def malumot_kiritiw(self, nomi, joylashuvi, turi, vaqti):
#         self.nomi = nomi
#         self.joylashuvi = joylashuvi
#         self.turi = turi
#         self.vaqti = vaqti

#     def ciqariw(self):
#         return f"Do'kon nomi: {self.nomi}, Joylashuvi: {self.joylashuvi}, Mahsulot turi: {self.turi}, Ish vaqti: {self.vaqti}"

# dok1 = Dokon("Iwash", "Sirdaryo", "Tour", "08:00-23:00")
# dok2 = Dokon("ElectoWorld", "Xorazm", "Electronika", "08:00-20:00")
# dok3 = Dokon("GDJ_Store", "Kattakurgan", "Elektronika", "12:00-21:00")
# dok4 = Dokon("Sung_sam", "Guliston", "phones", "05:00-21:00")
# dok5 = Dokon("MarElct", "Namangan", "Elektronika", "01:00-19:00")

# elektr_mar = [dok2, dok3, dok4, dok5]

# for dokon in elektr_mar:
#     print(dokon.ciqariw())

# # TASK 06
# class Avtomobil:
#     def __init__(self, marka, model, yil, narx):
#         self.marka = marka
#         self.model = model
#         self.yil = yil
#         self.narx = narx

#     def kiritish(self):
#         self.marka = input("Avtomobil markasini kiriting: ")
#         self.model = input("Avtomobil modelini kiriting: ")
#         self.yil = int(input("Ishlab chiqarilgan yilini kiriting: "))
#         self.narx = float(input("Narxini kiriting: "))

#     def chiqarish(self):
#         print(f"Marka: {self.marka}")
#         print(f"Model: {self.model}")
#         print(f"Ishlab chiqarilgan yili: {self.yil}")
#         print(f"Narxi: {self.narx}")

# def auto_filt(automobiles):
#     for avtomobil in automobiles:
#         if avtomobil.yil > 2010:
#             avtomobil.chiqarish()

# avto1 = Avtomobil("KIA", "K5", 2024, 35000)
# avto2 = Avtomobil("Chevrolet", "Damas", 2009, 15000)
# avto3 = Avtomobil("Kitay", "Sonata", 2000, 18000)

# automobiles = [avto1, avto2, avto3]
# auto_filt(automobiles)