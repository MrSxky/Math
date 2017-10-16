def product(x):
  product = 1
  for i in x:
    product *= i
  return product

print (product([1,2,3]))