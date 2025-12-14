import random
alcohol_bar = ["Teqilla", "Rum", "Vodka", "Gin", "Champangine", "Tripple sec", "Aperol"]
non_alco_bar = ["Cola", "Lemon juice", "Tonic", "Orange juice", "Sugar syrup", "Lemon-lime soda", "Blue curacao", "Grenadine", "Peach concentrate", "Mint"]
bar = alcohol_bar + non_alco_bar


coctails = {"Long island": ["Teqilla", "Rum", "Vodka", "Gin", "Tripple sec", "Cola"],
            "Mojito": ["Rum", "Soda", "Lemon juice", "Sugar syrup", "Mint"],
            "Cuba libre": ["Rum", "Cola"],
            "Gin tonic": ["Gin", "Tonic"],
            "Margarita": ["Teqilla", "Tripple sec"],
            "Screwdriver": ["Vodka", "Orange juice"],
            "Gin sour": ["Gin", "Lemon juice", "Sugar syrup"],
            "Daiqiri": ["Rum", "Lime juice", "Sugar syrup"],
            "Electric lemonade": ["Vodka", "Lemon juice", "Sugar syrup", "Lemon-lime soda", "Blue curacao"],
            "Teqilla sunrise": ["Teqilla", "Grenadine", "Orange juice"],
            "Bellini": ["Champangine", "Peach concentrate"],
            "Mimosa": ["Champangine", "Orange juice"], 
            "French 75": ["Champangine", "Gin", "Lemon juice", "Sugar syrup"],
            "Aperol Spritz": ["Champangine", "Aperol"],
            "Northern lights": ["Champangine", "Vodka", "Lemon juice", "Sugar syrup"],
            "Cosmopolitan": ["Vodka", "Tripple sec", "Cranberry juice", "Lemon juice"]}

def get_coctail(val):
    for key, value in coctails.items():
        if val == value:
            return key
    return "No coctail"

def in_coctails(val):
    return True if val in coctails else False


def run(inp_bar):
    print("Input values:", list(set(inp_bar)), "\n")
    #total_enough = []
    #total_not_enough = []
    for recepie in coctails.values():
        remain = list(set(recepie) - set(inp_bar))
        if (sorted(remain) != sorted(recepie)):
            if not remain:
                #total_enough.append(f"You got everything for {get_coctail(recepie)}.\n")
                print(f"You got everything for {get_coctail(recepie)}.")
            else:
                remain = ", ".join(remain)
                #total_not_enough.append(f"For {get_coctail(recepie)} not enough {remain}.\n")
                print(f"For {get_coctail(recepie)} not enough {remain}.")
    #print(total_enough, total_not_enough)
    print("")

while True:
    bar = input().split(", ")
    run(bar)

# for i in range(5):
#     test_vals = [bar[random.randrange(len(bar))] for i in range(random.randrange(1, len(bar)))]
#     run(test_vals)
