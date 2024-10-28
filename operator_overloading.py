class BankAccount:
    def __init__ (self, lari, tetri):
        self.l = lari
        self.t = tetri

    def __str__ (self):
        return f"this bank account is {self.l} lari and {self.t} tetri"

    def __add__ (self, other):
        lari = giorgi.l + nino.l
        tetri = giorgi.t + nino.t
        return  BankAccount(lari , tetri)
    

giorgi = BankAccount(1000, 50)
nino = BankAccount(1233 , 10)
print(giorgi + nino)

