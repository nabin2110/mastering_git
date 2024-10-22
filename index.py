class Car:
    def __init__(self,model,brand,price,launch_date):
        self.model = model
        self.brand = brand
        self.price = price
        self.launch_date = launch_date

    def get_car_detail(self):
        print(f"the model of the car is {self.model} and the brand of the car is {self.brand} and the price of the car is {self.price} and it's launch date on {self.launch_date}")


toyota = Car(model="toyota",brand="toyota",price=200000,launch_date="2022/01/12")
toyota.get_car_detail()