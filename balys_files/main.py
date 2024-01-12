from fridge import *

def main():
    fridge = Fridge()
    recipe = Recipe()
    while True:
        print('''
-------------------- Main Fridge Menu --------------------
check - Checks fridge for a product
add - Add a new product
remove - Remove existing product
print - Prints the contents
recipe add - Add products to recipe
recipe remove - Remove products from recipe
recipe change - Change ingridient quantity of the recipe
recipe print - Print current recipe
recipe check - Check if recipe is craftable
exit - Exit
----------------------------------------------------------
              ''')
        choice = input("Your choice: ")
        if choice.startswith("exit"):
            break
        elif choice.startswith("check"):
            input_name = input("Input name: ")
            index, product = fridge.check_product(input_name)
            if index == None:
                print(f"{input_name} was not found in the fridge")
            else:
                print(f"{product} is item number:{index+1} in the fridge")
        elif choice.startswith("add"):
            input_name = input("Input name: ")
            input_quantity = float(input("Input quantity: "))
            input_unit_of_measurement = input("Input unit of measurment: ")
            fridge.add_product(input_name, input_quantity, input_unit_of_measurement)
        elif choice.startswith("remove"):
            if len(fridge.contents) == 0:
                print("Fridge is empty...")
            else:
                input_name = input("Input name: ")
                input_quantity = float(input("Input quantity: "))
                fridge.remove_product(input_name, input_quantity)
        elif choice.startswith("print"):
            if len(fridge.contents) == 0:
                print("Fridge is empty...")
            else:
                print("Current contents of the fridge:")
                fridge.print_contents()
        elif choice.startswith("recipe add"):
            input_recipe_name = input("Input product name: ")
            input_recipe_quantity = float(input("Input product quantity: "))
            input_unit_of_measurement = input("Input unit of measurment: ")
            input_product = Product(input_recipe_name, input_recipe_quantity, input_unit_of_measurement)
            recipe.add_ingredient(input_product)
        elif choice.startswith("recipe change"):
            input_ingridient_name = input("Input existing product name: ")
            input_ingridient_quantity = float(input("Input new product quantity: "))
            recipe.change_ingredient_quantity(input_ingridient_name, input_ingridient_quantity)
        elif choice.startswith("recipe remove"):
            if len(recipe.ingredients) == 0:
                print("Recipe is empty...")
            else:
                input_ingridient_name = input("Input product name: ")
                input_ingridient_quantity = float(input("Input product quantity: "))
                recipe.remove_ingredient(input_ingridient_name, input_ingridient_quantity)
        elif choice.startswith("recipe print"):
            if len(recipe.ingredients) == 0:
                print("Recipe is empty...")
            else:
                print("Contents of the recipe:")
                recipe.print_recipe()
        elif choice.startswith("recipe check"):
            if len(recipe.ingredients) ==0:
                print("Fridge is empty...")
            else:
                fridge.check_recipe(recipe)
        else:
            print("Bad choice, try again")

fridge = Fridge()
fridge.add_product("milk", 1.1, "l")
recipe = Recipe()
recipe.add_ingredient(Product("milk", 1.1, "l"))

if __name__ == "__main__":
    main()