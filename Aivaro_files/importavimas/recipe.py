from product import Product

class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product: Product):
        ingredient_id, existing_product = self.check_ingredient(product.name)
        if existing_product is not None:
            existing_product.quantity += product.quantity
            print(f"{existing_product.name} was already in the recipe, and we added {product.quantity} more. ")
        else:
            self.ingredients.append(Product(product.name, product.quantity, product.unit_of_measurement))
            print(f"{product.name} {product.quantity} {product.unit_of_measurement} was added to the recipe. ")

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
                print(f"{name} x {ingredient} was removed from recipe. ")
                if ingredient.quantity == 0:
                    self.ingredients.remove(ingredient)
                    print(f"All the {ingredient} was removed. ")
            else:
                print(f"Not enough {name} in the recipe. ")
        else:
            print(f"Ingredient {name} does not exist in the recipe.")

    def print_recipe(self):
        for index, ingredient in enumerate(self.ingredients, start=1):
            print(f"{index}. {ingredient} {ingredient.unit_of_measurement}")

    def change_ingredient_quantity(self, name:str, quantity:float):
        product_id, ingredient = self.check_ingredient(name)
        if ingredient is not None:
            ingredient.name = name
            ingredient.quantity = quantity
            print(f"{name} x {quantity} {ingredient.unit_of_measurement} was added to recipe")
        else:
            print("Product does not exist in recipe")
        