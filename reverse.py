def reverse(text):
    word = ""
    l = len(text) - 1
    print (text[l])
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

print (reverse("lion"))