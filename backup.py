coctails = {"Long island": ["Teqilla", "Rum", "Vodka", "Whiskey", "Tripple sec", "Cola"],
            "Whiskey cola": ["Whiskey", "Cola"],
            "Cuba libre": ["Rum", "Cola"],
            "Gin tonic": ["Gin", "Tonic"],
            "Margarita": ["Teqilla", "Tripple sec"],
            "Screwdriver": ["Vodka", "Orange juice"]}

def get_coctail(val):
    for key, value in coctails.items():
        if val == value:
            return key
    return "No coctail"

while True:
    inp_bar = input("Your bar: ").split()
    
    for recepie in coctails.values():
        remain = list(set(recepie) - set(inp_bar))
        if (sorted(remain) != sorted(recepie)):
            if not remain:
                print(f"You got everything for {get_coctail(recepie)}.")
            else:
                print(f"For {get_coctail(recepie)} not enough {", ".join(remain)}.")

    print("")