from product import Product


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