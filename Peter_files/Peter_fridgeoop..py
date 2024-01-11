class Product:
    def __init__(self, name:str, quantity:float, unit_of_measurement:str = 'unit', **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = unit_of_measurement
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product: Product):
        ingredient_id, existing_product = self.check_ingredient(product.name)
        if existing_product is not None:
            existing_product.quantity += product.quantity
            print(f"Produktas {existing_product.name} jau yra recepte, todėl reikalingas kiekis padidintas {product.quantity}.")
        else:
            self.ingredients.append(Product(product.name, product.quantity, product.unit_of_measurement))
            print(f"{product.name} {product.quantity} {product.unit_of_measurement} buvo pridėtas į receptą.")

    def change_ingredient_quantity(self, name:str, quantity:float):
        product_id, ingredient = self.check_ingredient(name)
        if ingredient is not None:
            ingredient.name = name
            ingredient.quantity = quantity
            print(f"Produkto {name} kiekis: {quantity} {ingredient.unit_of_measurement} buvo pridėtas į receptą.")
        else:
            print("Recepte tokio produkto nėra.")

    def check_ingredient(self, ingredient_name:str) -> (int, Product):
        for ingredient_id, ingredient in enumerate(self.ingredients):
            if ingredient_name.lower() == ingredient.name.lower():
                return ingredient_id, ingredient
        return None, None
    
    def remove_ingredient(self, name:str, quantity:float):
        self.print_recipe()
        ingredient_id, ingredient = self.check_ingredient(name)
        if ingredient is not None:
            if ingredient.quantity >= quantity:
                ingredient.quantity -= quantity
                print(f"{quantity} produkto {ingredient} buvo ištrinti iš recepto.")
                if ingredient.quantity == 0:
                    self.ingredients.remove(ingredient)
                    print(f"Visas {ingredient} buvo pašalintas iš recepto.")
            else:
                print(f"Nurodytas {name} kiekis kurį norite pašalinti iš recepto per didelis.")
        else:
            print(f"Produkto {name} recepte nėra.")

    def print_recipe(self):
        print("Receptui reikia: ")
        for index, ingredient in enumerate(self.ingredients, start=1):
            print(f"{index}, {ingredient} {ingredient.unit_of_measurement}")


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name.lower() == product_name.lower():
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float, unit_of_measurement:str):
        product_id, product = self.check_product(name) 
        if product is not None:
            product.quantity += quantity
            print(f"{name} jau buvo šaldytuve, {quantity} {unit_of_measurement} buvo pridėtas prie jau esamo.")
        else:
            self.contents.append(Product(name, quantity, unit_of_measurement))
            print(f"Produkto {name} kiekis {quantity} {unit_of_measurement} buvo pridėtas į šaldytuvą.")

    def remove_product(self, name:str, quantity:float):
        self.print_contents()
        product_id, product = self.check_product(name)
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"Produkto {product} kiekis {quantity}  buvo pašalintas iš šaldytuvo.")
                if product.quantity == 0:
                    self.contents.remove(product)
                    print(f"Produkto {product} šaldytuve neliko.")
            else:
                print(f"Produkto {name} šaldytuve yra per mažai.")
        else:
            print(f"Produkto {name} šaldytuve nėra.")

    def print_contents(self):
            print('Šaldytuve esantys produktai:')
            for index, product in enumerate(self.contents, start=1):
                print(f'{index}. {product} {product.unit_of_measurement}')

    def check_recipe(self, recipe: Recipe):
            for ingredient in recipe.ingredients:
                index, fridge_product = self.check_product(ingredient.name)
                if fridge_product is None:
                    print(f"Produkto {ingredient.name} šaldytuve nėra.")
                    print("Recepto pagaminti negalima.")
                    return False
                quantity_difference = self.check_product_quantity(fridge_product, ingredient.quantity)
                if quantity_difference < 0:
                    print(f"Trūksta {abs(quantity_difference)} produkto {fridge_product.name} pagaminti receptui.")
                    print("Recepto pagaminti negalima.")
                    return False
            print("Galite gaminti pagal pateiktą receptą!")
            return True


def main():
    fridge = Fridge()
    recipe = Recipe()

    while True:
            print('''
        ----Pasirinkite ką norite daryti šaldytuve----
        0 = Išeiti.
        1 = Įdėti produktą į šaldytuvą.
        2 = Išimti produktus iš šaldytuvo.
        3 = Patikrinti ar konkretus produktas yra šaldytuve
        4 = Atspausdinti šaldytuve esančių produktų sąrašą
        5 = Pridėti produktą į receptą
        6 = Išimti produktą iš recepto
        7 = Pakeisti produkto kiekį recepte
        8 = Atspausdinti receptą           
        9 = Patikrinti ar galima pagaminti pagal receptą.
         
        ''')
            choice = input("Jūsų pasirinkimas: ")

            if choice == "0":
                break
            elif choice == "1":
                input_name = input("Įveskite produktą: ")
                input_quantity = float(input("Įveskite produkto kiekį: "))
                input_unit_of_measurement = input("Įveskite matavimo vienetą: ")
                fridge.add_product(input_name, input_quantity, input_unit_of_measurement)
            elif choice == "2":
                input_name = input("Įveskite produkto pavadinimą, kurį norite išimti: ")
                input_quantity = float(input("Įveskite kiekį, kurį norite išimti: "))
                fridge.remove_product(input_name, input_quantity)
            elif choice == "3":
                input_name = input("Įveskite produkto pavadinimą: ")
                index, product = fridge.check_product(input_name)
                if index == None:
                    print(f"Produkto {input_name} šaldytuve nėra.")
                else:
                    print(f"{product} numeris šaldytuve:{index+1}.")
            elif choice == "4":
                    fridge.print_contents()
            elif choice =='5':
                input_recipe_name = input("Įveskite produktą, kuri norite pridėti į receptą: ")
                input_recipe_quantity = float(input("Įveskite produkto kiekį: "))
                input_unit_of_measurement = input("Įveskite matavimo vienetą: ")
                input_product = Product(input_recipe_name, input_recipe_quantity, input_unit_of_measurement)
                recipe.add_ingredient(input_product)
            elif choice =='6':
                input_ingridient_name = input("Input product name: ")
                input_ingridient_quantity = float(input("Input product quantity: "))
                recipe.remove_ingredient(input_ingridient_name, input_ingridient_quantity)
            elif choice =='7':
                input_ingridient_name = input("Input existing product name: ")
                input_ingridient_quantity = float(input("Input new product quantity: "))
                recipe.change_ingredient_quantity(input_ingridient_name, input_ingridient_quantity)
            elif choice =='8':
                recipe.print_recipe()
            elif choice =='9':    
                fridge.check_recipe(recipe)
            else:
                print("Neteisingas pasirinkimas, Bandykite iš naujo!")

fridge = Fridge()
fridge.add_product("Kiaušiniai", 3, "vnt")
recipe = Recipe()
recipe.add_ingredient(Product("Sviestas", 200, "g"))


if __name__ == "__main__":
    main()
   