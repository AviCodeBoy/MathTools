def prime_or_not(numberToTest):
    findFactorsOf = numberToTest
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
        return numberToTest


number = 1
primeNums = []
maxim = 200

while True:
    result = prime_or_not(number)
    if number > maxim:
        break
    if result == number:
        primeNums.append(number)
    number = number + 1

print(primeNums)
