from product import Product
from recipe import Recipe
from fridge import Fridge


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
   