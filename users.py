class Talaba:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.grades = []
        
    def addGrades (self, grades):
        if 0 <= grades <= 100:
            self.grades.append(grades)
        else:
            print("Siz notogri baho kiritingiz!")
            return
            
    def averageGrade (self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        
talaba_mal = [
    {"name": "Ali", "course": 1, "grades": [85, 90]},
    {"name": "Laylo", "course": 2, "grades": [78, 88]},
    {"name": "Zafar", "course": 3, "grades": [92, 85]}
]

talabalar = []

for malumot in talaba_mal:
    talaba = Talaba(malumot["name"], malumot["course"])
    for grade in malumot["grades"]:
        talaba.addGrades(grade)
    talabalar.append(talaba)
    
for talaba in talabalar:
    average_grades = talaba.averageGrade()
    print(f"{talaba.name} ({talaba.course}-kurs): o'rtacha baho {average_grades:.2f}")