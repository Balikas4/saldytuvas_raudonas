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
            print(f"{name} was already in the fridge and we added {quantity}{unit_of_measurement} more.")
        else:
            self.contents.append(Product(name, quantity, unit_of_measurement))
            print(f"{name} {quantity} {unit_of_measurement} was added to the fridge.")

    def print_contents(self):
        for index, line in enumerate(self.contents, start=1):
            print(f"{index} - {line} {line.unit_of_measurement}")

    def remove_product(self, name:str, quantity:float):
        self.print_contents()
        product_id, product = self.check_product(name)
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantity
                print(f"{quantity} x {product} was removed from fridge. ")
                if product.quantity == 0:
                    self.contents.remove(product)
                    print(f"All the {product} was removed")
            else:
                print(f"Not enough {name} in the fridge.")
        else:
            print(f"Product {name} does not exist in the fridge.")

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