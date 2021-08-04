multiplyBy = 1
baseNumber = 5
roof = 100

while True:
    product = baseNumber * multiplyBy
    multiplyBy += 1
    if product > roof:
        break
    print(product)