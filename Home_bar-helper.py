import random
alcohol_bar = ["Teqilla", "Rum", "Vodka", "Gin"]
non_alco_bar = ["Cola", "Lemon juice", "Tripple sec", "Tonic", "Orange juice", "Sugar syrup", "Lemon-lime soda", "Blue curacao", "Grenadine"]
bar = alcohol_bar + non_alco_bar


coctails = {"Long island": ["Teqilla", "Rum", "Vodka", "Gin", "Tripple sec", "Cola"],
            #"Whiskey cola": ["Whiskey", "Cola"],
            "Cuba libre": ["Rum", "Cola"],
            "Gin tonic": ["Gin", "Tonic"],
            "Margarita": ["Teqilla", "Tripple sec"],
            "Screwdriver": ["Vodka", "Orange juice"],
            "Gin sour": ["Gin", "Lemon juice", "Sugar syrup"],
            "Daiqiri": ["Rum", "Lime juice", "Sugar syrup"],
            "Electric lemonade": ["Vodka", "Lemon juice", "Sugar syrup", "Lemon-lime soda", "Blue curacao"],
            "Teqila sunrise": ["Teqila", "Grenadine", "Orange juice"]}

def get_coctail(val):
    for key, value in coctails.items():
        if val == value:
            return key
    return "No coctail"

def in_coctails(val):
    return True if val in coctails else False


def run(inp_bar):
    print("Input values:", list(set(inp_bar)))
    for recepie in coctails.values():
        remain = list(set(recepie) - set(inp_bar))
        if (sorted(remain) != sorted(recepie)):
            if not remain:
                print(f"You got everything for {get_coctail(recepie)}.")
            else:
                remain = ", ".join(remain)
                print(f"For {get_coctail(recepie)} not enough {remain}.")

    print("")

for i in range(5):
    test_vals = [bar[random.randrange(len(bar))] for i in range(random.randrange(1, len(bar)))]
    run(test_vals)
