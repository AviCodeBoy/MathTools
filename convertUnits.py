def km_mi(unit, amount):
    if unit == "km":
        mi = amount / 1.609
        return mi
    if unit == "mi":
        km = amount * 1.609
        return km


unit = input("km or mi? ")
amount = int(input(f"How many {unit} to you want to convert to the opposite unit? "))
print(f"The answer is {km_mi(unit, amount)}.")
