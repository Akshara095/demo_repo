from datetime import datetime
class Person:
    def _init_(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth
    def calculate_age(self):
        today = datetime.today()
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
person1 = Person("John Doe", "USA", datetime(1990, 5, 15))
age = person1.calculate_age()
print(f"{person1.name} is {age} years old.")
