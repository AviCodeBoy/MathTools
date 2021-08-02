while True:
    findFactorsOf = int(input("Enter a number and you will know whether it is prime or non-prime. "))
    divisor = 1
    factorList = []
    comparator = [1, findFactorsOf]

    while True:
        x = findFactorsOf / divisor
        wholeOrNot = x - int(x) == 0
        if wholeOrNot:
            factorList.append(divisor)
        divisor = divisor + 1
        if divisor > findFactorsOf:
            break

    if factorList == comparator:
        print(f"{findFactorsOf} is prime")
    elif factorList != comparator:
        print(f"{findFactorsOf} is non-prime")