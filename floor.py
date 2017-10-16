def floor(x):
    total = 0
    while x>0:
        total= total + x%10
        x = x // 10
        print (x)
        print (total)

floor(1234)