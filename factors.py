while True:
    findFactorsOf = int(input("What number do you want to find factors of? "))
    divisor = 1
    factorList = []

    while True:
        x = findFactorsOf / divisor
        wholeOrNot = x - int(x) == 0
        if wholeOrNot:
            factorList.append(divisor)
        divisor = divisor + 1
        if divisor > findFactorsOf:
            break

    print(f'''The factors of {findFactorsOf} are {factorList}
''')
