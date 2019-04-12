def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product


num = int(input("Enter numer: "))

result = factorial(num)

print(result)
