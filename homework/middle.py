# # TASK 01
# class School:
#     students = []
    
#     def __init__(self, name: str) -> None:
#         self.name = name
        
#     def add_student(self, student: str) -> None:
#         self.students.append(student)
        
#     def delete_student(self, student: str) -> None:
#         self.students.remove(student)
        
# s = School("School21")
# s.add_student("Lazizbek")
# s.add_student("Diyorbek")

# s.delete_student("Lazizbek")

# print(s.students)

# # TASK 02
# class Restaurant:
#     def __init__(self, name):
#         self.name = name
    
#     def get_menu(self):
#         raise NotImplementedError("Har bir restoran o'z menyusi")
    
#     def get_price(self):
#         raise NotImplementedError("Har bir restoran o'z narxlari")

# class FastFood(Restaurant):
#     def __init__(self, name):
#         super().__init__(name)
#         self.menu = {"Burger": 5, "Fries": 3, "Cola": 2}
    
#     def get_menu(self):
#         return self.menu
    
#     def get_price(self, item):
#         return self.menu.get(item, "Bunday taom menyuda yo'q.")

# class FineDining(Restaurant):
#     def __init__(self, name):
#         super().__init__(name)
#         self.menu = {"Steak": 25, "Lobster": 40, "Wine": 30}
    
#     def get_menu(self):
#         return self.menu
    
#     def get_price(self, item):
#         return self.menu.get(item, "Bunday taom menyuda yo'q.")

# fast_food = FastFood("QuickBite")
# fine_dining = FineDining("Elite Dine")

# print(f"{fast_food.name} menyusi: {fast_food.get_menu()}")
# print(f"Burger narxi: ${fast_food.get_price('Burger')}")

# print(f"{fine_dining.name} menyusi: {fine_dining.get_menu()}")
# print(f"Steak narxi: ${fine_dining.get_price('Steak')}")
    
# # TASK 03
# class Student:
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
    
#     def get_average(self):
#         return sum(self.grades) / len(self.grades) if self.grades else 0
    
#     def is_passing(self):
#         return self.get_average() > 60

# # Talaba uchun misol
# student = Student("Ali", 20, [70, 80, 90])
# print(f"{student.name} ning o'rtacha bahosi: {student.get_average()}")
# print(f"{student.name} o'tish natijasi: {student.is_passing()}")

# # TASK 04
# class Talaba:
#     def __init__(self, ism, kurs, ortacha_baho, stipendiya):
#         self.ism = ism
#         self.kurs = kurs
#         self.ortacha_baho = ortacha_baho
#         self.stipendiya = stipendiya
    
#     def __str__(self):
#         return f"Ism: {self.ism}, Kurs: {self.kurs}, ortaca baho: {self.ortacha_baho}, Stipendiya: {self.stipendiya} som"

# talabalar = [
#     Talaba("Ali", 2, 85, 1200000),
#     Talaba("Vali", 1, 78, 900000),
#     Talaba("Dior", 3, 92, 1500000),
#     Talaba("Alex", 4, 70, 800000),
#     Talaba("Bob", 2, 88, 1300000)
# ]

# mos_talabalar = [talaba for talaba in talabalar if talaba.ortacha_baho > 80 and talaba.stipendiya > 1000000]

# print("ortaca bahosi 80 dan yuqori va stipendiyasi 1 mln somdan katta bolgan talabala:")
# for talaba in mos_talabalar:
#     print(talaba)

# # TASK 05
# class ShoppingCart:
#     def __init__(self):
#         self.items = {}
    
#     def add_item(self, name, price):
#         if name in self.items:
#             self.items[name]['quantity'] += 1
#         else:
#             self.items[name] = {'price': price, 'quantity': 1}
    
#     def remove_item(self, name):
#         if name in self.items:
#             if self.items[name]['quantity'] > 1:
#                 self.items[name]['quantity'] -= 1
#             else:
#                 del self.items[name]
    
#     def get_total(self):
#         return sum(item['price'] * item['quantity'] for item in self.items.values())
    
#     def show_cart(self):
#         return self.items

# # Sinov
# cart = ShoppingCart()
# cart.add_item("Olma", 2)
# cart.add_item("Banan", 1)
# cart.add_item("Olma", 2)
# print(cart.get_total())
# cart.remove_item("Olma")
# print(cart.get_total())

