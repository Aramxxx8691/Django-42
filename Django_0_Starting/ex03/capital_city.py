import sys

def capital_city(argv):

    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }

    if argv in states:
        if states[argv] in capital_cities:
            print(capital_cities[states[argv]])
    else:
        print("Unknown state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        capital_city(sys.argv[1])
    