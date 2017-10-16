def factorial(x):
    y = 1
    while x > 0:
        y = x * y
        x -= 1

        print (y)


factorial(5)