""" Komandinio darbo / savarankiška užduotis
===[ Biudžetas ]===

Reikalavimai

* Biudžeto turinys - pajamų/išlaidų žurnalo žodynas
** raktas - paskirtis
** reikšmė - pajamos pozityvus float, išlaidos negatyvus float
* Galimybė pridėti pajamas arba išlaidas
* Spausdinti pajamų/išlaidų žurnalą
* Suskaičiuoti biudžeto balansą

"""

class Budget:
    def __init__(self):
        self.budget_journal = {}

    def add_transaction(self, purpose, amount):
        if purpose not in self.budget_journal:
            self.budget_journal[purpose] = 0
        self.budget_journal[purpose] += amount

    def print_journal(self):
        print("===[ Biudžeto žurnalas ]===")
        for purpose, amount in self.budget_journal.items():
            print(f"{purpose}: {amount}")

    def calculate_balance(self):
        total_income = sum(amount for purpose, amount in self.budget_journal.items() if amount > 0)
        total_expenses = sum(amount for purpose, amount in self.budget_journal.items() if amount < 0)
        balance = total_income + total_expenses
        return balance


def main(): 
    budget = Budget()
    
    while True:
        print('''===[ Biudžetas ]===''' )
        print('''
          ---- Biudžeto valdymas ----
          1: Pridėti pajamas
          2: Pridėti išlaidas
          3: Atimti pajamas
          4: Atimti išlaidas
          5: Spausdinti biudžeto žurnalą
          6: Skaičiuoti biudžeto balansą
          0: Išeiti
          ''')
        choice = input("Pasirinkimas: ")
        
        if choice == '0':
            break
        elif choice == '1':
            purpose = input("Pajamų paskirtis: ")
            amount = int(input("Pajamų suma: "))
            budget.add_transaction(purpose, amount)
        elif choice == '2':
            purpose = input("Išlaidų paskirtis: ")
            amount = int(input("Išlaidų suma: "))
            budget.add_transaction(purpose, -amount)   # išlaidos turėtų būti negatyvios
        elif choice == '3':
            purpose = input("Atėmimo paskirtis iš pajamų: ")
            amount = int(input("Atėmimo suma iš pajamų: "))     # atimtis
            budget.add_transaction(purpose, -amount)
        elif choice == '4':
            purpose = input("Atėmimo paskirtis iš išlaidų: ")
            amount = int(input("Atėmimo suma iš išlaidų: "))
            budget.add_transaction(purpose, amount)
        elif choice == '5':
            budget.print_journal()
        elif choice == '6':
            balance = budget.calculate_balance()
            print(f"Biudžeto balansas: {balance}")
        else:
            print("Neteisingas pasirinkimas. Bandykite dar kartą.")

if __name__ == "__main__":
    main()
