def anti_vowel(text):
  new = ""
  for n in text:
    if n == "A" or n =="a" or  n == "E" or n =="e" or n == "I" or n =="i" or n == "O" or n =="o" or n == "U" or n =="u":
      new = new
    else:
      new = new + n
  print (new)

anti_vowel("Hey look Words!")