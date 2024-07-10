import sys

def find_key_by_value(d, t_value):
    for key, value in d.items():
        if value == t_value:
            return key
    return ("Unknown capital")

def all_in(argv):

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

    argv = argv.split(',')
    argv = [x.strip() for x in argv if x.strip()]

    for val in argv:
        v = find_key_by_value(states, find_key_by_value(capital_cities, val))
        if v != "Unknown capital":
            print(val, "is the capital of", v)
        else:
            if val in states:
                if states[val] in capital_cities:
                    print(val, "is a state of", capital_cities[states[val]])
            else:
                print(val, "is neither a capital city nor a state")

if __name__ == '__main__':
    if len(sys.argv) == 2:
        all_in(sys.argv[1])
    