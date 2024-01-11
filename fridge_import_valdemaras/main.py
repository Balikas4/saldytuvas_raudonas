from fridge import Fridge
from recipe import Recipe
from product import Product

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
        7: Change ingredient quantity of the recipe
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
            input_unit_of_measurement = input("Input unit of measurment: ")
            fridge.add_product(input_name, input_quantity, input_unit_of_measurement)

        elif choice.startswith('2'):
            input_name = input("Which product would you like to check: ")
            index, product = fridge.check_product(input_name)
            if index == None:
                print(f"{input_name} was not found in the fridge. ")
            else:
                print(f"{product} is item number:{index+1} in the fridge. ")

        elif choice.startswith('3'):
            input_name = input("Choose which product you would like to remove from the fridge: ")
            input_quantity = float(input("Input product quantity: "))
            fridge.remove_product(input_name, input_quantity)

        elif choice.startswith('4'):
            print("Current contents of the fridge:")
            fridge.print_contents()

        elif choice.startswith('5'):
            input_recipe_name = input("Which recipe would you like to add: ")
            input_recipe_quantity = float(input("Input recipe quantity: "))
            input_unit_of_measurement = input("Input unit of measurment: ")
            input_product = Product(input_recipe_name, input_recipe_quantity, input_unit_of_measurement)
            recipe.add_ingredient(input_product)
        
        elif choice.startswith('6'):
            input_ingredient_name = (input("Choose which recipe you would like to remove from the fridge: "))
            input_ingredient_quantity = float(input("Input recipe quantity: "))
            recipe.remove_ingredient(input_ingredient_name, input_ingredient_quantity)

        elif choice.startswith('7'):
            input_ingredient_name = (input("Which recipe would you like to change: "))
            input_ingredient_quantity = float(input("Input recipe quantity: "))
            recipe.change_ingredient_quantity(input_ingredient_name, input_ingredient_quantity)

        elif choice.startswith('8'):
            print("Contents of the recipe: ")
            recipe.print_recipe()

        elif choice.startswith('9'):
            fridge.check_recipe(recipe)        
        else:
            print("Incorrect command, please try again!")

fridge = Fridge()
fridge.add_product("milk", 1.1, "l")
recipe = Recipe()
recipe.add_ingredient(Product("milk", 1.1, "l"))
            
if __name__ == "__main__":
    main()