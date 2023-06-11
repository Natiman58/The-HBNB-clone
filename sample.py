class Vehicle:
    def __init__(self, color, make, model):
        self.color = color
        self.make = make
        self.model = model


class Car(Vehicle):
    def __init__(self, color, make, model, num_doors):
        super().__init__(color, make, model)
        self.num_doors = num_doors


my_car = Car("red", "Toyota", "corolla", 4)
print(my_car.color)
print(my_car.make)
print(my_car.model)
print(my_car.num_doors)