def main():
    pass

def insert_item(item_name, item_quantity): #Balys
    item_add = {"Item name:": item_name, "Item quantity": item_quantity}
    fridge_items.append(item_add)
    print(f"{item_quantity}x{item_name} was added to the fridge")

def remove_item():
    pass

def search_item(string_entered: str, fridge_content={'None':0.00} ):
    for key in fridge_content:
        if str(key).startswith(string_entered):
            print(f"Item found {key} with quantity {fridge_content[key]}!")
        else:
            print("No items found!")
    

def print_items():
    pass




""" Komandinio darbo užduotis
===[ Šaldytuvas ]===

Reikalavimai:

* Šaldytuvo turinys - žodynas, kurio raktas yra produkto pavadinimas, reikšmė - kiekis (float).
* Pridėti produktą į šaldytuvą. Pridedant egzistuojantį produktą, kiekiai sudedami su esančiais.
* Išimti produktą iš šaldytuvo. Išimant egzistuojantį produktą, kiekis atitinkamai sumažinamas.
* Patikrinti, ar reikiamas produkto kiekis yra šaldytuve.
* Išspausdinti visą šaldytuvo turinį su kiekiais.

BONUS:

* Patikrinti, ar receptas išeina. 
** Recepto įvedimas vyksta viena eilute, kuri po to išdalinama. Pva.: Sūris: 0.5, Pomidoras: 2, Duona: 0.4
** Jeigu receptas neišeina, išvardinti kiek ir kokių produktų trūksta.

"""
