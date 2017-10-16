def remove_duplicates(x):
  y =[]
  for i in x:
    if i not in y:
    	y.append(i)
  return y

print (remove_duplicates([1,2,1,1,3,4,5,2,7]))