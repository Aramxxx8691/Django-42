class Intern:
    def __init__(self):
        self.name = "My name? I’m nobody, an intern, I have no name."

    def __str__(self):
        return self.name
    
    def builder(self, name):
        self.name = name
        return self.name

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return self.Coffee()
    
    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."    

def intern():
    intern1 = Intern()
    intern2 = Intern()
    intern1.builder("Mark")
    print(intern1)
    print(intern2)
    print(intern1.make_coffee())
    try:
        print(intern2.work())
    except Exception as e:
        print(e)

if __name__ == "__main__":
    intern()