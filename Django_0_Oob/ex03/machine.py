import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:

    class EmptyCup(HotBeverage):
        def __init__(self):
            self.name = "empty cup"
            self.price = 0.90

        def describe(self) -> str:
            return "An empty cup?! Gimme my money back!"
        
        def __str__(self):
            return f"name : {self.name}\nprice : {self.price}\ndescription : {self.describe()}"

    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("❌ This coffee machine has to be repaired.")

    def __init__(self):
        self.broken_count = 10 

    def repair(self):
        self.broken_count = 10
        return "✅ This coffee machine has been repaired."

    def serve(self, drink: HotBeverage) -> HotBeverage:
        if self.broken_count <= 0:
            raise CoffeeMachine.BrokenMachineException()
        self.broken_count -= 1
        if random.randint(0, 5) == 1:
            return CoffeeMachine.EmptyCup()
        return drink

def print_box(header, content, footer=''):
    box_width = 50
    print(header.center(box_width, '-'))
    print(content.center(box_width))
    if footer:
        print(footer.center(box_width, '-'))

def print_ascii_art():
    art = """
                     ________
                    /        \\
                   |  _   _  |
                   | | | | | |
                   | | | | | |
                   | | | | | |
                   | | | | | |
                    \\_______/
                   /         \\
                  /___________\\
    """
    return art

def machine():
    coffee_machine = CoffeeMachine()
    beverages = [Coffee(), Tea(), Chocolate(), Cappuccino()]
    print_box("Welcome to the Coffee Machine!", print_ascii_art())
    
    for _ in range(15):
        try:
            beverage = random.choice(beverages)
            print_box("Trying to Serve", str(beverage))
            served_beverage = coffee_machine.serve(beverage)
            print_box("Served", str(served_beverage))
        except CoffeeMachine.BrokenMachineException as e:
            print()
            print_box("Error", str(e), "Repairing...")
            repair_message = coffee_machine.repair()
            print_box("", repair_message)
            print_box("Coffee Machine is ready to serve!", print_ascii_art())
        print()

if __name__ == "__main__":
    machine()
