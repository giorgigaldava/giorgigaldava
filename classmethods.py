import random
class Hat():
    houses = ["Grifindor", "Slizerin", "Huflepuf", "Ravenclaw"]
    
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        return f"{name} from {house}"

result = Hat.sort("Harry")

print(result)
