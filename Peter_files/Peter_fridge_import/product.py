class Product:
    def __init__(self, name:str, quantity:float, unit_of_measurement:str = 'unit', **kwargs) -> None:
        self.name = name
        self.quantity = quantity
        self.unit_of_measurement = unit_of_measurement
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self) -> str:
        return f"{self.name}: {self.quantity}"
    
    def __repr__(self) -> str:
        return f"({self.name}, {self.quantity})"
