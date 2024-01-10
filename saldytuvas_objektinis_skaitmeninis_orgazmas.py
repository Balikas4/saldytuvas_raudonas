class Product:
    def __init__(self, name:str, quantity:float, **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = 'unit' # options: kg, g, L, ml
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"


class Recipe:
    ingredients = []
    instructions = []

    def add_ingredient(self, product:Product):
        self.ingredients.append(product)

    def change_ingredient_quantity(self, ingredient_id:int, new_quantity:float):
        self.ingredients[ingredient_id].quantity = new_quantity

#Balys new function update
    def check_ingredient(self, ingredient_name:str) -> (int, Product):
        for ingredient_id, ingredient in enumerate(self.ingredients):
            if ingredient_name == ingredient.name:
                return ingredient_id, ingredient
        return None, None

#Balys/Petras quantity/print update
    def remove_ingredient(self, name:str, quantity:float):
        self.print_recipe()
        ingredient_id, ingredient = self.check_ingredient(name)
        if ingredient is not None:
            if ingredient.quantity >= quantity:
                ingredient.quantity -= quantity
                print(f"{quantity}x{ingredient} was removed from recipe")
                if ingredient.quantity == 0:
                    self.ingredients.remove(ingredient)
                    print(f"All the {ingredient} was removed")
            else:
                print(f"Not enough {name} in the recipe.")
        else:
            print(f"Ingredient {name} does not exist in the recipe.")

    def print_recipe(self):
        for index, ingredient in enumerate(self.ingredients, start=1):
            print(f"{index}, {ingredient}")


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

#Valdemaras print update
    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) 
        if product is not None:
            product.quantity += quantity
            print(f"{name} was already in the fridge and we added {quantity} more.")
        else:
            self.contents.append(Product(name, quantity))
            print(f"{name}x {quantity} was added to the fridge.")

    def print_contents(self):
        for index, line in enumerate(self.contents, start=1):
            print(f"{index} - {line}")

#Petras quantity update
    def remove_product(self, name:str, quantity:float):
        self.print_contents()
        product_id, product = self.check_product(name)
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"{quantity}x{product} was removed from fridge")
                if product.quantity == 0:
                    self.contents.remove(product)
                    print(f"All the {product} was removed")
            else:
                print(f"Not enough {name} in the fridge.")
        else:
            print(f"Product {name} does not exist in the fridge.")

#Balys missing quantity update
    def check_recipe(self, recipe: Recipe):
            for ingredient in recipe.ingredients:
                index, fridge_product = self.check_product(ingredient.name)
                if fridge_product is None:
                    print(f"{ingredient.name} was not found in the fridge")
                    print("Recipe is not craftable")
                    return False
                quantity_difference = self.check_product_quantity(fridge_product, ingredient.quantity)
                if quantity_difference < 0:
                    print(f"Missing {abs(quantity_difference)} x {fridge_product.name}")
                    print("Recipe is not craftable")
                    return False
            print("Recipe is craftable")
            return True
    

def main():
    fridge = Fridge()
    recipe = Recipe()

    while True:
        print('''
-------------------- Welcome To Main Fridge Menu --------------------

        0: Exit
        1: Add a new product
        2: Checks fridge for a product
        3: Remove existing product
        4: Prints the contents
        5: Add products to recipe
        6: Remove products from recipe
        7: Change ingridient quantity of the recipe
        8: Print current recipe
        9: Check if recipe is craftable

---------------------------------------------------------------------
              ''')



        choice = input("Select the menu item you would like to do: ")

        if choice.startswith('0'):
            break
        elif choice.startswith('1'):
            input_name = input("Which product would you like to add: ")
            input_quantity = float(input("Input product quantity: "))
            fridge.add_product(input_name, input_quantity)

        elif choice.startswith('2'):
            input_name = input("Which product would you like to check: ")
            index, product = fridge.check_product(input_name)
            print(f"{product} is item number:{index+1} in the fridge")

        elif choice.startswith('3'):
            input_name = input("Choose which product you would like to remove from the fridge: ")
            quantity = float(input("Quantity: "))
            fridge.remove_product(input_name, quantity)

        elif choice.startswith('4'):
            print("Current contents of the fridge:")
            fridge.print_contents()

        elif choice.startswith('5'):
            input_recipe_name = input("Which recipe would you like to add: ")
            input_recipe_quantity = float(input("Input product quantity: "))
            input_product = Product(input_recipe_name, input_recipe_quantity)
            recipe.add_ingredient(input_product)
        
        elif choice.startswith('6'):
            input_ingridient_id = int(input("Choose which recipe you would like to remove from the fridge: "))
            recipe.remove_ingredient(input_ingridient_id-1)

        elif choice.startswith('7'):
            input_ingridient_id = int(input("Which recipe would you like to change: "))
            input_ingridient_quantity = float(input("Input recipe quantity: "))
            recipe.change_ingredient_quantity(input_ingridient_id-1, input_ingridient_quantity)

        elif choice.startswith('8'):
            print("Contents of the recipe: ")
            recipe.print_recipe()

        elif choice.startswith('9'):
            fridge.check_recipe(recipe)        
        else:
            print("Incorrect command, please try again!")

Fridge().add_product("milk", 1)
Recipe().add_ingredient(Product("milk", 1))
            
if __name__ == "__main__":
    main()














    # meniukas | vartotojo sasaja

# apple = Product('apple', 1)
# another_apple = Product('apple', 1)

# print(apple == another_apple)