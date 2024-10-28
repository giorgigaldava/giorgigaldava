class Students:
    def __init__(self, name1, house1):
        if not name1:
            raise ValueError ("invalid name")
        self.n = name1
        self.h = house1
    
    def __str__(self):
        return(f"{self.n} from {self.h}")
    
    @classmethod
    def get(cls):
        nam = input("name tne student: ")
        hou = input("name the house: ")
        return cls(nam, hou)
    
    # getter
    @property
    def h(self):
        return (self._house)
    
    # setter
    @h.setter
    def h(self, house):
        if house not in (["gryfindor", "Hufflepuff", "Ravenclaw", "Slytherin"]):
            raise ValueError ("invalid house")
        self._house = house

def main():
    student = Students.get()
    print(student)



main()