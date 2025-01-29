# # TASK 01
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.borrower = None
#         self.due_date = None

#     def borrow(self, name, date):
#         if self.borrower:
#             print(f"Kitob allaqachon {self.borrower} tomonidan qarzga olingan.")
#         else:
#             self.borrower = name
#             self.due_date = datetime.strptime(date, "%Y-%m-%d")
#             print(f"Kitob {self.borrower} tomonidan qarzga olingan. Qaytarish muddati: {self.due_date.strftime('%Y-%m-%d')}.")

#     def return_book(self):
#         if self.borrower is None:
#             print("Kitob hali qarzga olinmagan.")
#         else:
#             today = datetime.today()
#             if today > self.due_date:
#                 print(f"Jazo qo‘llaniladi! Kitob {self.borrower} tomonidan kechiktirilgan.")
#             else:
#                 print(f"Kitob {self.borrower} tomonidan muvaffaqiyatli qaytarildi.")
#             self.borrower = None
#             self.due_date = None

# book = Book("Python dasturlash", "John Doe")
# book.borrow("Ali", "2025-02-01")
# book.return_book()