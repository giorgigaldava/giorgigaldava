class Wizard():
    def __init__(self, name):
        if not name:
            raise ValueError("Invalid name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Snape")
student = Student("Harry", "Gryfindor")
professor = Professor("Snape", "Defence against dark side")

print(student)



