class HotBeverage:
    price = 0.30
    name = "hot beverage"
    description = "Just some hot water in a cup."

    def describe(self):
        return self.description

    def __str__(self):
        return "name : " + self.name + "\nprice : " + str(self.price) + "\ndescription : " + self.describe()

class Coffee(HotBeverage):
    price = 0.40
    name = "coffee"
    description = "A coffee, to stay awake."

class Tea(HotBeverage):
    price = 0.30
    name = "tea"
    description = "Just some hot water in a cup."

class Chocolate(HotBeverage):
    price = 0.50
    name = "chocolate"
    description = "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    price = 0.45
    name = "cappuccino"
    description = "Un po’ di Italia nella sua tazza!"

def beverages():
    hot_beverage = HotBeverage()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    print("---------------------------------------------")
    print(hot_beverage)
    print("---------------------------------------------")
    print(coffee)
    print("---------------------------------------------")
    print(tea)
    print("---------------------------------------------")
    print(chocolate)
    print("---------------------------------------------")
    print(cappuccino)
    print("---------------------------------------------")

if __name__ == "__main__":
    beverages()