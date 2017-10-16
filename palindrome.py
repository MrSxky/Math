def palind(x):
    if x == x[::-1]:
        return "palindrome"
    else:
        return "not a palindrome"





print (palind("5225"))
