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

    def remove_ingredient(self, ingredient_id:int):
        self.ingredients.pop(ingredient_id)


class Fridge:
    contents = []

    def check_product(self, product_name:str) -> (int, Product):
        for product_id, product in enumerate(self.contents):
            if product.name == product_name:
                return product_id, product
        return None, None
    
    def check_product_quantity(self, product:Product, quantity:float):
        return product.quantity - quantity

    def add_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            product.quantity += quantity
        else:
            self.contents.append(Product(name, quantity))

    def remove_product(self, name:str, quantity:float):
        product_id, product = self.check_product(name) # nenaudojamus kintamuosius galima vadinti tiesiog _
        if product is not None:
            if product.quantity >= quantity:
                product.quantity -= quantity
                if product.quantity == 0:
                    self.contents.remove(Product(name, quantity))
                print(f"{name} was removed from the fridge.")
            else:
                print(f"Not enough {name} quantity in the fridge.")
        else:
            print(f"{name} does not exist in the fridge.")           
        

    def print_contents(self):
        print('Contents of the fridge:')
        for index, product in enumerate(self.contents, start=1):
            print(f'{index}. {product.name} : {product.quantity}')

    def check_recipe(self, recipe:Recipe):    
        for ingredient in recipe.ingredients:
            product_id, _ = Fridge().check_product(ingredient.name)
            if product_id is None:
                print(f"{ingredient.name} was not found in the fridge")
                print("Recipe is not craftable")
                return False
        print("Recipe is craftable")
        return True
   


def main():
    fridge = Fridge()
    # meniukas | vartotojo sasaja

# apple = Product('apple', 1)
# another_apple = Product('apple', 1)

# print(apple == another_apple)
