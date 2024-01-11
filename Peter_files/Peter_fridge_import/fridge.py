from product import Product
from recipe import Recipe


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